#!/usr/bin/env python3
"""魂剥ぎV8とゴルガリ・ミッドレンジの対戦を、単純な手順で回して勝率を比べる。

目的: ゴルガリ戦のSBプランを比べる。
  G1: メイン同士
  プランA: 墓地の勝ち筋のまま、相手の墓地対策に答える（思考囲い・突然の衰微・墓地の侵入者を入れる）
  プランB: 黙示録、シェオルドレッドを入れる（第8版のSB案）
相手のSB後は、致命的な一押し・選別の儀式などを抜き、未認可霊柩車3・真っ白2・戦略的裏切り3を入れる。

単純化（結果を読むときに必ず考える）:
- 戦闘でブロックしない。両者とも攻撃できるクリーチャー全員で毎ターン攻撃する（レースの計算）
- 色は無視し、土地の枚数をマナとする。タップインは無視する
- 相手の除去は「こちらの一番強い脅威」から順に、撃てるものを撃つ。こちらは除去を相手の一番強いクリーチャーに撃つ
- カードの選択（ハンデスで何を抜くか、墓地対策で何を追放するか）は決まった優先順で行う
- 12ターンで決着しなければ引き分けとして数える
カードのテキストは oracle/cards.csv で確かめた。

使い方:
    python3 tools/v8_golgari_sim.py
"""
import random

N = 4000
MAXT = 12

# ---------------- カードの定義 ----------------
# 自分の墓地に置くクリーチャー: 魂剥ぎに渡すキーワード
DONOR_KW = {
    'RW': {'hexproof'},
    'SA': {'double', 'haste', 'vigilance'},
    'BR': {'flying'},
    'AT': {'flying', 'vigilance', 'deathtouch', 'lifelink'},
}
YARD_CREATURES = ['BR', 'SA', 'AT', 'RW', 'SF', 'SSM', 'WI', 'TR', 'SH']
CREATURE_STATS = {  # 全体リアニメイトで戻ったときなどの能力（パワー、キーワード、マナ総量）
    'RW': (5, {'hexproof'}, 7), 'SA': (3, {'double', 'haste', 'vigilance'}, 5), 'BR': (6, {'flying'}, 8),
    'AT': (7, {'flying', 'lifelink', 'deathtouch', 'vigilance'}, 7), 'SF': (4, set(), 6), 'SSM': (4, set(), 4),
    'WI': (6, set(), 5), 'TR': (3, {'ward'}, 3), 'SH': (4, {'deathtouch'}, 4),
}
OPP_CREATURE_STATS = {'Cub': (2, 2), 'Trespasser': (3, 3), 'Sheoldred': (4, 4)}


class Side:
    def __init__(self, deck, rng):
        self.lib = deck[:]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.yard = []
        self.lands = 0
        self.life = 20
        self.board = []  # dict(name, power, kw, mv, sick)
        self.rng = rng

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def play_land(self):
        if 'L' in self.hand:
            self.hand.remove('L'); self.lands += 1


def threat_value(c):
    p = c['power'] * (2 if 'double' in c['kw'] else 1)
    return p + (3 if 'hexproof' in c['kw'] else 0) + (2 if c['name'] == 'Sheoldred' else 0)


# ---------------- 自分 ----------------
class Me(Side):
    def __init__(self, deck, rng):
        super().__init__(deck, rng)
        self.machines = False  # メカの天才が戦場にある（絶望招来の対象）

    def need_land(self):
        return self.lands + self.hand.count('L') < 4

    def discard_one(self, keep=()):
        h = self.hand
        for c in ['BR', 'SA', 'AT', 'RW']:
            if c in h:
                h.remove(c); self.yard.append(c); return c
        if h.count('L') >= 2 and not self.need_land():
            h.remove('L'); self.yard.append('L'); return 'L'
        for c in ['SF', 'SSM']:
            if h.count(c) >= 2:
                h.remove(c); self.yard.append(c); return c
        for c in ['PU', 'GZ', 'BT', 'WI', 'DG', 'GR', 'MA', 'AD', 'TS', 'TR', 'SH', 'L', 'SF', 'SSM']:
            if c in h and c not in keep:
                h.remove(c); self.yard.append(c); return c
        if h:
            c = h.pop(0); self.yard.append(c); return c
        return None

    def dig(self, rev):
        h = self.hand
        wants = (['SSM'] if 'SSM' not in h else []) + (['SF'] if 'SF' not in h else []) \
            + (['L'] if self.need_land() else []) + ['SSM', 'SF']
        take = next((c for c in wants if c in rev), None)
        if take:
            rev.remove(take); h.append(take)
        self.yard.extend(rev)

    def yard_creature_power(self, yard):
        return sum(CREATURE_STATS[c][0] * (2 if 'double' in CREATURE_STATS[c][1] else 1) for c in yard if c in CREATURE_STATS)


def my_turn(me, op, t, first):
    if not first:
        me.draw()
        if any(c['name'] == 'Sheoldred' for c in op.board):
            me.life -= 2
        if any(c['name'] == 'SH' for c in me.board):
            me.life += 2
    me.play_land()
    mana = me.lands
    for c in me.board:
        c['sick'] = False
    h = me.hand
    # 1. ハンデス（2ターン目まで）
    if 'TS' in h and mana >= 1 and t <= 3:
        h.remove('TS'); me.yard.append('TS'); mana -= 1; me.life -= 2
        for want in ['GoBlank', 'Betrayal', 'Hearse', 'Dellian', 'Sheoldred', 'Bitter', 'Extinction', 'Invoke', 'Trespasser', 'Cub', 'Decay']:
            if want in op.hand:
                op.hand.remove(want); break
    # 2. 置物と小さいクリーチャーへの回答（突然の衰微）
    while 'AD' in h and mana >= 2:
        cs = [c for c in op.board if c['mv'] <= 3 and c['name'] != 'Earth']
        if not op.hearse and not cs:
            break
        h.remove('AD'); me.yard.append('AD'); mana -= 2
        if op.hearse:
            op.hearse = False
        else:
            c = max(cs, key=threat_value); op.board.remove(c); op.yard.append(c['name'])
            if 'ward' in c['kw']:
                me.discard_one()
    # 3. 除去（苦々しい勝利・致命的な一押し）
    for name, cost in (('BT', 2), ('PU', 1)):
        while name in h and mana >= cost:
            cs = [c for c in op.board if name == 'BT' or c['mv'] <= 2]
            if not cs:
                break
            c = max(cs, key=threat_value)
            h.remove(name); me.yard.append(name); mana -= cost
            if name == 'BT':
                if any(x in h for x in ['BR', 'SA', 'AT', 'RW']):
                    me.discard_one()
                else:
                    me.life -= 3
            if 'ward' in c['kw']:
                me.discard_one()
            op.board.remove(c); op.yard.append(c['name'])
    # 4. 勝ち筋
    progress = True
    while progress:
        progress = False
        # スーペリア・スパイダーマン
        if 'SSM' in h and mana >= 4:
            choice = None
            my_power = me.yard_creature_power(me.yard)
            op_back = sum(OPP_CREATURE_STATS.get(x, (0, 0))[0] for x in op.yard)
            if 'BR' in me.yard and my_power - op_back >= 8:
                choice = 'BR'
            elif 'SA' in me.yard:
                choice = 'SA'
            elif 'AT' in me.yard:
                choice = 'AT'
            elif 'Sheoldred' in op.yard:
                choice = 'OPSH'
            elif 'BR' in me.yard and my_power > op_back:
                choice = 'BR'
            if choice:
                h.remove('SSM'); mana -= 4
                if choice == 'BR':
                    me.yard.remove('BR')
                    for c in me.board:
                        me.yard.append(c['name'])  # 生け贄（トークンでないものは墓地へ）
                    me.board = []
                    for c in list(op.board):
                        op.yard.append(c['name'])
                    op.board = []
                    back = [x for x in me.yard if x in CREATURE_STATS and x != 'SSM_COPY']
                    for x in back:
                        me.yard.remove(x)
                        p, kw, mv = CREATURE_STATS[x]
                        me.board.append(dict(name=x, power=p, kw=set(kw), mv=mv, sick=False))
                    if any(c['name'] == 'SA' for c in me.board):
                        for c in me.board:
                            c['kw'].add('haste')
                    opb = [x for x in op.yard if x in OPP_CREATURE_STATS]
                    for x in opb:
                        op.yard.remove(x)
                        p, mv = OPP_CREATURE_STATS[x]
                        op.board.append(dict(name=x, power=p, kw={'ward'} if x == 'Trespasser' else ({'deathtouch'} if x == 'Sheoldred' else set()), mv=mv, sick=True))
                    me.board.append(dict(name='SSM', power=4, kw={'flying'}, mv=8, sick=True))
                elif choice == 'SA':
                    me.yard.remove('SA')
                    me.board.append(dict(name='SSM', power=4, kw={'double', 'haste', 'vigilance'}, mv=5, sick=False))
                    for c in me.board:
                        c['kw'].add('haste')
                elif choice == 'AT':
                    me.yard.remove('AT')
                    me.board.append(dict(name='SSM', power=4, kw={'flying', 'lifelink', 'deathtouch'}, mv=7, sick=True))
                    me.draw(3)
                else:
                    op.yard.remove('Sheoldred')
                    me.board.append(dict(name='SH', power=4, kw={'deathtouch'}, mv=4, sick=True))
                progress = True; continue
        # 魂剥ぎ
        if 'SF' in h:
            need = 2 + max(0, 4 - len(me.yard))
            donors = [x for x in me.yard if x in DONOR_KW]
            if mana >= need and donors:
                h.remove('SF'); mana -= need
                kw = set()
                exiled = 0
                for d in sorted(donors, key=lambda x: ['RW', 'SA', 'AT', 'BR'].index(x)):
                    if exiled >= 4:
                        break
                    me.yard.remove(d); kw |= DONOR_KW[d]; exiled += 1
                while exiled < 4 and me.yard:
                    me.yard.pop(0); exiled += 1
                me.board.append(dict(name='SF', power=4, kw=kw, mv=6, sick='haste' not in kw))
                progress = True; continue
        # 黙示録、シェオルドレッド
        if 'SH' in h and mana >= 4:
            h.remove('SH'); mana -= 4
            me.board.append(dict(name='SH', power=4, kw={'deathtouch'}, mv=4, sick=True)); progress = True; continue
        # 墓地の侵入者
        if 'TR' in h and mana >= 3:
            h.remove('TR'); mana -= 3
            me.board.append(dict(name='TR', power=3, kw={'ward'}, mv=3, sick=True))
            tgt = next((x for x in ['Sheoldred', 'Trespasser', 'Cub'] if x in op.yard), None)
            if tgt:
                op.yard.remove(tgt); op.life -= 1; me.life += 1
            progress = True; continue
        # 墓地を肥やす
        lib = me.lib
        if 'DG' in h and mana >= 3 and 'BR' not in me.yard and 'BR' in lib:
            h.remove('DG'); me.yard.append('DG'); mana -= 3
            lib.remove('BR'); me.yard.append('BR'); me.rng.shuffle(lib); progress = True; continue
        if 'MA' in h and mana >= 2:
            h.remove('MA'); mana -= 2; me.machines = True
            me.yard.extend(lib[:2]); del lib[:2]; me.draw(2); me.discard_one(); me.discard_one(); progress = True; continue
        if 'GR' in h and mana >= 2:
            h.remove('GR'); me.yard.append('GR'); mana -= 2
            rev = lib[:5]; del lib[:5]; me.dig(rev); progress = True; continue
        if 'WI' in h and mana >= 2:
            h.remove('WI'); me.yard.append('WI'); mana -= 2; me.draw(2); me.discard_one(); progress = True; continue
        if 'GZ' in h and mana >= 1:
            h.remove('GZ'); me.yard.append('GZ'); mana -= 1
            top = lib[:3]; del lib[:3]; keep = []
            for c in top:
                if (c == 'SSM' and 'SSM' not in h) or (c == 'SF' and 'SF' not in h) or (c == 'L' and me.need_land() and 'L' not in keep):
                    keep.append(c)
                else:
                    me.yard.append(c)
            lib[:0] = keep; progress = True; continue
        if 'RW' in h and mana >= 1:
            h.remove('RW'); me.yard.append('RW'); mana -= 1; me.draw(); progress = True; continue
    # 5. 攻撃
    for c in me.board:
        if not c['sick'] or 'haste' in c['kw']:
            dmg = c['power'] * (2 if 'double' in c['kw'] else 1)
            op.life -= dmg
            if 'lifelink' in c['kw']:
                me.life += dmg
            if c['name'] == 'TR':
                tgt = next((x for x in ['Sheoldred', 'Trespasser', 'Cub'] if x in op.yard), None)
                if tgt:
                    op.yard.remove(tgt); op.life -= 1; me.life += 1


# ---------------- ゴルガリ ----------------
class Opp(Side):
    def __init__(self, deck, rng):
        super().__init__(deck, rng)
        self.hearse = False
        self.dellian = 0
        self.annex = 0


def opp_turn(op, me, t, first):
    if not first:
        op.draw()
        if any(c['name'] == 'SH' for c in me.board):
            op.life -= 2
    op.play_land()
    mana = op.lands
    for c in op.board:
        c['sick'] = False
    h = op.hand
    # 1. ハンデス
    if 'Thoughtseize' in h and mana >= 1 and t <= 3:
        h.remove('Thoughtseize'); op.yard.append('Thoughtseize'); mana -= 1; op.life -= 2
        for want in ['SSM', 'SF', 'DG', 'SH', 'MA', 'GR', 'TR', 'AD', 'TS']:
            if want in me.hand:
                me.hand.remove(want); me.yard.append(want); break
    if 'Duress' in h and mana >= 1 and t <= 3:
        h.remove('Duress'); mana -= 1
        for want in ['DG', 'MA', 'GR', 'AD', 'TS', 'BT', 'WI', 'GZ']:
            if want in me.hand:
                me.hand.remove(want); me.yard.append(want); break
    # 2. 除去（こちらの強い脅威から）
    def legal(c, how):
        if how in ('Bitter', 'Dellian') and 'hexproof' in c['kw']:
            return False
        if how == 'Decay' and c['mv'] > 3:
            return False
        if how == 'Push' and c['mv'] > 2:
            return False
        return True
    for _ in range(3):
        if not me.board:
            break
        target = max(me.board, key=threat_value)
        used = False
        if op.dellian >= 3 and legal(target, 'Dellian'):
            op.dellian -= 3; used = True
        else:
            for name, cost in (('Push', 1), ('Decay', 2), ('Bitter', 2)):
                if name in h and mana >= cost and legal(target, name):
                    h.remove(name); mana -= cost; used = True
                    if name == 'Bitter':
                        op.life -= 3 if len(h) < 2 else 0
                    break
            if not used and 'Dellian' in h and mana >= 4 and legal(target, 'Dellian'):
                h.remove('Dellian'); mana -= 4; op.dellian = 2; used = True
        if used:
            if 'ward' in target['kw']:
                if h:
                    op.yard.append(h.pop())
            me.board.remove(target); me.yard.append(target['name'] if target['name'] in CREATURE_STATS else 'X')
            continue
        # 対象を取らない除去
        if 'Betrayal' in h and mana >= 2:
            h.remove('Betrayal'); mana -= 2
            c = min(me.board, key=threat_value); me.board.remove(c)
            me.yard = []  # 墓地をすべて追放
            continue
        if 'Extinction' in h and mana >= 4:
            h.remove('Extinction'); mana -= 4
            odd = [c for c in me.board if c['mv'] % 2 == 1]; even = [c for c in me.board if c['mv'] % 2 == 0]
            hit = odd if sum(map(threat_value, odd)) > sum(map(threat_value, even)) else even
            for c in hit:
                me.board.remove(c)
            continue
        if 'Invoke' in h and mana >= 5:
            h.remove('Invoke'); mana -= 5
            c = min(me.board, key=threat_value); me.board.remove(c); me.yard.append(c['name'])
            if me.machines:
                me.machines = False
            else:
                me.life -= 2; op.draw()
            me.life -= 2; op.draw()  # PWが無い
            continue
        break
    # 3. 墓地対策（こちらの墓地に勝ち筋の材料があるとき）
    key = [x for x in me.yard if x in ('BR', 'SA', 'AT', 'RW')]
    if key and 'GoBlank' in h and mana >= 3:
        h.remove('GoBlank'); mana -= 3
        me.discard_one(); me.discard_one(); me.yard = []
    elif key and 'Betrayal' in h and mana >= 2 and me.board:
        h.remove('Betrayal'); mana -= 2
        c = min(me.board, key=threat_value); me.board.remove(c); me.yard = []
    if 'Hearse' in h and mana >= 2 and not op.hearse:
        h.remove('Hearse'); mana -= 2; op.hearse = True
    if op.hearse and any(c['power'] >= 2 for c in op.board):
        # 未認可霊柩車: 搭乗2で動かし、こちらの墓地の勝ち筋の材料を2枚追放する
        exiled = 0
        for want in ['BR', 'SA', 'AT', 'RW']:
            while want in me.yard and exiled < 2:
                me.yard.remove(want); exiled += 1
    # 4. 展開
    for name, cost in (('Sheoldred', 4), ('Dellian', 4), ('Trespasser', 3), ('Annex', 3), ('Cub', 2)):
        while name in h and mana >= cost:
            h.remove(name); mana -= cost
            if name == 'Dellian':
                op.dellian = 7  # +2で出す（3点回復）
                op.life += 3
            elif name == 'Annex':
                op.annex += 1
            else:
                p, mv = OPP_CREATURE_STATS[name]
                kw = {'ward'} if name == 'Trespasser' else ({'deathtouch'} if name == 'Sheoldred' else set())
                op.board.append(dict(name=name, power=p, kw=kw, mv=mv, sick=True))
                if name == 'Cub':
                    op.board.append(dict(name='Earth', power=1, kw={'haste'}, mv=0, sick=False))
                if name == 'Trespasser':
                    tgt = next((x for x in ['BR', 'SA', 'AT', 'RW'] if x in me.yard), None)
                    if tgt:
                        me.yard.remove(tgt); me.life -= 1; op.life += 1
    if op.dellian and op.dellian < 3:
        op.dellian += 2; op.life += 3
    # 5. 攻撃
    for c in op.board:
        if not c['sick'] or 'haste' in c['kw']:
            me.life -= c['power']
            if c['name'] == 'Trespasser':
                tgt = next((x for x in ['BR', 'SA', 'AT', 'RW'] if x in me.yard), None)
                if tgt:
                    me.yard.remove(tgt); me.life -= 1; op.life += 1
    if op.lands >= 5 and mana >= 1:
        me.life -= 2  # 変わり谷
    # 6. 終了ステップ（不浄な別室）
    for _ in range(op.annex):
        op.draw(); op.life -= 2


def game(my_deck, opp_deck, seed, on_play):
    rng = random.Random(seed)
    me = Me(my_deck, random.Random(seed * 3 + 1))
    op = Opp(opp_deck, random.Random(seed * 5 + 2))
    for t in range(1, MAXT + 1):
        order = [('me', t == 1 and on_play), ('op', t == 1 and not on_play)] if on_play else [('op', t == 1 and not on_play), ('me', t == 1 and on_play)]
        for who, first in order:
            if who == 'me':
                my_turn(me, op, t, first)
            else:
                opp_turn(op, me, t, first)
            if op.life <= 0 and me.life > 0:
                return 1
            if me.life <= 0:
                return 0
    return 0.5


def deck(d):
    out = [k for k, v in d.items() for _ in range(v)]
    assert len(out) == 60, (len(out), d)
    return out


MAIN = dict(SF=4, SSM=4, RW=4, SA=3, BR=2, AT=2, GR=4, MA=4, WI=2, DG=2, GZ=1, BT=3, PU=3, L=22)


def side(main, ins, outs):
    d = dict(main)
    for k, v in outs.items():
        d[k] -= v
    for k, v in ins.items():
        d[k] = d.get(k, 0) + v
    return d


PLAN_A = side(MAIN, dict(TS=3, AD=2, TR=2), dict(BR=2, PU=3, GZ=1, DG=1))
PLAN_B = side(MAIN, dict(TS=3, TR=2, SH=2, AD=2), dict(BR=2, PU=3, DG=2, GZ=1, SA=1))
GOLGARI = dict(Cub=4, Trespasser=4, Dellian=4, Sheoldred=3, Push=4, Decay=3, Bitter=2, Thoughtseize=4, Duress=1,
               Culling=2, Annex=4, Tear=1, L=24)
GOLGARI_SB = side(GOLGARI, dict(Hearse=3, GoBlank=2, Betrayal=3), dict(Push=4, Culling=2, Tear=1, Decay=1))

if __name__ == '__main__':
    cases = [
        ('G1: メイン同士', MAIN, GOLGARI),
        ('SB後: こちらSBなし、相手は墓地対策を入れる', MAIN, GOLGARI_SB),
        ('SB後: プランA（墓地のまま対策に答える）', PLAN_A, GOLGARI_SB),
        ('SB後: プランB（黙示録、シェオルドレッドを入れる）', PLAN_B, GOLGARI_SB),
        ('参考: プランB、相手は墓地対策を入れない', PLAN_B, GOLGARI),
    ]
    print(f'勝率（引き分けは0.5勝）。各 {N} ゲーム')
    for name, mine, theirs in cases:
        res = []
        for on_play in (True, False):
            w = sum(game(deck(mine), deck(theirs), s, on_play) for s in range(N))
            res.append(f"{'先手' if on_play else '後手'} {100 * w / N:.1f}%")
        print(f'  {name}: ' + ' / '.join(res))

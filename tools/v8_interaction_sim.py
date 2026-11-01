#!/usr/bin/env python3
"""魂剥ぎV8の妨害カードが、相手の理想ムーブのキルターンを、自分が妨害に使ったターン以上に遅らせられるかを見積もる。

比べ方（共通乱数法）:
  同じシャッフルで2回ゲームを回す。1回目は妨害カードを手札に持っていても使わない。2回目は使う。
  相手のキルターンの遅れ（ΔK）と、自分の勝ち筋が成立するターンの遅れ（ΔG）を、1ゲームずつ比べる。
  ΔK ≥ ΔG なら「妨害に使ったターン以上に相手を遅らせた」と数える。

相手: MTGGoldfishの平均リスト（2026-11-01取得）の赤単果敢とイゼット果敢を、こちらがブロックしない前提で動かす（理想ムーブ）。
  - 毎ターン土地を置き、クリーチャーを先に唱え、残りのマナで呪文を全部唱えてから全員で攻撃する
  - 果敢は唱えた非クリーチャー呪文ごとに+1/+1。火力は顔に撃つ。こちらのクリーチャー（大洞窟のコウモリ）がいれば先に除去する
  - こちらのライフはショックランドなどの支払いを見込んで18から始める
自分: notes/soulflayer_v8_proposal.md の60枚。勝ち筋の判定は tools/soulflayer_v8_sim.py と同じ（色・タップインは無視）。
妨害の使い方は2通り:
  dev: 自分の展開を先にして、余ったマナで相手のターンに除去を撃つ
  int: 相手のクリーチャーがいれば、自分のターンの最初に除去を撃ってから展開し、余ったマナでも相手のターンに除去を撃つ
  どちらも、思考囲いは2ターン目まで、大洞窟のコウモリは3ターン目までに唱える

使い方:
    python3 tools/v8_interaction_sim.py
"""
import random
from statistics import mean

N = 4000
MAXT = 9
START_LIFE = 18

# ---------------- 相手のデッキ ----------------
OPP_CARDS = {
    # name: (cost, type, power, toughness, flags)
    'Swiftspear': (1, 'C', 1, 2, {'haste', 'prowess'}),
    'SoulScar': (1, 'C', 1, 2, {'prowess'}),
    'Battlemage': (1, 'C', 1, 1, {'prowess', 'prepared'}),
    'Emberheart': (2, 'C', 2, 2, {'haste', 'prowess'}),
    'Slickshot': (2, 'C', 1, 2, {'haste', 'slick'}),
    'Nemesis': (3, 'C', 3, 3, {'haste'}),
    'Kumano': (1, 'S', 0, 0, set()),
    'Burst': (1, 'I', 0, 0, set()),
    'MRage': (1, 'I', 0, 0, set()),
    'RRage': (1, 'I', 0, 0, set()),
    'Dispute': (1, 'I', 0, 0, set()),
    'Sleight': (1, 'I', 0, 0, set()),
    'Flow': (2, 'I', 0, 0, set()),
    'Boomerang': (1, 'I', 0, 0, set()),
    'Talent': (1, 'E', 0, 0, set()),
    'Hangout': (1, 'I', 0, 0, set()),
    'Land': (0, 'L', 0, 0, set()),
}
OPP_DECKS = {
    '赤単果敢': dict(Burst=4, Emberheart=4, Kumano=4, MRage=4, Battlemage=4, Swiftspear=4, RRage=4,
                 Slickshot=4, SoulScar=4, Dispute=4, Land=20),
    'イゼット果敢': dict(Flow=4, Burst=4, Talent=4, Dispute=4, Sleight=4, RRage=4, Emberheart=2, SoulScar=4,
                   Boomerang=3, Swiftspear=4, Battlemage=2, Land=20, MRage=1),
}
# ハンデスで抜く優先順
OPP_VALUE = ['Slickshot', 'Emberheart', 'Talent', 'MRage', 'Swiftspear', 'Burst', 'Nemesis', 'Kumano',
             'SoulScar', 'Battlemage', 'Hangout', 'Flow', 'Dispute', 'Sleight', 'RRage', 'Boomerang']

# ---------------- 自分のデッキ ----------------
CORE = dict(SF=4, SSM=4, RW=4, AT=2, CO=1, BR=2, GZ=4, GR=4, MA=4, L=24)  # 53枚
INTERACTION = {
    # name: (cost, kind, condition)
    'PUSH': (1, 'kill', lambda c: c['cost'] <= 2),
    'TCRIT': (2, 'kill', lambda c: True),            # 絶望的批評（Terminal Criticism）。青か赤のクリーチャーなら破壊できる
    'BT': (2, 'kill', lambda c: True),               # 苦々しい勝利
    'HEX': (1, 'kill', lambda c: c['cost'] <= 2),     # 報いの呪詛（Requiting Hex）
    'GASP': (2, 'kill', lambda c: c['t'] <= 3),       # 最後の喘ぎ（Last Gasp）。相手の果敢より前に撃つのでタフネスで判定
    'THX': (2, 'charm', lambda c: c['t'] <= 2),       # セオリクスの魔除け（Theorix Charm）。-2/-2、対象がなければ切削3・1ドロー
    'TS': (1, 'discard', None),                      # 思考囲い
    'BAT': (2, 'bat', None),                          # 大洞窟のコウモリ
}
DISCARD_FIRST = ['BR', 'ZE', 'CO', 'AT', 'RW']


class Opp:
    def __init__(self, deck, rng, on_play_me):
        self.lib = [k for k, v in deck.items() for _ in range(v)]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.rng = rng
        self.lands = 0
        self.board = []  # dict(name,p,t,flags,sick,role,cost)
        self.saga = None  # lore counter of Kumano
        self.dmg = 0
        self.first = not on_play_me  # 相手が先手なら最初のドローなし
        self.exiled_by_bat = None

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def creatures(self):
        return self.board

    def threat(self, c):
        return c['p'] + c['role'] * 1 + (2 if 'prowess' in c['flags'] or 'slick' in c['flags'] else 0)


def opp_turn(o, me, kill_window):
    """相手の1ターン。kill_window(o) は相手がクリーチャーを唱えた後、戦闘前にこちらが除去を撃つ場面。"""
    if o.first:
        o.first = False
    else:
        o.draw()
    for c in o.board:
        c['sick'] = False
    # 熊野の章
    if o.saga is not None:
        o.saga += 1
        if o.saga == 3:
            o.board.append(dict(name='KumanoC', p=2, t=2, flags={'haste'}, sick=False, role=0, cost=1, kumano=True))
            o.saga = None
    if 'Land' in o.hand:
        o.hand.remove('Land'); o.lands += 1
    mana = o.lands
    spells = 0
    pump = {}

    def cast_noncreature():
        nonlocal spells
        spells += 1
        for c in o.board:
            if 'prowess' in c['flags']:
                pump[id(c)] = pump.get(id(c), 0) + 1
            if 'slick' in c['flags']:
                pump[id(c)] = pump.get(id(c), 0) + 2

    # 熊野を1マナで
    if 'Kumano' in o.hand and mana >= 1 and o.saga is None and not any(c.get('kumano') for c in o.board):
        o.hand.remove('Kumano'); mana -= 1; o.dmg += 1; o.saga = 1; cast_noncreature()
    # クリーチャー
    for name in ['Emberheart', 'Slickshot', 'Swiftspear', 'SoulScar', 'Battlemage', 'Nemesis']:
        while name in o.hand and mana >= OPP_CARDS[name][0]:
            cost, _, p, t, fl = OPP_CARDS[name]
            o.hand.remove(name); mana -= cost
            o.board.append(dict(name=name, p=p, t=t, flags=set(fl), sick='haste' not in fl, role=0, cost=cost,
                                prepared='prepared' in fl))
    # こちらの除去の場面
    kill_window(o)
    # こちらのコウモリを除去
    if me.bat_on_board:
        for name in ['Burst', 'RRage', 'Boomerang']:
            if name in o.hand and mana >= 1 and (name != 'RRage' or o.board):
                o.hand.remove(name); mana -= 1; cast_noncreature(); me.bat_dies(o)
                break
    # 非クリーチャー呪文
    if 'Talent' in o.hand and mana >= 1:
        o.hand.remove('Talent'); mana -= 1; cast_noncreature()
        o.board.append(dict(name='Otter', p=1, t=1, flags={'prowess'}, sick=True, role=0, cost=0))
    attackers = [c for c in o.board if not c['sick']]
    progress = True
    while progress and mana > 0:
        progress = False
        for c in o.board:
            if c.get('prepared') and mana >= 1:
                c['prepared'] = False; mana -= 1; cast_noncreature(); progress = True
        for name in ['Sleight', 'Dispute', 'Flow', 'Hangout']:
            if name in o.hand and mana >= OPP_CARDS[name][0] and (name != 'Dispute' or o.board):
                o.hand.remove(name); mana -= OPP_CARDS[name][0]; cast_noncreature()
                if name == 'Flow':
                    o.draw(1)
                elif name == 'Sleight':
                    o.draw(1)
                # 学問的論争の学習（1枚捨てて1枚引く）と、Improvised Actの手札入れ替えは、枚数が変わらないので無視する
                elif name == 'Hangout':
                    for c in attackers[:2]:
                        pump[id(c)] = pump.get(id(c), 0) + 1
                progress = True
                break
        if progress:
            continue
        if 'MRage' in o.hand and mana >= 1 and attackers:
            o.hand.remove('MRage'); mana -= 1; cast_noncreature()
            best = max(attackers, key=lambda c: c['p'])
            pump[id(best)] = pump.get(id(best), 0) + 2
            best['role'] = 1
            progress = True; continue
        if 'Burst' in o.hand and mana >= 1:
            o.hand.remove('Burst')
            if mana >= 5:
                mana -= 5; o.dmg += 4
            else:
                mana -= 1; o.dmg += 2
            cast_noncreature(); progress = True; continue
    # 攻撃
    for c in o.board:
        if not c['sick']:
            o.dmg += max(0, c['p'] + c['role'] + pump.get(id(c), 0))
    if me.bat_on_board:
        o.dmg -= 1  # コウモリの攻撃の絆魂（概算）


class Me:
    def __init__(self, deck, rng, use_inter, policy, opp):
        self.lib = deck[:]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.yard = []
        self.lands = 0
        self.rng = rng
        self.use = use_inter
        self.policy = policy
        self.opp = opp
        self.reserved = 0
        self.goal = None
        self.bat_on_board = False
        self.casts = 0

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def need_land(self):
        return self.lands + self.hand.count('L') < 4

    def discard_one(self):
        h = self.hand
        for c in DISCARD_FIRST:
            if c in h:
                h.remove(c); self.yard.append(c); return
        if h.count('L') >= 2 and not self.need_land():
            h.remove('L'); self.yard.append('L'); return
        for c in ['SF', 'SSM']:
            if h.count(c) >= 2:
                h.remove(c); self.yard.append(c); return
        for c in list(INTERACTION) + ['DMM', 'SWS', 'DG', 'GZ', 'GR', 'MA', 'L', 'SF', 'SSM']:
            if c in h:
                h.remove(c); self.yard.append(c); return

    def check_goal(self, mana, t):
        if self.goal:
            return
        h, y = self.hand, self.yard
        ssm = 'SSM' in h and mana >= 4 and any(x in y for x in ['BR', 'AT', 'CO', 'ZE'])
        sf = 'SF' in h and mana >= 2 + max(0, 4 - len(y)) and 'RW' in y
        if ssm or sf:
            self.goal = t

    def bat_dies(self, o):
        self.bat_on_board = False
        if o.exiled_by_bat:
            o.hand.append(o.exiled_by_bat); o.exiled_by_bat = None
        self.yard.append('BAT')

    # 除去: 相手のターンの戦闘前（dev）か、自分のターン（int）に撃つ
    def try_kill(self, o, mana):
        if not o.board:
            return 0
        targets = sorted(o.board, key=lambda c: -o.threat(c))
        for name in ['HEX', 'PUSH', 'TCRIT', 'GASP', 'THX', 'BT']:
            cost, kind, cond = INTERACTION[name]
            if name in self.hand and mana >= cost:
                tgt = next((c for c in targets if cond(c)), None)
                if tgt is None:
                    continue
                self.hand.remove(name); self.yard.append(name); self.casts += 1
                o.board.remove(tgt)
                if name == 'BT':
                    if any(x in self.hand for x in ['BR', 'ZE', 'CO', 'AT', 'RW']):
                        self.discard_one()
                    else:
                        o.dmg += 3
                return cost
        return 0

    def my_turn(self, t, on_play):
        if t > 1 or not on_play:
            self.draw()
        if 'L' in self.hand:
            self.hand.remove('L'); self.lands += 1
        mana = self.lands
        self.check_goal(mana, t)
        o = self.opp
        if self.use:
            # ハンデスとコウモリは2ターン目までに撃つ
            if 'TS' in self.hand and mana >= 1 and t <= 2 and o.hand:
                self.hand.remove('TS'); self.yard.append('TS'); mana -= 1; o.dmg += 2; self.casts += 1
                best = next((x for x in OPP_VALUE if x in o.hand), None)
                if best:
                    o.hand.remove(best)
            if 'BAT' in self.hand and mana >= 2 and t <= 3 and not self.bat_on_board:
                self.hand.remove('BAT'); mana -= 2; self.bat_on_board = True; self.casts += 1
                best = next((x for x in OPP_VALUE if x in o.hand), None)
                if best:
                    o.hand.remove(best); o.exiled_by_bat = best
            if self.policy == 'int':
                while True:
                    used = self.try_kill(o, mana)
                    if not used:
                        break
                    mana -= used
        # 展開
        progress = True
        while progress and not self.goal:
            progress = False
            h, y, lib = self.hand, self.yard, self.lib
            if 'DG' in h and mana >= 3 and (('BR' not in y and 'BR' in lib) or ('SSM' not in h and 'SSM' in lib and any(x in y for x in ['BR', 'AT', 'CO', 'ZE']))):
                # ダイナの導き: 運び手が墓地に無ければ墓地へ、あればスーペリア・スパイダーマンを手札へ
                h.remove('DG'); y.append('DG'); mana -= 3
                if 'BR' not in y and 'BR' in lib:
                    lib.remove('BR'); y.append('BR')
                else:
                    lib.remove('SSM'); h.append('SSM')
                self.rng.shuffle(lib); progress = True
            elif 'MA' in h and mana >= 2:
                h.remove('MA'); mana -= 2
                y += lib[:2]; del lib[:2]; self.draw(2); self.discard_one(); self.discard_one(); progress = True
            elif 'GR' in h and mana >= 2:
                h.remove('GR'); y.append('GR'); mana -= 2
                rev = lib[:5]; del lib[:5]
                wants = (['SSM'] if 'SSM' not in h else []) + (['SF'] if 'SF' not in h else []) \
                    + (['L'] if self.need_land() else []) + ['SSM', 'SF']
                take = next((c for c in wants if c in rev), None)
                if take:
                    rev.remove(take); h.append(take)
                y += rev; progress = True
            elif 'SWS' in h and mana >= 2:
                # 救う価値あり（Something Worth Saving）: 切削4、パーマネント・カードを1枚手札へ
                h.remove('SWS'); y.append('SWS'); mana -= 2
                rev = lib[:4]; del lib[:4]
                wants = (['SSM'] if 'SSM' not in h else []) + (['SF'] if 'SF' not in h else []) \
                    + (['L'] if self.need_land() else [])
                take = next((c for c in wants if c in rev), None)
                if take:
                    rev.remove(take); h.append(take)
                y += rev; progress = True
            elif 'DMM' in h and mana >= 1:
                # 暗黒物質の操り手（Dark Matter Manipulator）: 切削3
                h.remove('DMM'); mana -= 1; y += lib[:3]; del lib[:3]; progress = True
            elif 'GZ' in h and mana >= 1:
                h.remove('GZ'); y.append('GZ'); mana -= 1
                top = lib[:3]; del lib[:3]; keep = []
                for c in top:
                    if (c == 'SSM' and 'SSM' not in h and 'SSM' not in keep) or \
                       (c == 'SF' and 'SF' not in h and 'SF' not in keep) or \
                       (c == 'L' and self.need_land() and keep.count('L') < 1):
                        keep.append(c)
                    else:
                        y.append(c)
                lib[:0] = keep; progress = True
            elif 'RW' in h and mana >= 1:
                h.remove('RW'); y.append('RW'); mana -= 1; self.draw(); progress = True
            elif self.use and 'THX' in h and mana >= 2 and not self.opp.board:
                # 相手のクリーチャーがいなければ、セオリクスの魔除けを切削3・1ドローで使う
                h.remove('THX'); y.append('THX'); mana -= 2
                y += lib[:3]; del lib[:3]; self.draw(1); progress = True
            self.check_goal(mana, t)
        self.check_goal(mana, t)
        self.reserved = mana if self.use else 0

    def kill_window(self, o):
        if self.use and self.reserved > 0:
            while True:
                used = self.try_kill(o, self.reserved)
                if not used:
                    break
                self.reserved -= used


def game(my_deck, opp_deck, seed, use, policy, on_play):
    rng = random.Random(seed)
    o = Opp(opp_deck, random.Random(seed * 7 + 1), on_play)
    me = Me(my_deck, rng, use, policy, o)
    kill = None
    for t in range(1, MAXT + 1):
        if on_play:
            me.my_turn(t, True)
            opp_turn(o, me, me.kill_window)
        else:
            opp_turn(o, me, me.kill_window)
            me.my_turn(t, False)
        if kill is None and o.dmg >= START_LIFE:
            kill = t
    return (kill or MAXT + 1), (me.goal or MAXT + 1), me.casts


def mk(extra, core=None):
    d = dict(core or CORE)
    for k, v in extra.items():
        d[k] = d.get(k, 0) + v
    deck = [k for k, v in d.items() for _ in range(v)]
    assert len(deck) == 60, len(deck)
    return deck


PACKAGES = {
    '苦々しい勝利4＋致命的な一押し3（提案）': dict(BT=4, PUSH=3),
    '苦々しい勝利4＋絶望的批評3': dict(BT=4, TCRIT=3),
    '苦々しい勝利4＋報いの呪詛3': dict(BT=4, HEX=3),
    '苦々しい勝利4＋最後の喘ぎ3': dict(BT=4, GASP=3),
    '苦々しい勝利4＋セオリクスの魔除け3': dict(BT=4, THX=3),
    '苦々しい勝利4＋思考囲い3': dict(BT=4, TS=3),
    '苦々しい勝利4＋大洞窟のコウモリ3': dict(BT=4, BAT=3),
    '致命的な一押し4＋報いの呪詛3': dict(PUSH=4, HEX=3),
    '妨害なし（暗黒物質の操り手4＋救う価値あり3）': dict(DMM=4, SWS=3),
}


def run():
    print('列: 相手キルターン平均 なし→あり / 自分の勝ち筋成立ターン平均 なし→あり / 妨害を撃ったゲームの割合 /'
          ' 撃ったゲームでの平均ΔK・平均ΔG / 撃ったゲームでΔK>ΔGの割合 / 相手のキルより先に勝ち筋が成立した割合 なし→あり')
    for opp_name, opp_deck in OPP_DECKS.items():
        for on_play in (True, False):
            print(f'\n== 相手: {opp_name} / 自分が{"先手" if on_play else "後手"}')
            for pname, pkg in PACKAGES.items():
                deck = mk(pkg)
                for policy in (('dev', 'int') if any(k in INTERACTION for k in pkg) else ('dev',)):
                    K0, G0, K1, G1, r0, r1 = [], [], [], [], 0, 0
                    dks, dgs, gt = [], [], 0
                    for s in range(N):
                        k0, g0, _ = game(deck, opp_deck, s, False, policy, on_play)
                        k1, g1, n = game(deck, opp_deck, s, True, policy, on_play)
                        K0.append(k0); G0.append(g0); K1.append(k1); G1.append(g1)
                        if n:
                            dks.append(k1 - k0); dgs.append(g1 - g0); gt += (k1 - k0) > (g1 - g0)
                        r0 += (g0 <= k0) if on_play else (g0 < k0)
                        r1 += (g1 <= k1) if on_play else (g1 < k1)
                    c = len(dks)
                    cond = (f'ΔK {mean(dks):+.2f} ΔG {mean(dgs):+.2f} ΔK>ΔG {100*gt/c:.0f}%') if c else '-'
                    print(f'  {pname} [{policy}]: K {mean(K0):.2f}→{mean(K1):.2f} / G {mean(G0):.2f}→{mean(G1):.2f} / '
                          f'撃った {100*c/N:.0f}% / {cond} / 間に合う {100*r0/N:.0f}%→{100*r1/N:.0f}%')


if __name__ == '__main__':
    run()

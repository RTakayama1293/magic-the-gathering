#!/usr/bin/env python3
"""魂剥ぎV8の妨害が、アブザン脂牙とラクドス異形化の理想ムーブのキルターンを、
自分が妨害に使ったターン以上に遅らせられるかを計算する。

比べ方は tools/v8_interaction_sim.py と同じ（共通乱数法）。同じシャッフルで、妨害を使わない回と使う回を回し、
1ゲームごとに相手のキルターンの遅れ（ΔK）と、自分の勝ち筋が成立するターンの遅れ（ΔG）を比べる。

相手の理想ムーブ（MTGGoldfishの平均リスト、2026-11-01取得）:
  アブザン脂牙: 象徴学の教授・救う価値あり・並外れた語り部・轟雷のブルードワゴンのサイクリングで、機体を墓地に置く。
    大牙勢団の総長、脂牙を戦闘前に唱え、戦闘の開始時に墓地の機体を戻して攻撃する。
    パルヘリオンⅡは攻撃すると4/4飛行の天使2体を攻撃状態で出す。機体は終了ステップに手札に戻る
  ラクドス異形化: 検体探しのトークン、鏡割りの寓話のゴブリンを対象に異形化を唱え、ライブラリーの大型クリーチャーを出す。
    鏡割りの寓話の2章・検体探しの学習・稲妻の斧のコストで大型クリーチャーを捨て、ゾンビ化で戻す
    大型クリーチャーは、恐怖を喰うもの、ヴァルガヴォス（9/9飛行絆魂）、偉大なる統一者、アトラクサ（7/7飛行絆魂）、
    召喚：バハムート（9/9飛行）、トラブルメーカー、ラフとマイキー（7/7トランプル速攻）
単純化:
- こちらはブロックしない。相手もこちらのクリーチャーや勝ち筋に干渉しない（思考囲いだけは撃つ）
- 色・タップインは無視する。こちらのライフは18から始める
- ヴァルガヴォスが戦場にある間は、こちらの墓地に行くカードが追放される（テキスト）。この間、墓地は増えない

使い方:
    python3 tools/v8_unfair_sim.py
"""
import random
from statistics import mean

N = 4000
MAXT = 9
START_LIFE = 18


# ---------------- 自分 ----------------
class Me:
    def __init__(self, deck, rng):
        self.lib = deck[:]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.yard = []
        self.lands = 0
        self.rng = rng
        self.goal = None
        self.casts = 0
        self.reserve = 0
        self.blocked = False  # ヴァルガヴォスで墓地が使えない

    def to_yard(self, c):
        if not self.blocked:
            self.yard.append(c)

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def need_land(self):
        return self.lands + self.hand.count('L') < 4

    def discard_one(self):
        h = self.hand
        for c in ['BR', 'SA', 'AT', 'RW']:
            if c in h:
                h.remove(c); self.to_yard(c); return
        if h.count('L') >= 2 and not self.need_land():
            h.remove('L'); self.to_yard('L'); return
        for c in ['SF', 'SSM']:
            if h.count(c) >= 2:
                h.remove(c); self.to_yard(c); return
        for c in ['PU', 'GZ', 'WI', 'DG', 'GR', 'MA', 'TS', 'GB', 'BE', 'LA', 'TR', 'BT', 'L', 'SF', 'SSM']:
            if c in h:
                h.remove(c); self.to_yard(c); return

    def check_goal(self, mana, t):
        if self.goal:
            return
        h, y = self.hand, self.yard
        ssm = 'SSM' in h and mana >= 4 and any(x in y for x in ['BR', 'AT', 'SA'])
        sf = 'SF' in h and mana >= 2 + max(0, 4 - len(y)) and 'RW' in y
        if ssm or sf:
            self.goal = t

    def develop(self, mana, t):
        h, lib = self.hand, self.lib
        progress = True
        while progress and not self.goal:
            progress = False
            if 'DG' in h and mana >= 3 and 'BR' not in self.yard and 'BR' in lib and not self.blocked:
                h.remove('DG'); self.to_yard('DG'); mana -= 3
                lib.remove('BR'); self.to_yard('BR'); self.rng.shuffle(lib); progress = True
            elif 'MA' in h and mana >= 2:
                h.remove('MA'); mana -= 2
                for c in lib[:2]:
                    self.to_yard(c)
                del lib[:2]; self.draw(2); self.discard_one(); self.discard_one(); progress = True
            elif 'GR' in h and mana >= 2:
                h.remove('GR'); self.to_yard('GR'); mana -= 2
                rev = lib[:5]; del lib[:5]
                wants = (['SSM'] if 'SSM' not in h else []) + (['SF'] if 'SF' not in h else []) \
                    + (['L'] if self.need_land() else []) + ['SSM', 'SF']
                take = next((c for c in wants if c in rev), None)
                if take:
                    rev.remove(take); h.append(take)
                for c in rev:
                    self.to_yard(c)
                progress = True
            elif 'WI' in h and mana >= 2:
                h.remove('WI'); self.to_yard('WI'); mana -= 2; self.draw(2); self.discard_one(); progress = True
            elif 'GZ' in h and mana >= 1:
                h.remove('GZ'); self.to_yard('GZ'); mana -= 1
                top = lib[:3]; del lib[:3]; keep = []
                for c in top:
                    if (c == 'SSM' and 'SSM' not in h) or (c == 'SF' and 'SF' not in h) or (c == 'L' and self.need_land() and 'L' not in keep):
                        keep.append(c)
                    else:
                        self.to_yard(c)
                lib[:0] = keep; progress = True
            elif 'RW' in h and mana >= 1:
                h.remove('RW'); self.to_yard('RW'); mana -= 1; self.draw(); progress = True
            self.check_goal(mana, t)
        return mana


# ---------------- アブザン脂牙 ----------------
GREASEFANG = dict(Grease=4, Parhelion=4, Brood=3, Chariot=4, Professor=4, Speaker=4, SWS=3, TS=4, X=7, L=23)


class Grease:
    def __init__(self, rng, on_play_me):
        self.lib = [k for k, v in GREASEFANG.items() for _ in range(v)]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.yard = []
        self.lands = 0
        self.dmg = 0
        self.rng = rng
        self.first = not on_play_me
        self.grease_on = False
        self.angels = 0
        self.cats = 0
        self.chariot = False

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def vehicles_in_yard(self):
        return [x for x in self.yard if x in ('Parhelion', 'Brood')]

    def turn(self, me, t, use):
        if self.first:
            self.first = False
        else:
            self.draw()
        if 'L' in self.hand:
            self.hand.remove('L'); self.lands += 1
        mana = self.lands
        h = self.hand
        if 'TS' in h and mana >= 1 and t <= 2:
            h.remove('TS'); mana -= 1
            for want in ['BT', 'TS', 'GB', 'BE', 'SSM', 'SF', 'DG']:
                if want in me.hand:
                    me.hand.remove(want); me.to_yard(want); break
        # 脂牙を唱える
        if not self.grease_on and 'Grease' in h and mana >= 3 and self.vehicles_in_yard():
            h.remove('Grease'); mana -= 3; self.grease_on = True
            # こちらの応答: 苦々しい勝利を構えていれば、戦闘前に破壊する
            if use and 'BT' in me.hand and me.reserve >= 2:
                me.hand.remove('BT'); me.discard_one(); me.reserve -= 2; me.casts += 1
                self.grease_on = False; self.yard.append('Grease')
        # 機体を墓地に置く
        progress = True
        while progress:
            progress = False
            veh_in_hand = [x for x in h if x in ('Parhelion', 'Brood')]
            if 'Brood' in h and mana >= 2 and not self.vehicles_in_yard():
                h.remove('Brood'); self.yard.append('Brood'); mana -= 2; self.draw(); progress = True
            elif 'Professor' in h and mana >= 2:
                h.remove('Professor'); mana -= 2
                if veh_in_hand:
                    h.remove(veh_in_hand[0]); self.yard.append(veh_in_hand[0]); self.draw()
                progress = True
            elif 'SWS' in h and mana >= 2:
                h.remove('SWS'); mana -= 2
                rev = self.lib[:4]; del self.lib[:4]
                take = 'Grease' if 'Grease' in rev and 'Grease' not in h else None
                if take:
                    rev.remove(take); h.append(take)
                self.yard.extend(rev); progress = True
            elif 'Speaker' in h and mana >= 3 and (veh_in_hand or 'Grease' not in h):
                h.remove('Speaker'); mana -= 3
                if veh_in_hand:
                    h.remove(veh_in_hand[0]); self.yard.append(veh_in_hand[0])
                elif h:
                    self.yard.append(h.pop())
                if 'Grease' in self.lib and 'Grease' not in h:
                    self.lib.remove('Grease'); h.append('Grease')
                progress = True
            elif not self.grease_on and 'Grease' in h and mana >= 3 and self.vehicles_in_yard():
                h.remove('Grease'); mana -= 3; self.grease_on = True
                if use and 'BT' in me.hand and me.reserve >= 2:
                    me.hand.remove('BT'); me.discard_one(); me.reserve -= 2; me.casts += 1
                    self.grease_on = False; self.yard.append('Grease')
                progress = True
            elif 'Chariot' in h and mana >= 4 and not self.chariot:
                h.remove('Chariot'); mana -= 4; self.chariot = True; self.cats += 2; progress = True
        # 戦闘
        dmg = 0
        if self.grease_on:
            v = self.vehicles_in_yard()
            if 'Parhelion' in v:
                self.yard.remove('Parhelion'); h.append('Parhelion')  # 終了ステップに手札へ
                dmg += 5 + 8; self.angels += 2
            elif 'Brood' in v:
                self.yard.remove('Brood'); h.append('Brood'); dmg += 6
        dmg += 4 * max(0, self.angels - (2 if self.grease_on and dmg >= 13 else 0))
        if self.chariot and self.cats >= 2:
            dmg += 4
        self.dmg += dmg


# ---------------- ラクドス異形化 ----------------
TRANSMOG = dict(Fable=4, Hunt=4, Trans=4, Zomb=4, TS=4, Axe=2, Big=4, X=11, L=23)
BIG = [('Valg', 9, True), ('Atraxa', 7, False), ('Bahamut', 9, False), ('RM', 7, False)]


class Trans:
    def __init__(self, rng, on_play_me):
        self.lib = [k for k, v in TRANSMOG.items() for _ in range(v)]
        rng.shuffle(self.lib)
        self.hand, self.lib = self.lib[:7], self.lib[7:]
        self.yard = []
        self.lands = 0
        self.dmg = 0
        self.rng = rng
        self.first = not on_play_me
        self.tokens = []  # パワー
        self.bigs = []    # (名前, パワー, ヴァルガヴォスか, 召喚酔い)
        self.fable = None

    def draw(self, n=1):
        for _ in range(n):
            if self.lib:
                self.hand.append(self.lib.pop(0))

    def big(self):
        return self.rng.choice(BIG)

    def turn(self, me, t, use):
        if self.first:
            self.first = False
        else:
            self.draw()
        if 'L' in self.hand:
            self.hand.remove('L'); self.lands += 1
        mana = self.lands
        h = self.hand
        if self.fable is not None:
            self.fable += 1
            if self.fable == 2 and 'Big' in h:
                h.remove('Big'); self.yard.append('Big'); self.draw()
            if self.fable == 3:
                self.fable = None
        if 'TS' in h and mana >= 1 and t <= 2:
            h.remove('TS'); mana -= 1
            for want in ['TS', 'GB', 'BT', 'PU', 'SSM', 'SF', 'DG']:
                if want in me.hand:
                    me.hand.remove(want); me.to_yard(want); break
        progress = True
        while progress:
            progress = False
            if 'Zomb' in h and mana >= 4 and 'Big' in self.yard:
                h.remove('Zomb'); mana -= 4; self.yard.remove('Big')
                n, p, v = self.big(); self.bigs.append([n, p, v, n != 'RM']); progress = True
            elif 'Trans' in h and mana >= 4 and self.tokens:
                h.remove('Trans'); mana -= 4; self.tokens.pop()
                n, p, v = self.big(); self.bigs.append([n, p, v, n != 'RM']); progress = True
            elif 'Fable' in h and mana >= 3 and self.fable is None:
                h.remove('Fable'); mana -= 3; self.fable = 1; self.tokens.append(2); progress = True
            elif 'Hunt' in h and mana >= 2:
                h.remove('Hunt'); mana -= 2; self.tokens.append(1)
                if 'Big' in h:
                    h.remove('Big'); self.yard.append('Big'); self.draw()
                progress = True
            elif 'Axe' in h and 'Big' in h and mana >= 1 and me_has_creature(me):
                h.remove('Axe'); h.remove('Big'); self.yard.append('Big'); mana -= 1; progress = True
        me.blocked = any(b[2] for b in self.bigs)
        dmg = sum(self.tokens)
        for b in self.bigs:
            if not b[3]:
                dmg += b[1]
            b[3] = False
        self.dmg += dmg


def me_has_creature(me):
    return False  # 単純化: こちらは勝ち筋が成立するまでクリーチャーを出さない


# ---------------- こちらの妨害 ----------------
def my_turn(me, opp, kind, t, on_play, use):
    if t > 1 or not on_play:
        me.draw()
    if 'L' in me.hand:
        me.hand.remove('L'); me.lands += 1
    mana = me.lands
    me.check_goal(mana, t)
    h = me.hand
    if use and not me.goal:
        # ハンデス
        if 'TS' in h and mana >= 1 and t <= 3:
            want = ['Grease', 'Parhelion', 'Speaker'] if kind == 'grease' else ['Trans', 'Zomb', 'Fable', 'Hunt']
            tgt = next((x for x in want if x in opp.hand), None)
            if tgt:
                h.remove('TS'); me.to_yard('TS'); mana -= 1; opp.dmg += 2; opp.hand.remove(tgt); me.casts += 1
        if 'GB' in h and mana >= 3:
            want = ['Grease', 'Parhelion', 'Brood'] if kind == 'grease' else ['Trans', 'Zomb', 'Big']
            if any(x in opp.hand for x in want) or (kind == 'grease' and opp.vehicles_in_yard()) or (kind == 'trans' and 'Big' in opp.yard):
                h.remove('GB'); me.to_yard('GB'); mana -= 3; me.casts += 1
                for _ in range(2):
                    tgt = next((x for x in want if x in opp.hand), None)
                    if tgt:
                        opp.hand.remove(tgt)
                opp.yard = []
        # 相手の墓地への対策
        for card, cost in (('LA', 1), ('BE', 2), ('TR', 3)):
            if card in h and mana >= cost:
                has = (kind == 'grease' and opp.vehicles_in_yard()) or (kind == 'trans' and 'Big' in opp.yard)
                if not has:
                    continue
                h.remove(card); mana -= cost; me.casts += 1
                if card in ('LA', 'BE'):
                    opp.yard = []
                    if card == 'BE':
                        if kind == 'grease' and opp.grease_on:
                            opp.grease_on = False
                        elif kind == 'trans':
                            if opp.tokens:
                                opp.tokens.pop()
                            elif opp.bigs:
                                opp.bigs.pop(0)
                else:
                    tgt = next((x for x in ['Parhelion', 'Brood', 'Big'] if x in opp.yard), None)
                    if tgt:
                        opp.yard.remove(tgt)
        # 除去（異形化: トークンを除去して異形化の対象を無くす。大型クリーチャーを苦々しい勝利で除去する）
        if kind == 'trans':
            while True:
                if opp.bigs and 'BT' in h and mana >= 2:
                    nonward = [b for b in opp.bigs if not b[2]]
                    if nonward:
                        h.remove('BT'); me.discard_one(); mana -= 2; opp.bigs.remove(nonward[0]); me.casts += 1; continue
                if opp.tokens and 'Trans' in opp.hand:
                    if 'PU' in h and mana >= 1:
                        h.remove('PU'); me.to_yard('PU'); mana -= 1; opp.tokens.pop(); me.casts += 1; continue
                break
    mana = me.develop(mana, t)
    # 脂牙対策: 苦々しい勝利を構える
    me.reserve = 0
    if use and kind == 'grease' and 'BT' in h:
        me.reserve = mana
    me.blocked = kind == 'trans' and any(b[2] for b in opp.bigs)


def game(my_deck, kind, seed, use, on_play):
    me = Me(my_deck, random.Random(seed))
    opp = (Grease if kind == 'grease' else Trans)(random.Random(seed * 7 + 3), on_play)
    kill = None
    for t in range(1, MAXT + 1):
        if on_play:
            my_turn(me, opp, kind, t, on_play, use)
            opp.turn(me, t, use)
        else:
            opp.turn(me, t, use)
            my_turn(me, opp, kind, t, on_play, use)
        if kill is None and opp.dmg >= START_LIFE:
            kill = t
    return kill or MAXT + 1, me.goal or MAXT + 1, me.casts


MAIN = dict(SF=4, SSM=4, RW=4, SA=3, BR=2, AT=2, GR=4, MA=4, WI=2, DG=2, GZ=1, BT=3, PU=3, L=22)


def side(ins, outs):
    d = dict(MAIN)
    for k, v in outs.items():
        d[k] -= v
    for k, v in ins.items():
        d[k] = d.get(k, 0) + v
    out = [k for k, v in d.items() for _ in range(v)]
    assert len(out) == 60, len(out)
    return out


PACKAGES = {
    'メインのみ（苦々しい勝利3・致命的な一押し3）': side({}, {}),
    '思考囲い3（一押し-3）': side(dict(TS=3), dict(PU=3)),
    '真っ白2（凝視-1、導き-1）': side(dict(GB=2), dict(GZ=1, DG=1)),
    '戦略的裏切り2（凝視-1、導き-1）': side(dict(BE=2), dict(GZ=1, DG=1)),
    '魂標ランタン1（凝視-1）': side(dict(LA=1), dict(GZ=1)),
    '墓地の侵入者2（凝視-1、導き-1）': side(dict(TR=2), dict(GZ=1, DG=1)),
    '第8版SB: 思考囲い3・真っ白2・戦略的裏切り2・ランタン1（一押し3・導き2・凝視1・運び手2）': side(dict(TS=3, GB=2, BE=2, LA=1), dict(PU=3, DG=2, GZ=1, BR=2)),
}

if __name__ == '__main__':
    print('列: 相手キルターン平均 なし→あり / 自分の勝ち筋成立ターン平均 なし→あり / 撃ったゲームの割合 / 撃ったゲームでΔK>ΔGの割合 / 相手のキルより先に成立 なし→あり')
    for kind, label in (('grease', 'アブザン脂牙'), ('trans', 'ラクドス異形化')):
        for on_play in (True, False):
            print(f"\n== {label} / 自分が{'先手' if on_play else '後手'}")
            for name, deck in PACKAGES.items():
                K0, G0, K1, G1, r0, r1, dk, dg, gt = [], [], [], [], 0, 0, [], [], 0
                for s in range(N):
                    k0, g0, _ = game(deck, kind, s, False, on_play)
                    k1, g1, n = game(deck, kind, s, True, on_play)
                    K0.append(k0); G0.append(g0); K1.append(k1); G1.append(g1)
                    r0 += (g0 <= k0) if on_play else (g0 < k0)
                    r1 += (g1 <= k1) if on_play else (g1 < k1)
                    if n:
                        dk.append(k1 - k0); dg.append(g1 - g0); gt += (k1 - k0) > (g1 - g0)
                c = len(dk)
                print(f'  {name}: K {mean(K0):.2f}→{mean(K1):.2f} / G {mean(G0):.2f}→{mean(G1):.2f} / 撃った {100*c/N:.0f}% / '
                      f'ΔK>ΔG {100*gt/max(c,1):.0f}% / 間に合う {100*r0/N:.0f}%→{100*r1/N:.0f}%')

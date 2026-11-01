#!/usr/bin/env python3
"""魂剥ぎV8のメイン構成の候補を、3・4・5ターン目までに勝ち筋が成立する確率で比べる。

tools/soulflayer_v8_sim.py を広げ、notes/soulflayer_v8_card_pool.md の候補カードを足したもの。
前提（数字は構成どうしの比較にだけ使う）:
- マリガンしない。色・タップインは無視し、土地の枚数をマナとする。相手の妨害は無い
- 苦々しい勝利は、相手のクリーチャーがいる確率0.6で唱え、手札の墓地用クリーチャーを捨てる
- 致命的な一押しなど、勝ち筋に関わらないカードは何もしないカードとして数える
勝ち筋の判定:
- SSM_good: スーペリア・スパイダーマンで、墓地の運び手・アトラクサ・コズミック・スパイダーマン・ゼタルパのどれかをコピーできる
- SSM_BR: そのうち運び手をコピーできる
- SF_hex: 呪禁の提供役（縞カワヘビ・夜帷の捕食者）を探査して魂剥ぎを唱えられる
- any: SSM_good か SF_hex

使い方:
    python3 tools/v8_build_sim.py
"""
import random


class Land(str):
    """土地のカード。文字列としては 'L' と等しく、kind に種類を持つ。
    S: 諜報ランド（タップインで諜報1） / F: ファストランド（3枚目までアンタップ） / H: ショックランド（2点払ってアンタップ）
    T: 始まりの町（3ターン目までアンタップ、色マナで1点） / C: マナの合流点（色マナで1点） / B: 基本土地などアンタップで出る土地"""
    def __new__(cls, kind='B'):
        obj = str.__new__(cls, 'L')
        obj.kind = kind
        return obj

N = 60000
OPP_CREATURE = 0.6
COPY_TARGETS = ['BR', 'AT', 'CO', 'ZE']
HEX = ['RW', 'NP']
YARD_ONLY = ['BR', 'ZE', 'CO', 'AT', 'NP', 'RW']  # 手札から捨てたいカード（左ほど優先）
BLANK = ['PU', 'X']
# 略号: L 土地 / SF 魂剥ぎ / SSM スーペリア・スパイダーマン / RW 縞カワヘビ / NP 夜帷の捕食者 / AT アトラクサ
# CO コズミック・スパイダーマン / ZE 原初の夜明け、ゼタルパ / BR 運び手 / GZ 異世界の凝視 / GR 忌まわしい回収
# SW 救う価値あり（真夜中の耕作も同じ扱い） / MA メカの天才 / TC セオリクスの魔除け（切削3・1ドローで使う）
# DG ダイナの導き / BT 苦々しい勝利 / PU 致命的な一押し / X 何もしないカード


def run(deck, play=True, seed=1, maxt=5, mull=False, stats=None):
    rng = random.Random(seed)
    keys = ['SSM_BR', 'SSM_good', 'SF_hex', 'any']
    res = {k: [0, 0, 0] for k in keys}
    for _ in range(N):
        lib = deck[:]
        rng.shuffle(lib)
        hand, lib = lib[:7], lib[7:]
        if mull:
            # ロンドン・マリガン。土地2〜5枚ならキープ。2回目（5枚）は必ずキープ
            for bottom in (1, 2):
                if 2 <= hand.count('L') <= 5:
                    break
                lib = deck[:]; rng.shuffle(lib); hand, lib = lib[:7], lib[7:]
                for _ in range(bottom):
                    c = 'L' if hand.count('L') > 3 else next((x for x in BLANK + ['BT', 'GZ', 'RW', 'L'] if x in hand), hand[0])
                    lib.append(hand.pop(hand.index(c)))
                if stats is not None:
                    stats['mull'] = stats.get('mull', 0) + 1
                if bottom == 2 or 2 <= hand.count('L') <= 5:
                    break
        yard, lands = [], 0
        life_paid = 0
        in_play = []
        got = {k: None for k in keys}

        def draw(n=1):
            for _ in range(n):
                if lib:
                    hand.append(lib.pop(0))

        def need_land():
            return lands + hand.count('L') < 4

        def discard_one():
            for c in YARD_ONLY:
                if c in hand:
                    hand.remove(c); yard.append(c); return
            if hand.count('L') >= 2 and not need_land():
                hand.remove('L'); yard.append('L'); return
            for c in ['SF', 'SSM']:
                if hand.count(c) >= 2:
                    hand.remove(c); yard.append(c); return
            for c in BLANK + ['GZ', 'BT', 'TC', 'SW', 'GR', 'DG', 'CRY', 'MA', 'L', 'SF', 'SSM']:
                if c in hand:
                    hand.remove(c); yard.append(c); return

        def check(mana, t):
            ok = {}
            ok['SSM_BR'] = 'SSM' in hand and mana >= 4 and 'BR' in yard
            ok['SSM_good'] = 'SSM' in hand and mana >= 4 and any(x in yard for x in COPY_TARGETS)
            ok['SF_hex'] = 'SF' in hand and mana >= 2 + max(0, 4 - len(yard)) and any(x in yard for x in HEX)
            ok['any'] = ok['SSM_good'] or ok['SF_hex']
            for k, v in ok.items():
                if v and got[k] is None:
                    got[k] = t

        def dig(rev, take_land=True):
            wants = (['SSM'] if 'SSM' not in hand else []) + (['SF'] if 'SF' not in hand else []) \
                + (['L'] if need_land() and take_land else []) + ['SSM', 'SF']
            take = next((c for c in wants if c in rev), None)
            if take:
                i = rev.index(take); hand.append(rev.pop(i))
            yard.extend(rev)

        for t in range(1, maxt + 1):
            if t > 1 or not play:
                draw()
            mana = lands
            land_cards = [c for c in hand if c == 'L']
            if land_cards:
                n = len(in_play)

                def untapped(c):
                    k = getattr(c, 'kind', 'B')
                    return k in 'BHC' or (k == 'F' and n <= 2) or (k == 'T' and t <= 3)
                if t == 1:
                    # 1ターン目はマナを使わないので、タップインの土地を先に置く
                    order = sorted(land_cards, key=lambda c: (untapped(c), getattr(c, 'kind', 'B') == 'H'))
                else:
                    order = sorted(land_cards, key=lambda c: (not untapped(c), getattr(c, 'kind', 'B') in 'HC'))
                c = order[0]
                del hand[next(i for i, x in enumerate(hand) if x is c)]  # 同じ 'L' でも、選んだ土地そのものを取り除く
                in_play.append(c); lands += 1
                k = getattr(c, 'kind', 'B')
                tapped_in = (k == 'S') or (k == 'F' and n > 2) or (k == 'T' and t > 3) or (k == 'H' and t == 1)
                if k == 'H' and t > 1:
                    life_paid += 2
                mana = lands - (1 if tapped_in else 0)
                if k == 'S' and lib:
                    top = lib[0]
                    keep = (top == 'SSM' and 'SSM' not in hand) or (top == 'SF' and 'SF' not in hand) or (top == 'L' and need_land())
                    if not keep:
                        yard.append(lib.pop(0))
            life_paid += sum(1 for x in in_play if getattr(x, 'kind', 'B') == 'C')
            life_paid += sum(1 for x in in_play if getattr(x, 'kind', 'B') == 'T') * 0.5
            if t >= 3:
                check(mana, t)
            progress = True
            while progress:
                progress = False
                if 'DG' in hand and mana >= 3:
                    target = None
                    if 'BR' not in yard and 'BR' in lib and ('SSM' in hand or t >= 3):
                        target, to_yard = 'BR', True
                    elif 'SSM' not in hand and 'SSM' in lib and any(x in yard for x in COPY_TARGETS):
                        target, to_yard = 'SSM', False
                    if target:
                        hand.remove('DG'); yard.append('DG'); mana -= 3
                        lib.remove(target); rng.shuffle(lib)
                        (yard if to_yard else hand).append(target); progress = True; continue
                if 'MA' in hand and mana >= 2:
                    hand.remove('MA'); mana -= 2
                    yard.extend(lib[:2]); del lib[:2]; draw(2); discard_one(); discard_one(); progress = True; continue
                if 'GR' in hand and mana >= 2:
                    hand.remove('GR'); yard.append('GR'); mana -= 2
                    rev = lib[:5]; del lib[:5]; dig(rev); progress = True; continue
                if 'CRY' in hand and mana >= 3:
                    # 歴戦の冷術士: 2枚引いて2枚捨てる（相手のクリーチャーを止める効果はこの計算では数えない）
                    hand.remove('CRY'); mana -= 3; draw(2); discard_one(); discard_one(); progress = True; continue
                if 'SW' in hand and mana >= 2:
                    hand.remove('SW'); yard.append('SW'); mana -= 2
                    rev = lib[:4]; del lib[:4]; dig(rev); progress = True; continue
                if 'TC' in hand and mana >= 2:
                    hand.remove('TC'); yard.append('TC'); mana -= 2
                    yard.extend(lib[:3]); del lib[:3]; draw(); progress = True; continue
                if 'GZ' in hand and mana >= 1:
                    hand.remove('GZ'); yard.append('GZ'); mana -= 1
                    top = lib[:3]; del lib[:3]; keep = []
                    for c in top:
                        if (c == 'SSM' and 'SSM' not in hand and 'SSM' not in keep) or \
                           (c == 'SF' and 'SF' not in hand and 'SF' not in keep) or \
                           (c == 'L' and need_land() and keep.count('L') < 1):
                            keep.append(c)
                        else:
                            yard.append(c)
                    lib[:0] = keep; progress = True; continue
                if 'RW' in hand and mana >= 1:
                    hand.remove('RW'); yard.append('RW'); mana -= 1; draw(); progress = True; continue
                if 'BT' in hand and mana >= 2 and any(x in hand for x in YARD_ONLY if x != 'RW') and rng.random() < OPP_CREATURE:
                    hand.remove('BT'); yard.append('BT'); mana -= 2
                    c = next(x for x in YARD_ONLY if x in hand)
                    hand.remove(c); yard.append(c); progress = True; continue
            if t >= 3:
                check(mana, t)
            if stats is not None:
                if t == 3 and lands < 3:
                    stats['screw3'] = stats.get('screw3', 0) + 1
                if t == 4 and lands < 4:
                    stats['screw4'] = stats.get('screw4', 0) + 1
                if t == maxt and lands + hand.count('L') >= maxt + 1 and len([c for c in hand if c != 'L']) <= 1:
                    stats['flood'] = stats.get('flood', 0) + 1
        if stats is not None:
            stats['life'] = stats.get('life', 0) + life_paid
            stats['never'] = stats.get('never', 0) + (got['any'] is None)
            stats['turnsum'] = stats.get('turnsum', 0) + (got['any'] or maxt + 1)
        for k in keys:
            for i, T in enumerate((3, 4, 5)):
                res[k][i] += got[k] is not None and got[k] <= T
    return {k: tuple(round(100 * x / N, 1) for x in v) for k, v in res.items()}


def mk(d, lands=None):
    """lands に {'S': 6, 'F': 7, ...} を渡すと、土地を種類つきで作る。渡さなければ d['L'] 枚の基本土地"""
    d = dict(d)
    if lands:
        assert sum(lands.values()) == d.get('L', 0), (lands, d.get('L'))
        d.pop('L')
    deck = [k for k, v in d.items() for _ in range(v) if v]
    if lands:
        deck += [Land(k) for k, v in lands.items() for _ in range(v)]
    assert len(deck) == 60, (len(deck), d)
    return deck


A = dict(SF=4, SSM=4, RW=4, AT=2, CO=1, BR=2, GZ=4, GR=4, MA=4, BT=4, PU=3, L=24)


def var(**kw):
    d = dict(A)
    for k, v in kw.items():
        d[k] = d.get(k, 0) + v
    return d


VARIANTS = {
    'A 構築案（2026-11-01）': A,
    'B1 一押し-1 ゼタルパ+1': var(PU=-1, ZE=1),
    'B2 コズミック-1 ゼタルパ+1': var(CO=-1, ZE=1),
    'B3 縞カワヘビ-2 夜帷の捕食者+2': var(RW=-2, NP=2),
    'B4 忌まわしい回収-4 救う価値あり+4': var(GR=-4, SW=4),
    'B5 凝視-2 ダイナの導き+2': var(GZ=-2, DG=2),
    'B6 メカの天才-2 ダイナの導き+2': var(MA=-2, DG=2),
    'B7 凝視-2 セオリクスの魔除け+2': var(GZ=-2, TC=2),
    'B8 一押し-3 セオリクスの魔除け+3': var(PU=-3, TC=3),
    'B9 運び手-1 ダイナの導き+1': var(BR=-1, DG=1),
    'B10 苦々しい勝利-2 ダイナの導き+2': var(BT=-2, DG=2),
}

if __name__ == '__main__':
    print('値は (3ターン目まで, 4ターン目まで, 5ターン目まで) に成立した割合%。N =', N)
    for play in (True, False):
        print('\n先手' if play else '\n後手')
        for name, d in VARIANTS.items():
            r = run(mk(d), play=play)
            print(f"  {name}: any {r['any']} / SSM_BR {r['SSM_BR']} / SSM_good {r['SSM_good']} / SF_hex {r['SF_hex']}")

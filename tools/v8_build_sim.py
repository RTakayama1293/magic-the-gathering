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


def run(deck, play=True, seed=1):
    rng = random.Random(seed)
    keys = ['SSM_BR', 'SSM_good', 'SF_hex', 'any']
    res = {k: [0, 0, 0] for k in keys}
    for _ in range(N):
        lib = deck[:]
        rng.shuffle(lib)
        hand, lib = lib[:7], lib[7:]
        yard, lands = [], 0
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
            for c in BLANK + ['GZ', 'BT', 'TC', 'SW', 'GR', 'DG', 'MA', 'L', 'SF', 'SSM']:
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
                rev.remove(take); hand.append(take)
            yard.extend(rev)

        for t in range(1, 6):
            if t > 1 or not play:
                draw()
            if 'L' in hand:
                hand.remove('L'); lands += 1
            mana = lands
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
        for k in keys:
            for i, T in enumerate((3, 4, 5)):
                res[k][i] += got[k] is not None and got[k] <= T
    return {k: tuple(round(100 * x / N, 1) for x in v) for k, v in res.items()}


def mk(d):
    deck = [k for k, v in d.items() for _ in range(v) if v]
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

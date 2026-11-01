#!/usr/bin/env python3
"""魂剥ぎV8の候補リストで、3・4ターン目に勝ち筋が成立する確率をモンテカルロで見積もる。

notes/soulflayer_v8_proposal.md の3章の数字はこのスクリプトの出力。
単純化した前提（結果を読むときに必ず考える）:
- マリガンしない。初手7枚、先手は1ターン目にドローしない
- 土地は毎ターン1枚置く。色・タップインは無視し、土地の枚数をそのままマナとする
- 相手の妨害（除去、ハンデス、墓地対策）は無い
- 苦々しい勝利は、相手のクリーチャーがいる確率 OPP_CREATURE で唱えられるとし、追加コストで手札の運び手・アトラクサ・コズミック・スパイダーマンを捨てる
- 鏡割りの寓話など、モデルに入れていないカードは空白のカード（X）として数える
- 1回の実行で各構成 N 回（既定 80000）試す。乱数の種は固定なので、同じ構成なら同じ数字が出る

使い方:
    python3 tools/soulflayer_v8_sim.py          # 先手と後手の両方
"""
import random

N = 80000
OPP_CREATURE = 0.6

# カードの略号
# L 土地 / SF 魂剥ぎ / SSM スーペリア・スパイダーマン / RW 縞カワヘビ / AT アトラクサ / CO コズミック・スパイダーマン
# BR 最後の贈り物の運び手 / BAT 大洞窟のコウモリ / GZ 異世界の凝視 / GR 忌まわしい回収
# MA メカの天才 / DI 陽気な哀歌 / SU 縫い師への供給者（Stitcher's Supplier）
# BT 苦々しい勝利 / PU 致命的な一押し / X モデルに入れていないカード
DISCARD_FIRST = ['BR', 'CO', 'AT', 'RW']


def run(deck, play=True, seed=1):
    random.seed(seed)
    keys = ['SSM_BR', 'SSM_good', 'SF_hex', 'any']
    res = {k: [0, 0] for k in keys}
    for _ in range(N):
        lib = deck[:]
        random.shuffle(lib)
        hand, lib = lib[:7], lib[7:]
        yard, lands = [], 0
        got = {k: [False, False] for k in keys}

        def draw(n=1):
            for _ in range(n):
                if lib:
                    hand.append(lib.pop(0))

        def need_land():
            return lands + hand.count('L') < 4

        def discard_one():
            for c in DISCARD_FIRST:
                if c in hand:
                    hand.remove(c); yard.append(c); return
            if hand.count('L') >= 2 and not need_land():
                hand.remove('L'); yard.append('L'); return
            for c in ['SF', 'SSM']:
                if hand.count(c) >= 2:
                    hand.remove(c); yard.append(c); return
            for c in ['X', 'PU', 'BAT', 'GZ', 'SU', 'BT', 'GR', 'DI', 'MA', 'L', 'SF', 'SSM']:
                if c in hand:
                    hand.remove(c); yard.append(c); return

        def check(mana, t):
            ok = {}
            ok['SSM_BR'] = 'SSM' in hand and mana >= 4 and 'BR' in yard
            ok['SSM_good'] = 'SSM' in hand and mana >= 4 and any(x in yard for x in ['BR', 'AT', 'CO'])
            sf_castable = 'SF' in hand and mana >= 2 + max(0, 4 - len(yard))
            ok['SF_hex'] = sf_castable and 'RW' in yard
            ok['any'] = ok['SSM_good'] or ok['SF_hex']
            i = 0 if t == 3 else 1
            for k, v in ok.items():
                if v:
                    got[k][i] = True

        for t in range(1, 5):
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
                if t >= 3 and 'DI' in hand and mana >= 3 and 'BR' not in yard and ('BR' in lib or 'RW' in lib):
                    hand.remove('DI'); yard.append('DI'); mana -= 3
                    c = 'BR' if 'BR' in lib else 'RW'
                    lib.remove(c); yard.append(c); random.shuffle(lib); progress = True; continue
                if 'MA' in hand and mana >= 2:
                    hand.remove('MA'); mana -= 2
                    yard += lib[:2]; del lib[:2]; draw(2); discard_one(); discard_one(); progress = True; continue
                if 'GR' in hand and mana >= 2:
                    hand.remove('GR'); yard.append('GR'); mana -= 2
                    rev = lib[:5]; del lib[:5]
                    wants = (['SSM'] if 'SSM' not in hand else []) + (['SF'] if 'SF' not in hand else []) \
                        + (['L'] if need_land() else []) + ['SSM', 'SF']
                    take = next((c for c in wants if c in rev), None)
                    if take:
                        rev.remove(take); hand.append(take)
                    yard += rev; progress = True; continue
                if 'SU' in hand and mana >= 1:
                    hand.remove('SU'); mana -= 1; yard += lib[:3]; del lib[:3]; progress = True; continue
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
                if 'RW' in hand and mana >= 1:  # サイクリング
                    hand.remove('RW'); yard.append('RW'); mana -= 1; draw(); progress = True; continue
                if 'BT' in hand and mana >= 2 and any(x in hand for x in ['BR', 'CO', 'AT']) and random.random() < OPP_CREATURE:
                    hand.remove('BT'); yard.append('BT'); mana -= 2
                    c = next(x for x in ['BR', 'CO', 'AT'] if x in hand)
                    hand.remove(c); yard.append(c); progress = True; continue
            if t >= 3:
                check(mana, t)
        for k in keys:
            res[k][0] += got[k][0]
            res[k][1] += got[k][0] or got[k][1]
    return {k: (round(100 * a / N, 1), round(100 * b / N, 1)) for k, (a, b) in res.items()}


def mk(d):
    deck = [k for k, v in d.items() for _ in range(v)]
    assert len(deck) == 60, (len(deck), d)
    return deck


THREATS = dict(SF=4, SSM=4, RW=4, AT=2, CO=1)
VARIANTS = {
    '提案（運び手2、回収4、メカ4、土地24）': dict(THREATS, BR=2, GZ=4, GR=4, MA=4, BT=4, PU=3, L=24),
    '土地23、一押し4': dict(THREATS, BR=2, GZ=4, GR=4, MA=4, BT=4, PU=4, L=23),
    '運び手1＋陽気な哀歌2': dict(THREATS, BR=1, GZ=4, GR=4, MA=4, DI=2, BT=4, PU=2, L=24),
    '運び手1（哀歌なし）': dict(THREATS, BR=1, GZ=4, GR=4, MA=4, BT=4, PU=4, L=24),
    '青黒2色（回収の代わりに縫い師への供給者4）': dict(THREATS, BR=2, GZ=4, SU=4, MA=4, BT=4, PU=3, L=24),
    '参考: V3に近い構成（寓話などは空白扱い、土地20）': dict(SF=4, SSM=4, RW=4, AT=3, CO=1, BR=1, BAT=2, GZ=4, GR=3, PU=2, BT=1, L=20, X=11),
}

if __name__ == '__main__':
    print('値は (3ターン目までに成立, 4ターン目までに成立) の%')
    print('SSM_BR: スーペリア・スパイダーマンで墓地の運び手をコピーできる')
    print('SSM_good: スーペリア・スパイダーマンで運び手・アトラクサ・コズミック・スパイダーマンのどれかをコピーできる')
    print('SF_hex: 縞カワヘビを探査して呪禁の魂剥ぎを唱えられる')
    print('any: SSM_good か SF_hex のどちらか')
    for play in (True, False):
        print('\n先手' if play else '\n後手')
        for name, d in VARIANTS.items():
            print(f'  {name}: {run(mk(d), play=play)}')

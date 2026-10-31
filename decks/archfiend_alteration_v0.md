# Archfiend Alteration v0（Grixis UBR）

- 区分: 現行デッキ（メイン使用）
- ベース: 晴れる屋トライアルTop4のリスト
- リストの版: v0.1（2026-04-22確定。2026-10-31時点でユーザーに確認し、変更なし）

## 勝ち筋

| 勝ち筋 | 内容 | 比率（2026-04時点） |
|---|---|---|
| コンボ | 変態変異（Metamorphic Alteration）でクリーチャーをドロスの魔神（Archfiend of the Dross）のコピーにし、油カウンターを0にして相手を敗北させる | 約40% |
| ミッドレンジ | 鏡割りの寓話（Fable of the Mirror-Breaker）、税血の収穫者（Bloodtithe Harvester）、黙示録、シェオルドレッド（Sheoldred, the Apocalypse）で盤面を取る | 約30% |
| シルバーバレット | 鏡に願いを（Beseech the Mirror）で対面に応じたカードをサーチする | 約30% |

## メインデッキ（60）

```
LANDS (25)
4 Blood Crypt
4 Watery Grave
2 Steam Vents
2 Sulfurous Springs
3 Shipwreck Marsh
3 Blackcleave Cliffs
1 Darkslick Shores
1 Hive of the Eye Tyrant
1 Xander's Lounge
1 Exclusive Nightclub
2 Starting Town
1 Swamp

CREATURES (12)
4 Bloodtithe Harvester
3 Ashling, Rekindled
4 Archfiend of the Dross
1 Sheoldred, the Apocalypse

ENCHANTMENTS / SAGAS (4)
4 Fable of the Mirror-Breaker

SPELLS (19)
4 Thoughtseize
4 Fatal Push
2 Go for the Throat
1 Kolaghan's Command
1 Culling Ritual
3 Metamorphic Alteration
3 Beseech the Mirror
1 Quantum Riddler
```

## サイドボード（15）

```
2 Duress
2 Mai, Scornful Striker
2 Kaito, Bane of Nightmares
1 Damping Sphere
1 Virulent Plague
1 Languish
1 Ashiok, Dream Render
1 Go Blank
1 Invoke Despair
1 Unlicensed Hearse
1 Molten Collapse
1 Unholy Annex
```

## 対面別SBプラン（確定分）

### vs ゴルガリミッドレンジ
- OUT: Sheoldred / Bloodtithe Harvester / Ashling / Fatal Push ×2
- IN: Invoke Despair / Go Blank / Unlicensed Hearse / Kaito ×2
- 1対1交換から2対1交換のカード枚数勝負に切り替える。Match #108–109で再現を確認
- 思考囲い（Thoughtseize）で抜く優先度: Badgermole Mole Pup（マナ加速と、除去されにくい本体でアドバンテージ源になる）> Sentinel of Lost Lore（地図トークンでカードを得る）> その他

### vs ボロス土地破壊
- IN: 強迫（Duress）×2 / 悪夢滅ぼし、魁渡（Kaito, Bane of Nightmares）×2
- OUT: 寓話 / 変態変異
- 基本土地がSwamp 1枚のみで、主要呪文が3〜4マナに集中しているため、2土地で止まると勝てない。メタ上の出現率が低い対面として負けを許容する

## マッチアップ傾向（2026-09時点）

- 有利: フェアなミッドレンジ、コントロール、盤面勝負のデッキ。コンボで予想外のタイミングに勝てる
- 不利: 完成形まで組み上がるコンボ（Creativity、Ramp）
- 不利: ディミーア・バウンス。Yorion 80枚でETBパーマネントを使い回し、ハンデス・除去・バウンスを持つため、コンボ軸でもミッドレンジ軸でも勝ちにくい
- コーリ鋼の短刀（Cori-Steel Cutter）の禁止でアグロが減り、準備に時間がかかるこのデッキには追い風（2026-09時点の見立て。2026-10時点ではイゼット果敢と赤単果敢が上位にいるため当てはまらない。`meta/2026-10_metagame.md` を参照）

## 保留中の検討事項

- SOS新カードの投入候補（Ral Zarek 2、Withering Curse 1、Tragedy Feaster 1）。ダイヤモンド帯到達後に検討する
- 20試合到達後の構造評価: コンボ成立率、Beseechのサーチ先選択の精度、Ashlingで捨てるカードの判断
- 実戦データを集める対面: グリースファング、モノレッド、ボロス召集

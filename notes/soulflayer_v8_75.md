# 魂剥ぎV8（リビエン型）の75枚

作成: 2026-11-01。`notes/soulflayer_v8_proposal.md` の第7版のメインと、第8版のサイドボード（ゴルガリ戦のプランは `notes/soulflayer_v8_matchup_sim.md` の計算で直したもの）をまとめた。まだ実戦で使っていないので、すべて検証前の構築として扱う。75枚のカードはすべてパイオニアで使え、Arenaにある（Scryfall、2026-11-01に確認）。

## メイン60枚

| 枚数 | カード | 役割 |
|:--:|---|---|
| 4 | 魂剥ぎ（Soulflayer） | 勝ち筋。探査で追放したクリーチャーのキーワードを得る |
| 4 | スーペリア・スパイダーマン（Superior Spider-Man） | 勝ち筋。墓地のクリーチャーのコピーとして出る。運び手をコピーすると全体リアニメイト |
| 4 | 縞カワヘビ（Striped Riverwinder） | 呪禁を渡す。サイクリングで自分を墓地に置く |
| 3 | 造反の代弁者、サムト（Samut, Voice of Dissent） | 二段攻撃・速攻を渡す。戦場に戻ると全員に速攻を与える |
| 2 | 最後の贈り物の運び手（Bringer of the Last Gift） | スーペリア・スパイダーマンのコピー先。飛行を渡す |
| 2 | 偉大なる統一者、アトラクサ（Atraxa, Grand Unifier） | コピー先（手札を増やす）。飛行・絆魂などを渡す |
| 4 | 忌まわしい回収（Grisly Salvage） | 墓地を肥やす。勝ち筋のカードか土地を手札に入れる |
| 4 | メカの天才（Does Machines） | 墓地を肥やす。手札の墓地用クリーチャーを捨てる |
| 2 | 幽愁（Wistfulness） | 想起で墓地を肥やすか、アーティファクト・エンチャントを追放する |
| 2 | ダイナの導き（Dina's Guidance） | 運び手を墓地に置くか、スーペリア・スパイダーマンを手札に入れる |
| 1 | 異世界の凝視（Otherworldly Gaze） | 墓地を肥やす |
| 3 | 苦々しい勝利（Bitter Triumph） | 除去。追加コストで墓地用クリーチャーを捨てる |
| 3 | 致命的な一押し（Fatal Push） | 1マナの除去 |
| 4 | 湿った墓（Watery Grave） | 土地 |
| 3 | 草むした墓（Overgrown Tomb） | 土地 |
| 1 | 繁殖池（Breeding Pool） | 土地 |
| 2 | 闇滑りの岸（Darkslick Shores） | 土地 |
| 3 | 花盛りの湿地（Blooming Marsh） | 土地 |
| 2 | 植物の聖域（Botanical Sanctum） | 土地 |
| 4 | 始まりの町（Starting Town） | 土地 |
| 1 | 耐え抜くもの、母聖樹（Boseiju, Who Endures） | 土地。チャネルで置物と土地を破壊する |
| 1 | ヨーグモスの墳墓、アーボーグ（Urborg, Tomb of Yawgmoth） | 土地。全部の土地から黒を出す |
| 1 | 島（Island） | 土地。廃墟の地（Field of Ruin）で探す基本土地 |

土地22枚。色マナ源は黒17（アーボーグがあれば全部）、青14、緑14。

## サイドボード15枚

| 枚数 | カード | 役割 |
|:--:|---|---|
| 3 | 思考囲い（Thoughtseize） | ハンデス |
| 2 | 真っ白（Go Blank） | ハンデス2枚と、相手の墓地の追放 |
| 1 | ヴェールのリリアナ（Liliana of the Veil） | ハンデスと生け贄 |
| 2 | 戦略的裏切り（Strategic Betrayal） | 相手のクリーチャー1体と墓地の追放 |
| 2 | 墓地の侵入者（Graveyard Trespasser） | 墓地を使わない3マナの脅威と、相手の墓地の追放 |
| 2 | 黙示録、シェオルドレッド（Sheoldred, the Apocalypse） | 墓地を使わない4マナの脅威 |
| 2 | 突然の衰微（Abrupt Decay） | マナ総量3以下の土地でないパーマネントの破壊 |
| 1 | 魂標ランタン（Soul-Guide Lantern） | 相手の墓地だけを追放する |

## Arena形式

スーペリア・スパイダーマンは、Arenaでは「Kavaero, Mind-Bitten」と表示される。

```
Deck
4 Soulflayer
4 Kavaero, Mind-Bitten
4 Striped Riverwinder
3 Samut, Voice of Dissent
2 Bringer of the Last Gift
2 Atraxa, Grand Unifier
4 Grisly Salvage
4 Does Machines
2 Wistfulness
2 Dina's Guidance
1 Otherworldly Gaze
3 Bitter Triumph
3 Fatal Push
4 Watery Grave
3 Overgrown Tomb
1 Breeding Pool
2 Darkslick Shores
3 Blooming Marsh
2 Botanical Sanctum
4 Starting Town
1 Boseiju, Who Endures
1 Urborg, Tomb of Yawgmoth
1 Island

Sideboard
3 Thoughtseize
2 Go Blank
1 Liliana of the Veil
2 Strategic Betrayal
2 Graveyard Trespasser
2 Sheoldred, the Apocalypse
2 Abrupt Decay
1 Soul-Guide Lantern
```

## 対面ごとのIN・OUT

「根拠」の列: 計算は `notes/soulflayer_v8_matchup_sim.md` と `notes/soulflayer_v8_interaction_sim.md` の結果。仮説はClaudeの推論だけで、計算も実戦もしていない。

| 対面 | IN | OUT | 根拠 |
|---|---|---|---|
| ゴルガリ・ミッドレンジ | 墓地の侵入者2、黙示録、シェオルドレッド2 | 致命的な一押し3、異世界の凝視1 | 計算（SB後の勝率がSBなしより約5ポイント高い） |
| アブザン脂牙 | 思考囲い3、真っ白2、戦略的裏切り2、魂標ランタン1 | 運び手2、ダイナの導き2、致命的な一押し3、異世界の凝視1 | 計算（相手のキルターンが約1.3ターン遅れる）。運び手を抜くかは確かめていない |
| ラクドス異形化 | 同上 | 同上 | 計算（相手のキルターンが約0.6ターン遅れる）。運び手を抜くかは確かめていない |
| テムール独創力、5色ロナ、スゥルタイ風景の変容 | 思考囲い3、真っ白2、ヴェールのリリアナ1、突然の衰微1 | 致命的な一押し3、苦々しい勝利3、異世界の凝視1 | 仮説 |
| ニクス・ランプ | 思考囲い3、真っ白2 | 苦々しい勝利3、ダイナの導き2 | 仮説 |
| 果敢デッキ（イゼット、赤単） | 黙示録、シェオルドレッド2、突然の衰微2 | ダイナの導き2、異世界の凝視1、アトラクサ1 | 仮説（メインの除去6枚は計算で決めた） |
| ジャンド・サクリファイス | 戦略的裏切り2、墓地の侵入者2、突然の衰微2 | 運び手2、ダイナの導き2、異世界の凝視1、サムト1 | 仮説 |
| アゾリウス・コントロール | 思考囲い3、真っ白2、ヴェールのリリアナ1、黙示録、シェオルドレッド2 | 致命的な一押し3、苦々しい勝利3、運び手2 | 仮説 |

## 実戦で確かめること

1. 土地22枚の過不足と、色マナが足りずに唱えられなかった呪文
2. 手札で使えなかった墓地用クリーチャー（運び手、サムト、アトラクサ）の枚数
3. 相手が使った墓地対策のカードと、勝ち筋が成立したターン
4. 仮説のSBプランを使った試合のMatch #。使ったプランは「仮説」を外す

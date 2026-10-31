# プロジェクト移管メモ — Cowork移管用

> **作成**: 2026-04-22
> **目的**: claude.aiプロジェクト「MTG Pioneer — Soulflayer Lab」を Cowork 環境へ移管するにあたり、これまでの経緯・現状・必要なアクションを整理する。

---

## 1. プロジェクト概要

### 目的
MTG Arenaでミシック上位に定着し、パイオニア環境の競技イベント（MITQ等）でも勝つための戦略支援プロジェクト。

### ユーザープロファイル
- **フォーマット**: パイオニア（MTG Arena / Explorer）
- **レベル**: 競技志向（MITQ等の紙イベントにも参加）
- **目標**: Arenaミシック上位定着
- **構築哲学**: メインの少なさと濃さ × 汎用カードシェルとの噛み合い × SB変身の駆け引き

### Claudeの役割
1. デッキ選択・調整の壁打ち
2. 対戦振り返り・反省分析
3. 新カード・新環境のメタ予測
4. デッキ別の戦略最適化

---

## 2. これまでの経緯（Soulflayer時代）

### 開始から V6 まで
- **1デッキ特化型**で Soulflayer（魂剥ぎ）を運用
- V3 → V4 → V4.1 → V4.12 → V5 → V5.1 → V6 → V7 → V8（構想） と継続的に改訂
- **V6 Esper（WUB、2026-02-27確定）** が最終形
  - 寓話・回収・サムト全カット
  - 繕い+耽溺のルーティング掘り
  - 干渉11枚メイン
  - 記念碑+ケトラモーズ+シェオルが非墓地勝ち筋
  - SB: 否認2強迫2星檻2記念碑2拒否権1評決1アショク1塵1ケトラ1シェオル1無効1

### V7 / V8 の試行
- **V7（Sultai）**: テスト済、爆発力不足で V6/Esper への回帰または V8 検討の根拠に
- **V8（Sultai）**: 構想段階。SSM（Superior Spider-Man）+ Bringer of the Last Gift コンボ + 魂剥ぎ。設計セッションは69枚から3案（エンジン重視/ドナー重視/バランス）の選択未決で中断

### 累積戦績
- **Match # 94まで** Notion DBに記録済み
- 通算データ・マッチアップ傾向はNotionが Single Source of Truth

---

## 3. 移行の経緯（2026-04-22）

### きっかけ
ストリクスヘイブンの秘密（SOS）リサーチ後、「魂剥ぎを抜きにしてゼロから握るべきデッキ」を診断。3問の質問で得たプロファイル：

1. 魂剥ぎで一番ハマってた要素 → **サイド変身・対面読みの駆け引き**
2. 試合ペース → アグロ以外は差がない
3. プレイ中のストレス → **相手の動きにロックされる**

### デッキ選定プロセス
- **第1候補**: Enigmatic Fires → ユーザー指摘により脱落（Yorion 80枚は「メインパーツの濃さ」と「サイド芸が決まる構造」を満たさない）
- **第2候補**: Niv to Light → 同じ理由で脱落
- **採用**: Archfiend Alteration（晴れる屋トライアルTop4ベース、Grixis）
  - 鏡割り重視・ドロスの魔神入り・Beseech the Mirrorによる動的シルバーバレット
  - 「メインの少なさと濃さ × 汎用シェル × SB変身」の構造を最も純粋に満たす

### 実戦テスト結果
- **シルバー1 → プラチナ1で8連勝**
- 対面: ラクドスデーモン、イゼフェニ、アゾコン、ジェスカイコン、白単人間
- 勝ち筋分布: **コンボ40% / ミッドレンジ30% / Beseechシルバーバレット30%**
  - 3軸並列で機能する構造的健全性を確認
  - ただしダイヤモンド帯前のサンプルとしては母数不足（信頼区間広い）

---

## 4. 現状（移管時点）

### 並行運用デッキ
1. **Archfiend Alteration**（メイン使用、Grixis）
   - 晴れる屋トライアルTop4ベース
   - Arenaラダー実戦投入中
2. **Soulflayer V6 Esper**（テスト継続、WUB）
   - 完成度高、いつでも復帰可能
3. **Soulflayer V8 Sultai**（構想段階）
   - SSM+Bringer+魂剥ぎ
   - 構築方向性未決

### Notion戦績DB
- Match # は **95から連続採番**（デッキ非リセット）
- DBに「使用デッキ」識別の追記が必要
  - 案A: タイトル末尾に `[ArchAlt]` 等のタグ
  - 案B: Key Takeaway内に明記
  - 案C: 新規Selectプロパティ「Deck」を追加

---

## 5. 移管時に必要なアクション

### Cowork側で再構築するもの

#### A. カスタム指示
- **アーキタイプ非依存の構成**に書き換え済み（本会話内で議論済み）
- 「現在使用中のデッキ」を可変参照にする
- ARCHIVE/プレフィックスでSoulflayer関連を分離

#### B. プロジェクトファイル

**新規作成が必要**:
- `CURRENT_DECKS.md` — 並行運用デッキ一覧（メモリの拡張版）
- `archfiend_alteration_v0.md` — メインデッキの詳細リスト＋SBプラン
- `index.md` — 新構造を反映した参照ガイド

**ARCHIVE/プレフィックスでリネーム**（Soulflayer V6関連）:
- `ARCHIVE/soulflayer_v6_decklist.md`
- `ARCHIVE/soulflayer_v6_decklist-1.md`
- `ARCHIVE/soulflayer_v7_design_notes.md`
- `ARCHIVE/soulflayer_v3_2_sb_plans.md`
- `ARCHIVE/soulflayer_v4_*`（全部、5ファイル程度）
- `ARCHIVE/soulflayer_v5_decklist.md`
- `ARCHIVE/v4_variable_catalog_*`（2ファイル）
- `ARCHIVE/soulflayer_lock_variable_map_v3.md`
- `ARCHIVE/soulflayer_deck_analysis_v3_1.md`
- `ARCHIVE/soulflayer_framework.md`

**そのまま残すもの（汎用・継続利用）**:
- `パイオニア_Pioneer_フォーマット包括ナレッジベース__メタゲーム_カードプール_禁止リスト総合分析.md`
- `match_log_entry_guide.md`
- `oracle_compact.md` / `oracle_compact_opponent.md`
- `oracle_core.csv` / `oracle_opponents.csv`
- `oracle_sos_candidates.md`
- `Pioneer_s_February_2026_Metagame__Greasefang_and_Cori-Steel_Cutter_Rule.md`
- `vs_black_midrange_guide.md`
- `scam_axis_analysis.md`
- `soulflayer_graveyard_strategy_framework.md` / `.html`（汎用墓地戦略）

#### C. Notion連携
- 戦績DB: `collection://6782b463-e3f6-439c-9432-44b88499e3cd`
- 親ページURL: https://www.notion.so/305e124c3ac7813f8cecc0828530f3b8
- Match # 95から連続採番
- 「使用デッキ」識別方法を決定（A/B/C案のいずれか）

#### D. メモリ
Cowork移行時、以下のメモリを引き継ぎ（現claude.aiメモリの内容）:

1. Match log: Latest confirmed Match # = 94
2. CURRENT_DECKS（複数デッキ並行運用、2026-04-22〜）
3. Bo3先後ルール（負け先、G1ユーザー申告、G2以降自動判定）

---

## 6. 進行中の懸案

### Archfiend Alteration関連
- **20試合到達後の構造評価**（コンボ成立率、Beseechターゲット選択精度、Ashling捨てカード判断）
- **SOS新カード投入候補**（Ral Zarek 2、Withering Curse 1、Tragedy Feaster 1） → **ダイヤモンド帯到達後に検討**
- **対グリースファング・対モノレッド・対ボロス召集** の実戦データ蓄積

### Soulflayer V8関連
- 構築方向性決定（エンジン重視 / ドナー重視 / バランス）
- パラ運用するか引退するかの判断

### 環境
- Cori-Steel Cutter禁止議論の動向
- SOS発売後（4/24紙、Arena配信済）のメタゲーム変動観測

---

## 7. 次の論点（Cowork初回会話時）

優先順位順：

1. **ファイル移管とリネーム**: ARCHIVE/構造への再編成
2. **CURRENT_DECKS.md と archfiend_alteration_v0.md の作成**
3. **Notion戦績DB**の「使用デッキ」識別方法決定
4. **Match #95からの戦績登録**（Archfiend Alterationの8連勝分を遡って登録するか、今後の試合から記録するか）
5. **カスタム指示の最終版確定とプロジェクトへの適用**

---

## 8. リスト：Archfiend Alteration v0.1（参考）

```
// MAIN (60)
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

// SIDEBOARD (15)
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

実戦実績: シルバー1→プラチナ1で8連勝（2026-04-22時点）

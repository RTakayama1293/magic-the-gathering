# プロジェクトの現状

最終更新: 2026-10-31（claude.aiからの移管時点）

## ラダーの状況

- 2026-09時点: プラチナ帯。直近のラダーセッションで18勝6敗
- 最新のMatch #は113（2026-09時点）。登録前には必ずNotion DBで最新値を確認する
- Soulflayer単独特化（約1年）から、2026-05に複数デッキ並行テストへ方針を変えた

## 未処理のタスク

- Notion戦績DBの `SB Depth` の選択肢がSoulflayer時代のまま（変身なし / 部分変身 / 全変身 / 偶察）。Archfiend Alteration用に選択肢を足すか、プロパティを使わないままにするかを決める
- `match_log_entry_guide.md` はSoulflayer V6時代の版。Archfiend Alteration用のSB Depthの扱いが決まったら書き直す
- `oracle/oracle_core.csv` と `oracle/oracle_compact.md` にArchfiend Alterationの採用カードを追加する（ドロスの魔神・変態変異・寓話・思考囲いは収録済み。血税の収穫者・Ashling・鏡への懇願・Quantum Riddler等は未収録）
- 環境観測: Cori-Steel Cutter禁止後とSOS発売後のメタ変動

## 移管時のファイル整理

- claude.aiプロジェクト上で同じ名前のファイルが2つずつあったもの（`soulflayer_v6_decklist.md`、`match_log_entry_guide.md`、`soulflayer_v4_12_decklist.md`）は、取得できた片方だけを移した
- `oracle_core.json` / `oracle_opponents.json` は廃止済みのため移していない。CSV版が正
- `soulflayer_deck_analysis_v3_1.md` は文字コードが壊れていたため機械的に復元した。日本語の一部に誤字が残っている可能性がある
- claude.aiの旧INDEX（Soulflayer V6用）は `ARCHIVE/index_soulflayer_v6.md`、2026-04のCowork移管メモは `ARCHIVE/cowork_migration_memo.md` に置いた

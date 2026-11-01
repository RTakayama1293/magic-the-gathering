# プロジェクトの現状

最終更新: 2026-10-31（Claude Codeでの初回整備の後）

## ラダーの状況

- 2026-05時点: プラチナ帯。2026-06〜10は休止していた
- Notion戦績DBの最新はMatch #113（vs ボロスバーン①、2026-05-16）。Archfiend Alterationでの登録は18マッチ9勝9敗（2026-05-06〜05-16）。2026-06〜09は試合をしていない（2026-10-31にユーザーに確認）
- 登録前には必ずNotion DBで最新値を確認する
- Soulflayer単独特化（約1年）から、2026-05に複数デッキ並行テストへ方針を変えた

## 未処理のタスク

- Notion戦績DBの `SB Depth` の選択肢がSoulflayer時代のまま（変身なし / 部分変身 / 全変身 / 偶察）。Archfiend Alteration用に選択肢を足すか、プロパティを使わないままにするかを決める
- `match_log_entry_guide.md` はSoulflayer V6時代の版。Archfiend Alteration用のSB Depthの扱いが決まったら書き直す
- （完了）Notion戦績DBのSoulflayer時代の102件に `使用デッキ` =「Soulflayer」を入れた。2026-10-31にDBを読み戻し、空欄0件、Soulflayer 102件（37勝65敗）、Archfiend Alteration 18件（9勝9敗）を確認した
- 再開デッキの選択: Archfiend Alterationに戻るか、Soulflayerを再開するか
- 魂剥ぎV8（スーペリア・スパイダーマン＋最後の贈り物の運び手＋魂剥ぎのスゥルタイ）の構築案を `notes/soulflayer_v8_proposal.md` に書いた（2026-11-01）。現行デッキとして `decks/` に登録するかは未決
- `meta/2026-10_metagame.md` の分析をもとに、Archfiend Alterationを今の環境に持ち込むかを議論する（イゼット果敢・赤単果敢・ジャンド・サクリファイスへのSBプランが無い）
- 次の禁止改定の発表（2026-11-30）の後に、`.claude/skills/meta-update/SKILL.md` の手順でメタを調べ直す

## 2026-10-31の整備で行ったこと

- private リポジトリの Claude Code 設定（UserPromptSubmit フックの書き方リマインダ、implementer と verifier のエージェント、CLAUDE.md の共通節）をこのリポジトリに写した
- `tools/fetch_oracle.py` を作り、カードのオラクルテキストと日本語名を Scryfall から `oracle/cards.csv` に取得するようにした。旧ファイル（`oracle_core.csv` など）は `ARCHIVE/oracle_old/` に移した
- `tools/check_names.py` を作り、文書中の「日本語名（英語名）」を `cards.csv` と照合するようにした。誤っていた日本語名（税血の収穫者、鏡に願いを、未認可霊柩車など）を直した
- 2026-10時点のメタを調べて `meta/2026-10_metagame.md` を作った

## 移管時のファイル整理

- claude.aiプロジェクト上で同じ名前のファイルが2つずつあったもの（`soulflayer_v6_decklist.md`、`match_log_entry_guide.md`、`soulflayer_v4_12_decklist.md`）は、取得できた片方だけを移した
- `oracle_core.json` / `oracle_opponents.json` は廃止済みのため移していない。CSV版も2026-10-31に `ARCHIVE/oracle_old/` へ移し、`oracle/cards.csv` に置き換えた
- `soulflayer_deck_analysis_v3_1.md` は文字コードが壊れていたため機械的に復元した。日本語の一部に誤字が残っている可能性がある
- claude.aiの旧INDEX（Soulflayer V6用）は `ARCHIVE/index_soulflayer_v6.md`、2026-04のCowork移管メモは `ARCHIVE/cowork_migration_memo.md` に置いた

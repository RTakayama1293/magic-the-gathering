---
name: meta-update
description: パイオニアのメタゲームを調べ直し、meta/<年>-<月>_metagame.md を作る。禁止改定の発表後、新セットの発売後、前回の調査から1か月以上たったとき、「最近のメタは」「環境どうなってる」と聞かれたときに使う。
---

# メタゲームの調べ直し

`meta/` の最新ファイルの調査日を見て、そこから後に起きたことを調べる。結果は新しいファイル `meta/<年>-<月>_metagame.md` に書き、古いファイルは書き換えない。

## 調べること

1. 禁止改定: 前回の調査日以降の発表（https://magic.wizards.com/en/banned-restricted-list と各発表ページ）。次の発表予定日も書く
2. 新セット: 前回以降に発売されたセットと、パイオニアの上位デッキが使っている新カード
3. 使用率: MTGGoldfish（https://www.mtggoldfish.com/metagame/pioneer/full ）と晴れる屋（https://www.hareruyamtg.com/ja/deck/20/metagame/ ）。集計期間と母数を書く
4. 直近の大きな大会の上位8（晴れる屋の大会、MTGO RC Super Qualifier、RC、プロツアー）
5. Arenaのイベント予定（Qualifier Play-In / Weekend、Arena Championship）
6. 現行デッキ（`CURRENT_DECKS.md`）のアーキタイプの大会結果と最新リスト

## 書き方

- すべての事実に出典のURLを付ける。確かめられなかったことは「見つからなかった」と書く。検索結果の要約しか読めなかったものは、そう書く
- 事実の節と「このデッキへの影響（分析）」の節を分ける。分析は `decks/` のファイルのマッチアップ傾向・SBプランと照らして書く
- 新しく出てきたカードは `oracle/lists/meta_<年>-<月>.txt` に英語名で足し、`python3 tools/fetch_oracle.py` を実行する。日本語名は `oracle/cards.csv` から取る
- 書き終えたら `python3 tools/check_names.py` を実行して問題0件にする

## 書いた後

- `CLAUDE.md` の「情報の鮮度」節にある最新ファイル名と次の禁止改定の日付を直す
- `decks/` のマッチアップ傾向やSB方針に、前提が変わった記述があれば、日付付きで注記する
- 前提が大きく変わったとき（デッキのカードの禁止、上位デッキの入れ替わり）は、ユーザーへの報告の最初に書く

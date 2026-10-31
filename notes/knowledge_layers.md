# 判断の層ごとの知見

最終更新: 2026-10-31

勝率を上げる判断を、取り組み方からArenaの操作まで11の層に分け、知見を1つのファイルにまとめた。前半の「使える知見」は、パイオニア（Arenaのラダーと紙の大会）でそのまま判断に使えるものを層ごとに並べた。後半の「アーカイブ」には、ほかのフォーマットだけの話、古いルール、出典を確かめられなかったもの、1試合だけの記録などを置いた。出典は末尾の一覧にIDで載せた。

調査の元の記録（発言の引用や、確かめられなかった点の詳細）は `notes/sources/` にある。

## 根拠の表記

| 表記 | 意味 |
|---|---|
| プロ | トッププロ・強豪が書いた記事か、本人の発言を直接引用したインタビュー |
| DB #n | 戦績DBのMatch #。試合数を書く |
| ユーザー | ユーザーが決めた方針 |
| 数学 | 計算で確かめられる事実 |
| Gemini | ユーザーがGemini Notebookで調べた結果。元の動画で確かめられないので二次として扱う |
| 仮説 | Claudeの推論 |

## 層の一覧

| 層 | 判断の中身 |
|---|---|
| 0 取り組み方 | 練習の形、振り返りの手順、負けの受け止め方 |
| 1 大会と形式 | Arenaのラダー・Bo1・Bo3・紙の大会の違い、リスト公開、時間制限 |
| 2 メタの読み | どのデッキがどれだけいるか、それをどう扱うか |
| 3 デッキ選択 | どのデッキを使うか |
| 4 構築 | 勝ち筋の骨格、カードの採否と枚数、マナベース |
| 5 サイドボード | SBの選び方、IN・OUT、先手後手での違い |
| 6 ゲームの入口 | 先手後手の選択、マリガン、キープの基準 |
| 7 ゲームプラン | 自分の役割、勝ち筋の選択、勝つ・負ける条件の把握 |
| 8 局面の判断 | 攻撃とブロック、除去やハンデスの対象、カウンターへの対処、相手の手札の読み |
| 9 マナと手順 | 土地を置く順番、タップする土地、呪文を唱える順番、構えるマナ |
| 10 操作と時間 | Arenaの操作、タイマー、紙の大会の時間 |

---

# 使える知見

## 0. 取り組み方

| 知見 | 根拠 | 出典 |
|---|---|---|
| 負けたら、技術的なミスと判断、精神面、SBと構築、デッキ、運の順に原因を調べる。運はほかを調べ尽くしてから見る | プロ（Reid Duke） | RD3 |
| 負けは常に自分の実力のせいと考える。勝った試合でも運の要素を分けて考える。考えられていなかった点は「技術が低いだけ」と認める | プロ（原根健太） | H4、H6 |
| 練習は時間数より、その時間から何を持ち帰るかで決まる。疲れたまま、ほかのことをしながらの練習はしない | プロ（Reid Duke） | RD3 |
| 強い相手と戦わないと自分の弱点に気づけない | プロ（八十岡翔太、原根健太） | Y6、H4 |
| 本番に近い形で練習する | プロ（原根健太） | H6 |
| 各ゲームに一言のメモを残す。対戦前に対面の展開を想像し、対戦で確かめる | プロ（Lucas Esper Berthoud） | LB1 |
| 負けたデッキでも、良かった部分を拾う | プロ（市川ユウキ） | IC1 |
| 対戦相手のターン中に次の自分の行動を決め、相手のプレイから情報を拾う | プロ（Reid Duke） | RD5 |
| 結果ではなく、その時点で見えていた情報での期待値で判断を評価する | ユーザー | CLAUDE.md |
| 試合数が少ないうちの勝率は幅が広い（10勝10敗で30%〜70%）。勝敗の数より試合の中で起きたことを記録する | 数学 | `notes/decision_criteria.md` 2章 |

## 1. 大会と形式

| 知見 | 根拠 | 出典 |
|---|---|---|
| 相手の履歴から使うデッキを読む「人読み」は、リーグ戦では使えるが、誰と当たるか分からない大会では使えない | プロ（佐藤レイ、八十岡翔太） | Y4 |
| デッキリスト公開制の大会では、相手が単体除去を自由に撃てるので、防御の呪文の価値が上がる | プロ（行弘賢） | YU2 |
| 自分のプレイ速度で時間内に終えられないデッキは使わない | プロ（PVDDR） | PV1 |
| 決勝ラウンドなど相手がリストを知っているときは、デッキの正体を隠す手が使えない | プロ（Mike Flores） | MF1 |

Arenaのラダー（Bo1とBo3）と紙の大会で何を変えるかは、ユーザーと決める論点として `notes/decision_criteria.md` 5章に置いてある。

## 2. メタの読み

| 知見 | 根拠 | 出典 |
|---|---|---|
| 使用率12%と8%のデッキでは当たる確率にほとんど差がない。使用率20%を超えるデッキがあるときだけメタを意識する | プロ（八十岡翔太） | Y1 |
| 一強の環境では、そのデッキを使うか、そのデッキに強いデッキを使う。一強をメタったデッキをさらにメタると失敗しやすい | プロ（八十岡翔太） | Y1 |
| メタを読むときに自分のデッキの好みを混ぜない | プロ（PVDDR） | PV1 |
| 来るデッキの予想は部分的に外れる | プロ（Reid Duke） | RD1 |
| 環境を定義しているカードと、環境が向かっている方向を理解する | プロ（市川ユウキ） | IC1 |
| メタの仮説を文章で書き、その仮説を覆せる要素（別の攻め手、SBプランの刷新、古いデッキの再利用）を探す | プロ（Lucas Esper Berthoud） | LB1 |
| メタの資料は出典URLと集計期間のあるものだけを使う | リポジトリの決まり | `.claude/skills/meta-update/SKILL.md` |

## 3. デッキ選択

| 知見 | 根拠 | 出典 |
|---|---|---|
| どのデッキを選ぶかより、選んだデッキをどれだけうまく使えるかが大事 | プロ（Reid Duke、八十岡翔太） | RD1、Y1 |
| 練度の中身は、主要な対面との相性、SBとキープの基準、ミラーマッチの勝ち方を理解していること | プロ（八十岡翔太） | Y1 |
| ミラーマッチで勝つ手段があることは、デッキを選ぶ理由になる | プロ（八十岡翔太） | Y1 |
| 全部の対面で45〜55%の、極端な負け方をしにくいデッキを選ぶ。1つでも勝てない相手がいると優勝できない | プロ（原根健太、PVDDR） | H1、PV1 |
| Arenaの勝率は広い相手との数字なので、そのままデッキ選択に使わない。勝率が高い理由（自分がやり込んだのか、SBプランができているのか）を理解してから使う | プロ（覚前輝也、行弘賢） | Y4 |
| 強いデッキの条件は、マリガンに強い、ぶん回りがある、長期戦に強い | プロ（渡辺雄也） | WY1 |
| 結果が出ているデッキは、メタが実際に変わるまで手放さない | プロ（Brad Nelson） | BN1 |
| デッキ選択で好みを優先しすぎない。1つのデッキにこだわりすぎない | プロ（原根健太、市川ユウキ） | H4、IC1 |

考えが分かれる点: 練度を優先する（八十岡翔太、Reid Duke）か、チームのリストと勝率データを信頼して練習していないデッキも使う（原根健太、H3）か。ユーザーは個人で調整しているので、チームのデータに当たるものは無い。

## 4. 構築

### 4-1. 勝ち筋とデッキの骨格

| 知見 | 根拠 | 出典 |
|---|---|---|
| 同じ資源を使って勝つ手段が複数あるのは強みとして扱う。1ゲームの中でどれを使うかはその場で選ぶ | ユーザー | `notes/play_learnings.md` |
| メインのカード種類を少なく、1種類の枚数を厚くし、汎用カードで固める | ユーザー | CLAUDE.md |
| カード名ではなく、カードの種類（役割）でデッキのテンプレートを作る | プロ（八十岡翔太） | Y2 |
| 遅いデッキでも能動的な勝ち筋を持つ。長期戦で勝てると思い込んでいて実際は勝てないのが一番危ない | プロ（Reid Duke） | RD1 |
| デッキはSB後の75枚の強さでも評価する | プロ（Reid Duke） | RD1 |
| ミッドレンジのカードは、守る段階か攻めに転じる段階のどちらかに役立つものにする | プロ（Reid Duke） | RD7 |
| 最良のデッキは多くの対面でビートダウンとコントロールの両方の役割を取れる | プロ（Mike Flores） | MF1 |

### 4-2. カードの採否と枚数

| 知見 | 根拠 | 出典 |
|---|---|---|
| カードを入れる理由を、そのカードを使いたい具体的な場面と相手のカードで判断する。各カードの役割を説明できるようにする | プロ（原根健太、渡辺雄也） | H2、WY2 |
| 枚数は実際に回して決める。2回唱えればほぼ勝つカードは3枚でよい | プロ（八十岡翔太） | Y3 |
| 「強い」「弱い」だけで採否を書かず、何に対して、どの場面で、何をするから採るのかを書く | リポジトリの決まり | `notes/decision_criteria.md` 3-3 |
| マリガンしたくなる初手が多いなら、構築を変えて防ぐ | プロ（津村健志、高橋優太） | TT1 |

### 4-3. マナベース

| 知見 | 根拠 | 出典 |
|---|---|---|
| 色マナ源の必要枚数（60枚、土地25枚前提）: 1ターン目の1マナ色1つで14枚、1C 13、2C 12、CC 21、1CC 18、2CC 16、1CCC 21など | プロ（Frank Karsten） | FK1 |
| 1ターン目の呪文にはアンタップで出る土地だけを数える。2ターン目以降はタップインの土地も数える | プロ（Frank Karsten） | FK1 |
| 多色の呪文は色ごとの必要数に1を足す（パイオニアのラクドスの例: 税血の収穫者（Bloodtithe Harvester）に黒14・赤14） | プロ（Frank Karsten） | FK1 |
| 3色以上で複数の色を濃く要求するデッキでは、色を選ぶ土地を完全な源として扱えない | プロ（Frank Karsten） | FK1 |
| 探査などでコストが下がる呪文は、実際にタップすると見込む土地の数でコストを置き換えて表を引く | プロ（Frank Karsten） | FK1 |
| 鏡割りの寓話（Fable of the Mirror-Breaker）4枚を、4マナ以上の呪文に対して黒1・赤1の源として数える | プロ（Frank Karsten） | FK1 |
| タップインの土地の上限の目安は、1マナ域のあるアグロで3枚、1マナ域のないミッドレンジで9枚 | プロ（Frank Karsten） | FK1 |
| 後手のときは先手より土地を1枚減らしてよい。干渉してこない相手には土地を増やし、リソースを交換し合う長いゲームでは減らす | プロ（Frank Karsten） | FK2 |
| 構築の土地は25枚が標準。少なすぎる危険は多すぎる危険よりずっと大きい。寓話の入ったデッキは土地を多めにする | プロ（Reid Duke） | RD11、RD5 |
| 呪文を1ターン遅れて唱えるほうが唱えられないよりよいので、色を足すより減らすほうを選ぶ | プロ（Reid Duke） | RD11 |
| ショックランドで払うライフは、攻撃的でない相手にも積み重なる | プロ（Reid Duke） | RD11 |
| 基本土地を減らす罰のあるカードがある環境では、基本土地を数枚入れる。1枚でも0枚よりずっとよい | プロ（Reid Duke） | RD11 |
| 色を「この色が出ない土地は入れない」「この色が無い手札はキープしない」「主な色」「副の色」「タッチ」に分けて配分する | プロ（Reid Duke） | RD12 |
| パイオニアのファストランドは、思考囲いや致命的な一押しを使う序盤に動くデッキに入れる。主な呪文が4マナ以上のコントロールには向かない | プロ（Martin Jůza） | MJ1 |
| 始まりの町（Starting Town）は3色のアグロやコンボの色マナを安定させる | プロ（Frank Karsten） | FK4 |
| 3色デッキで3ターン目に3色すべてを約80%でそろえるには、各色15枚の源が要る | プロ（金子真実、塚本） | KT3 |
| Archfiend Alterationの色マナ源は、2ターン目以降で黒23・赤15・青14枚で、Karstenの目安を上回る | 仮説（Karstenの表との照合） | `notes/sources/pro_thinking_lower.md` 末尾 |

## 5. サイドボード

| 知見 | 根拠 | 出典 |
|---|---|---|
| SBは何に対して使うカードかを明確にする。対面を理解していなければ正しく組めない | プロ（八十岡翔太、PVDDR） | Y3、PV1 |
| SBは対面で選び、特定の1枚のカードで選ばない。各対面でメインから抜いてよいカードの枚数を数えてSBの枚数を決める | プロ（Reid Duke） | RD2 |
| 1つのデッキ専用のカードより、幅広く対策できるカードを多く用意するほうが全体の勝率が上がる | プロ（八十岡翔太） | Y3 |
| SB後のゲームはG1より遅くなり、ドローや重い呪文の価値が上がる。元のプランが通らないならプランごと変える | プロ（Sam Black） | SB1 |
| 相手のSB後のプランを予測して対策する | プロ（Sam Black、PVDDR） | SB1、PV2 |
| 先手ではデッキの中心を残して入れ替えを少なくし、後手では対応寄りにする。SB後はマリガンの基準も変える | プロ（PVDDR） | PV2 |
| G2とG3の間でSBを見直す。予測されないことに価値があることもある | プロ（Reid Duke） | RD2 |
| G1で得た情報と感じたことをSBに反映する | プロ（原根健太） | H3 |
| 相手のフィニッシャーで負けたように見えても、本当の負けの理由を見てSBする | プロ（Reid Duke） | RD10 |
| SBで1つの対面に寄せすぎると、ほかのデッキに弱くなる | プロ（中村修平） | NK1 |
| SB後にデッキの戦い方を変えて相手の読みを外す | ユーザー | CLAUDE.md |
| 対ゴルガリ・ミッドレンジでは、1対1交換から2対1交換に切り替えるSBで勝った | DB #108・#109（2試合） | 戦績DB |

## 6. ゲームの入口

| 知見 | 根拠 | 出典 |
|---|---|---|
| 迷ったら先手を取る。後手を選ぶのは、序盤のテンポで優位を得にくい、ゲームが長引くなどの条件が全部そろうときだけ | プロ（Reid Duke） | RD4 |
| 先手の有利は「あって55%」。後手の勝ち方はカードの交換で、先手の理想の動きをなぞると負ける | プロ（茂里憲之） | MO1 |
| パイオニアは先手の有利が大きいという評判がある。後手でさらにタップインの土地から始めると大きく不利になる | プロ（Martin Jůza） | MJ1 |
| 後手では、安い干渉で相手の序盤の優位を消すことに集中する | プロ（Reid Duke） | RD5 |
| キープの基本は土地2〜5枚。迷う手札は最良・最悪・平均の3つの展開を想像する | プロ（Reid Duke） | RD6 |
| どちらかが速いデッキなら少し厳しくマリガンする。両方遅いなら少し緩くする | プロ（Reid Duke） | RD6 |
| 最初のドローで土地を引く確率は50%弱。最初のドローで土地を引く必要がある手札はキープしない | プロ（Reid Duke） | RD6 |
| 色が1つ欠けた手札は、残りの色で唱えられる呪文が1枚も無ければマリガンする | プロ（Reid Duke） | RD6 |
| 初手7枚を見たら4ターン先まで想像し、動けるターンを1点として数える。後手で2ターン目をパスする手札は危ない | プロ（高橋優太、津村健志） | TT1 |
| SB後に入れたキーカードの有無をキープの基準に入れる | プロ（津村健志） | TT1 |
| ミッドレンジで対コンボの妨害が思考囲いだけなら、思考囲いの有無をマリガンの基準に入れる | プロ（Reid Duke） | RD7 |
| パイオニアのラクドスの先手で、土地5枚と税血の収穫者・鏡割りの寓話の手札はキープする | プロ（Reid Duke） | RD6 |

## 7. ゲームプラン

| 知見 | 根拠 | 出典 |
|---|---|---|
| 自分の役割（ビートダウンかコントロールか）は相手によって入れ替わる。役割を誤るとゲームを落とす | プロ（Mike Flores） | MF1 |
| 役割は「どちらがダメージを多く出せるか」「どちらが除去を多く持つか」で見分け、決めたら役割に沿って動く | プロ（Mike Flores） | MF1 |
| 先手は攻撃する理由が多く、後手は1枚多い手札でダメージを防ぐ。先手と後手で戦い方を変える | プロ（Mike Flores） | MF1 |
| 自分の本当の役割（デッキの正体）を隠すと有利になる | プロ（Mike Flores） | MF1 |
| ミッドレンジは、まず守ってマナを伸ばし、次に攻めに転じる | プロ（Reid Duke） | RD7 |
| ミッドレンジ対アグロでは、レースに乗らず安定させてから早く終わらせる | プロ（Reid Duke） | RD7 |
| ミッドレンジ対コンボでは、妨害しながら一番強い脅威を早く出す。3ターン目に負けても7ターン目に負けても同じなのでリスクを取る | プロ（Reid Duke） | RD7 |
| 対コントロールでは、相手が望む「1枚ずつ答えられる」ゲームを避ける | プロ（Reid Duke） | RD10 |
| ゲームに勝つ・負けるには何が起きる必要があるかを常に把握する | プロ（PVDDR） | PV1 |
| ライフを0にする前の「実質勝ち」（リソース、ライフ、テンポのどれで勝つか）を目標にする。どうすれば負けないかでなく、どう勝つかを考える | プロ（茂里憲之） | MO1 |
| 自分があと何ターン持つかと、相手を倒すまで何ターンかを数える。不利なのに保守的に構えると逆転の目が無くなる | プロ（金子真実、塚本） | KT1 |
| 有利か不利かを早く決めつけない。局面は毎ターン変わる | プロ（佐藤レイ） | SR1 |
| ドロスの魔神（Archfiend of the Dross）を攻撃役にするかブロック役にするかを毎ターン決めてから動く | DB #107・#112（2試合） | 戦績DB |
| 相手がこのデッキをライフゲインのデーモンデッキと誤認するので、デッキの正体を早く見せない | DB #102・#105（2試合） | 戦績DB |

## 8. 局面の判断

### 攻撃とブロック

| 知見 | 根拠 | 出典 |
|---|---|---|
| たくさん攻撃し、たくさんブロックする。相手がマナを残して攻撃してきても、たいていはブロックしてトリックを使わせる。例外はブロッカーが勝ち筋の中心のとき | プロ（Reid Duke） | RD5、RD9 |
| 攻撃するかは+2点の価値で決まり、相手のライフと手札の枚数で変わる。キルターンを確かめながら決める | プロ（佐藤レイ） | SR1 |
| 生き延びるためでなく勝つためにプレイする。安全策で数ターン先の負けを増やすなら、その安全策は取らない | プロ（Reid Duke） | RD5 |

### 除去とハンデス

| 知見 | 根拠 | 出典 |
|---|---|---|
| 思考囲い（Thoughtseize）は、相手の手札の穴（場の脅威への答えが無いなど）を作るカードを抜く。作れなければ一番強いカードを抜く。マナ加速を抜いて土地事故を狙わない | プロ（Reid Duke） | RD13 |
| 相手の脅威が問題なら、思考囲いは止められる範囲でできるだけ遅く撃つ。相手のカウンターが問題なら、自分の重要な呪文を通す前のターンか同じターンに撃つ。理由が無ければ1ターン目に撃たない | プロ（Reid Duke） | RD13 |
| 思考囲いでは、ゲームの構造を変えるカードを1対1の干渉呪文より優先して抜く | DB #59・#90・#108（3試合） | 戦績DB |
| 対ゴルガリの思考囲いは、アナグマモグラの仔（Badgermole Cub）と名もなき都市の歩哨（Sentinel of the Nameless City）を優先して抜く | DB #108・#109の学び欄 | 戦績DB |
| ハンデスは、相手が強い行動を先に取れないようにし、自分の後のターンをタップアウトできるようにする | プロ（Reid Duke） | RD7 |
| 除去は相手のクリーチャーに合う順に使う。置いておくと得をし続けるカードはすぐ除去する | プロ（Luis Scott-Vargas） | LSV1 |
| 序盤の除去は相手の最初の展開を止めるために使う | プロ（Reid Duke） | RD8 |
| インスタントの除去は、相手の攻撃時誘発や瞬速の有無を見て使う時期を決める | Gemini | `notes/sources/gemini_dengeki_2026-10-31.md` |

### カウンターへの対処

| 知見 | 根拠 | 出典 |
|---|---|---|
| 相手が別の強い行動にマナを使いたいターンに重要な呪文を唱える。相手の切り札の前のターンに、カウンターされる呪文を唱えない | プロ（Luis Scott-Vargas） | LSV1 |
| カウンターの多い対戦ほど土地を置き続ける | プロ（Luis Scott-Vargas） | LSV1 |
| カウンター相手には、1ターンに2つ唱えるか、相手のエンドに1つ唱えてから自分のターンにもう1つ唱える | プロ（Reid Duke） | RD9 |
| 自分の位置が悪いほどカウンターを避けるプレイをしない。負けているときは唱えて相手が持っていないことに賭ける | プロ（Reid Duke） | RD10 |
| 相手のカウンターを誘うために、本命の前に別の呪文を唱える | Gemini | `notes/sources/gemini_dengeki_2026-10-31.md` |

### 相手の手札の読みとブラフ

| 知見 | 根拠 | 出典 |
|---|---|---|
| 相手の行動の理由を考える。1ターン目に基本土地を置いたなら、タップインの土地を持っていない可能性が高い | プロ（Reid Duke） | RD5 |
| 相手が除去を撃てる機会に撃たなかったなら、持っている可能性は下がる。手札を多く持ってマナを残してパスしたら、インスタントの可能性が上がる | プロ（Reid Duke） | RD9 |
| 相手が除去を持っていそうなら、弱い脅威から出す（相手がキープし、2ターン目にアンタップの土地を置き、2マナ域を出さなかったことから除去を読んだ例） | プロ（Frank Karsten） | FK3 |
| 一度ケアしたカードは次のターンもケアする | プロ（Reid Duke） | RD9 |
| 相手のデッキに入っていると知っているカードだけをケアする。ブラフで土地を手札に残すのはたいてい誤り | プロ（Jacob Nagro） | JN1 |
| 土地を複数枚手札に残すと、ほとんど損なく相手を慎重にさせられる。最後の1枚は次のターンのために残す | プロ（Gavin Verhey） | GV2 |
| ブラフが成功しやすいのは自分が不利なときか相手が有利なとき。何も無いときに毎回何もしないと読まれるので、ときどき行動を変える | プロ（金子真実、塚本） | KT2 |
| 投了しない。いつも最後まで相手に呪文を唱えさせれば、本当に何か持っているときに読まれにくい | プロ（Reid Duke） | RD5 |

## 9. マナと手順

| 知見 | 根拠 | 出典 |
|---|---|---|
| アンタップしてドローしたら止まり、そのターンにすることを全部決めてから動く。途中で止まって考えると相手に情報を渡す | プロ（Reid Duke。Jon FinkelとPVDDRの方法として紹介） | RD8 |
| 自分に情報をくれる行動と相手に判断を迫る行動は早く、相手に情報を渡す行動は後にする | プロ（Reid Duke） | RD8 |
| 速攻や関係する能力の無いクリーチャーは、攻撃の後に唱える | プロ（Reid Duke） | RD8 |
| 土地は普通は戦闘後に置いて情報を隠す。戦闘前に置くとトリックを持っているように見せられる場面もある | プロ（Reid Duke） | RD8 |
| タップインの土地は、土地の枚数を参照するカードが無い限り戦闘後に置く | プロ（Jacob Nagro） | JN1 |
| 3ターン目にアンタップのショックランドで2マナを残すと、2マナのインスタントを構えていると相手に伝わる | プロ（Jacob Nagro） | JN1 |
| 土地は「このターンにしたいことを諦めずに、先のターンのマナを最大にする」順で置く。1ターン目に唱えるものが無ければ、タップインの土地やショックランドをタップ状態で置く | プロ（Gavin Verhey） | GV1 |
| ファストランドは序盤に先に置き、2枚目もアンタップで出せる順にする | プロ（Gavin Verhey） | GV1 |
| ダブルシンボルの呪文に要る色の土地を先に置く。置く色で別のデッキに見せることもある | プロ（Gavin Verhey） | GV1 |
| 置く土地の順番は手札だけでなく、次に引きうるカードも考えて決める。タップインの土地は2ターン目に置かず、1ターン目か3ターン目に置く | プロ（Handy） | HA1 |
| 黒の1マナ呪文を多く使うデッキでは、2枚目の黒の源を1枚目の赤の源より優先する | プロ（Handy） | HA1 |
| 1ターン目にタップイン、2ターン目に強迫とタップインのように、アンタップの土地を中盤のために残す | プロ（Reid Duke） | RD8 |
| 4ターン目に重要な呪文を撃つなら、4枚目の土地がアンタップで出るように計画する。1〜3ターン目のプレイを1つ諦めてもよい | プロ（Reid Duke） | RD8 |
| マナを使い切る。3マナで2マナ域と3マナ域があるなら3マナ域を唱え、2マナ域は後で2つ同時に唱える機会に使う | プロ（Reid Duke） | RD8 |
| 占術は情報が多いほど正しく判断できるので、ドローしてから占術ランドを置く | プロ（Reid Duke） | RD8 |
| 全体除去が来そうなターンは非クリーチャーの脅威を使い、一番強い脅威は全体除去の後に取っておく | プロ（Reid Duke） | RD10 |
| G1で相手のデッキが分からないときは、自分のデッキの正体を見せない手順を選ぶ | Gemini | `notes/sources/gemini_dengeki_2026-10-31.md` |
| 追加のマナを要求する打ち消しがある相手には、本命を1ターン遅らせて余分なマナを残して唱える | Gemini | `notes/sources/gemini_dengeki_2026-10-31.md` |

## 10. 操作と時間

| 知見 | 根拠 | 出典 |
|---|---|---|
| ArenaではCtrlでそのターンだけフルコントロール、Ctrl+Shiftで維持する。インスタントの有無を相手に知られにくくなるが、操作の多いデッキでは時間切れのおそれがある | プロ（茂里憲之、2022-03時点の挙動） | MO2 |
| メイン1とエンドにフェイズストップを入れると、いつでも使えるアクションを持っているように見せられる | プロ（茂里憲之） | MO2 |
| 相手ターンの開始時にEnterを押しておくと、相手がクリーチャーを唱えたときだけ止まってインスタントの除去を使える | プロ（茂里憲之） | MO2 |
| Arenaでは自分の手札を隠すためにストップを余分に入れる | プロ（Reid Duke） | RD5 |
| ArenaとMTGOでは手早くプレイする習慣がつきやすい。土地を置いてすぐクリーチャーを唱えて攻撃に進まず、正しい順番を守る | プロ（Reid Duke） | RD8 |
| 紙の大会で投了する理由になるのは時計の時間を節約することだけ。オンラインでは投了の時間の得はほとんど無い | プロ（Reid Duke） | RD10 |

---

# アーカイブ

判断にそのまま使わない知見。理由ごとに分けた。

## A. ほかのフォーマットや特定の環境だけの話

| 知見 | 根拠 | 出典 |
|---|---|---|
| 一番の練習は大会（グランプリ）に出ること。一人回しの調整はほとんどしない（2015年時点） | プロ（八十岡翔太） | Y2 |
| マジックの基礎（盤面の判断、マリガン、戦闘）はリミテッドで身につく。戦闘の上達にはリミテッドを多く遊ぶ | プロ（八十岡翔太、佐藤レイ） | Y2、SR1 |
| カードプールが広い環境ほど1マナ域の選択肢が増えてアグロが強くなる | プロ（八十岡翔太） | Y1 |
| GPの参加者は直前でデッキの構成をあまり変えない | プロ（原根健太、GP静岡2018） | H2 |
| 赤黒にだけ負けて残りに勝つデッキを選んだ（相性の偏ったデッキを選ぶ考え方） | プロ（行弘賢、2018年） | YU1 |
| 候補を消していった結果、使い慣れていない緑単信心を選び、ケアレスミスが多かった | プロ（中村修平） | NK1 |
| 環境初期は能動的なデッキを優先する。アグロでは1マナのクリーチャーを多く入れる | プロ（Lucas Esper Berthoud） | LB1 |
| Inquisition of Kozilekは思考囲いより先に撃つ。Serum Visionsはほかのキャントリップの後に唱える（モダン） | プロ（Ari Lax） | AL1 |
| Hieroglyphic Illuminationをサイクリングしてからカウンターを唱える | プロ（Reid Duke） | RD8 |
| レガシーの技術: 脳みそ揉みの後にフェッチでシャッフルする、目くらましに備えて1マナ残す、不毛の大地の起動に対応してフェッチを切る、選定された平和の番人の指定、チャリスのX=0、金属モックスの刻印の選び方 | Gemini | `notes/sources/gemini_dengeki_2026-10-31.md` |

## B. 古いルールの技術

| 知見 | 根拠 | 出典 |
|---|---|---|
| 戦闘ダメージをスタックに乗せた後に起動型能力を使う、当て逃げ | Gemini（表自身が「現行ルールでは不可」と書いている） | `notes/sources/gemini_dengeki_2026-10-31.md` |

## C. 出典を確かめられなかったもの

| 知見 | 状態 | 出典 |
|---|---|---|
| 除去と1対1交換になるカードを外し、1対2の交換を取り続ける構成にする（高橋優太） | 検索要約のみ | `notes/sources/pro_thinking.md` |
| 色マナ源の枚数の古い記事、土地の枚数の記事（Frank Karsten）、「Your land count is too low!」（Reid Duke） | 旧サイトで開けなかった | `notes/sources/pro_thinking_lower.md` |
| Next Level Deckbuildingの原則（Patrick Chapin） | 目次のみ | `notes/sources/pro_thinking.md` |
| 「プレイに上手いも下手もなく、あるのはたった1つの正解だけ」（Jon Finkel） | 原根健太の記憶による引用。原文未確認 | H4 |
| テストを続けても真実に近づかなくなる点がある（Jon Finkel） | 検索要約のみ | `notes/sources/pro_thinking.md` |
| SBで入れ替えすぎてメインの戦略を損なう失敗（Reid Duke） | 第三者の記事の検索要約のみ | `notes/sources/pro_thinking.md` |
| 同じくらいのレベルの相手と練習する（渡辺雄也） | MTG Wikiの記載のみ | `notes/sources/pro_thinking.md` |
| 構えるタイプのデッキでは後手のほうがよいことがある（渡辺雄也、リミテッド） | 検索要約のみ | `notes/sources/pro_thinking_lower.md` |
| 大きな攻撃の後で切り札を唱えずに優先権を渡し、相手に先に対応を使わせた（PVDDR） | Reid Dukeの解説による二次 | `notes/sources/pro_thinking_lower.md` |
| 紙の大会は50分と5ターンの延長、Arena Championshipの持ち時間30分 | 検索要約のみ | `notes/sources/pro_thinking_lower.md` |
| 「電撃」シリーズで示されているとされる内容全般 | Geminiの出典に動画が無い | `notes/sources/gemini_dengeki_2026-10-31.md` |

## D. 実績の確かめられない書き手のもの

| 知見 | 書き手 | 出典 |
|---|---|---|
| ショックランドはできる限りタップインで置く。2ターン目にショックランドをアンタップで置くとカウンターが透ける。カードを構えたいときこそ基本土地をそのまま置く | 富田峻太郎（大きな成績は無いと本人が書いている） | `notes/sources/pro_thinking_lower.md` |
| 50分には相手とシャッフルの時間も入る。方針を先に決めて選択肢を減らす | しょ〜た（N）（実績の記載なし） | `notes/sources/pro_thinking_lower.md` |
| Arenaで相手が時間切れに見えるときは自分の回線切れのことがある | lilium（実績の記載なし） | `notes/sources/pro_thinking_lower.md` |

## E. 個人の経験談や好み

| 知見 | 根拠 | 出典 |
|---|---|---|
| コントロールを自分だけ使って勝てる環境が一番好き。シミックフラッシュは使い手の腕で強さが50から100まで変わる | プロ（八十岡翔太） | Y4 |
| デッキ選択の理由を「メタが読めなかった」と説明したが、本当の理由はカードの入手費用だった | プロ（八十岡翔太） | `notes/sources/pro_thinking.md` 0章 |
| 環境に合っていないと思いつつ、楽しかったのでそのデッキを使った | プロ（原根健太） | H1 |
| チームのリストと勝率データを信頼して、練習で使っていないデッキを7回使った | プロ（原根健太） | H3 |
| 100点のプレイがほぼ不可能なデッキでは、細かいミスの差で勝敗が決まる | プロ（八十岡翔太） | Y5 |

## F. 1試合だけの記録（原則にしていない）

| 記録 | 根拠 |
|---|---|
| ドロスの魔神の油カウンターに反応する前に、自分と相手の残りターン数を数える | DB #107 |
| 変態変異（Metamorphic Alteration）を疑似除去として使う | DB #56（Soulflayer期） |
| 対黒単デーモンのG3で先手後手の選択を誤り、攻守が逆になって負けた | DB #111 |
| 対アグロで除去が0枚の手札をマリガンした | DB #28（Soulflayer期） |
| ディミーア・バウンスは、Yorionでパーマネントを使い回す長期戦のデッキ | DB #103 |

---

# 出典一覧

| ID | 書き手 | 記事 | URL |
|---|---|---|---|
| Y1 | 八十岡翔太（インタビュー） | スタンダード環境終盤の考え方（プレイヤーズコンベンション愛知2024） | https://mtg-jp.com/coverage/pcaichi24/article/0037861/ |
| Y2 | 八十岡翔太（インタビュー） | 八十岡翔太インタビュー ～その根源を探る～ 後編（2015-10-15） | https://mtg-jp.com/reading/special/0015807/ |
| Y3 | 八十岡翔太 | 「青黒ドラゴンコントロール」構築録（2015-04-24） | https://mtg-jp.com/reading/special/0014864/ |
| Y4 | 八十岡翔太・行弘賢・覚前輝也・佐藤レイ（インタビュー） | Team Cygames【MCVII】八十岡翔太の2019年（2019-12-14） | https://team-cygames.com/2019/12/14/6338/ |
| Y5 | 八十岡翔太（インタビュー） | Team Cygames【MCⅤ】強いデッキとは？（2019-10-25） | https://team-cygames.com/2019/10/25/6128/ |
| Y6 | 八十岡翔太（インタビュー） | Breaking! Shota Yasooka Joins Hareruya Pros! | https://article.hareruyamtg.com/article/?p=5294 |
| H1 | 原根健太（インタビュー） | チャンピオンズカップファイナル シーズン2ラウンド3 優勝者インタビュー | https://mtg-jp.com/coverage/pcaichi24/article/0037869/ |
| H2 | 原根健太（インタビュー） | デッキテク「地図ミゼット・コントロール」（GP静岡2018） | https://mtg-jp.com/coverage/gpshz18standard/article/0031504/ |
| H3 | 原根健太 | PT名古屋2020優勝レポート（note、2020-02-06） | https://note.com/jsp/n/n0d57a47acc4d |
| H4 | 原根健太（インタビュー） | 速報！原根 健太、Hareruya Prosに加入！！（2015-11-11） | https://article.hareruyamtg.com/article/article_2059/ |
| H5 | 原根健太（インタビュー） | プレイヤーズツアー・名古屋2020 優勝者インタビュー | https://mtg-jp.com/coverage/ptnag20/article/0033776/ |
| H6 | 原根健太（インタビュー） | ゴールド・レベル・プロ、原根 健太インタビュー（2017-07-30） | https://article.hareruyamtg.com/article/article_4412/ |
| PV1 | PVDDR | PV's Playhouse – Tournament Preparation（2009-05-22） | https://articles.starcitygames.com/articles/pvs-playhouse-tournament-preparation/ |
| PV2 | PVDDR | There's More To Sideboarding Than You Think（2019-12-19） | https://articles.starcitygames.com/magic-the-gathering/premium/theres-more-to-sideboarding-than-you-think/ |
| PV3 | PVDDR | PV's Playhouse – Making Decisions in Magic（2010-02-04） | https://articles.starcitygames.com/articles/pvs-playhouse-making-decisions-in-magic/ |
| RD1 | Reid Duke | Choosing Your Deck（2015-06-08） | https://magic.wizards.com/en/articles/archive/level-one/choosing-your-deck-2015-06-08 |
| RD2 | Reid Duke | Sideboard Plans（2015-03-09） | https://magic.wizards.com/en/articles/archive/level-one/sideboard-plans-2015-03-09 |
| RD3 | Reid Duke | Becoming a Better Player（2015-09-28） | https://magic.wizards.com/en/articles/archive/level-one/becoming-better-player-2015-09-28 |
| RD4 | Reid Duke | Play or Draw（2015-03-16） | https://magic.wizards.com/en/news/feature/play-or-draw-2015-03-16 |
| RD5 | Reid Duke | Valuable MTG Tips to Become a Better Player | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ |
| RD6 | Reid Duke | When Should You Mulligan in MTG | https://www.tcgplayer.com/content/article/When-Should-You-Mulligan-in-MTG/3c705b90-2d3c-4143-b37f-fbd657d9c62e/ |
| RD7 | Reid Duke | Everything You Need to Know About Midrange | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Midrange/cb9d19d9-09ba-4739-9b5a-e4914197e786/ |
| RD8 | Reid Duke | Deep Dive: Sequencing | https://www.tcgplayer.com/content/article/Deep-Dive-Sequencing/776349be-d17f-4d9f-8a73-7639b30a9c16/ |
| RD9 | Reid Duke | How to Play Around Cards in MTG | https://www.tcgplayer.com/content/article/How-to-Play-Around-Cards-in-MTG/96459728-597d-46d4-8dcb-5c7a69ea622a/ |
| RD10 | Reid Duke | How to Beat Control Decks | https://www.tcgplayer.com/content/article/How-to-Beat-Control-Decks-Deep-Dive/bdb3f548-4bea-4a29-82d7-9f074279861f/ |
| RD11 | Reid Duke | How to Build a Mana Base in MTG | https://www.tcgplayer.com/content/article/How-to-Build-a-Mana-Base-in-MTG/4b5261eb-8999-49a8-84ea-988c217939b9/ |
| RD12 | Reid Duke | Managing Your Mana Base | https://www.tcgplayer.com/content/article/Managing-Your-Mana-Base-Deep-Dive/817630e3-756a-481c-8042-b2bf1e8bbd10/ |
| RD13 | Reid Duke | Thoughtseize You | https://articles.starcitygames.com/articles/thoughtseize-you/ |
| FK1 | Frank Karsten | How Many Sources Do You Need to Consistently Cast Your Spells? A 2022 Update | https://www.tcgplayer.com/content/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/ |
| FK2 | Frank Karsten | Should You Board Out a Land on the Draw? | https://www.tcgplayer.com/content/article/Should-You-Board-Out-a-Land-on-the-Draw/ce818a66-49fd-4867-9528-77df8d2b4ad2/ |
| FK3 | Frank Karsten | Against Removal, Play Your Weaker Threats First | https://www.tcgplayer.com/content/article/Against-Removal-Play-Your-Weaker-Threats-First-Strategy-Bite/0d5e0b93-3fd1-49fe-be19-418b1ba992f6/ |
| FK4 | Frank Karsten | Metagame Mentor: Pioneer with Tarkir Dragonstorm and FINAL FANTASY | https://magic.gg/news/metagame-mentor-pioneer-with-tarkir-dragonstorm-and-magic-the-gathering-final-fantasy |
| MJ1 | Martin Jůza | The Fastlands Will Make a Huge Impact in Pioneer | https://www.tcgplayer.com/content/article/The-Fastlands-Will-Make-a-Huge-Impact-in-Pioneer-MTG/c1801b7e-e5cc-4872-95ea-27407ae3f885/ |
| MF1 | Mike Flores | Eight Core Principles of Who's the Beatdown | https://articles.starcitygames.com/articles/eight-core-principles-of-whos-the-beatdown/ |
| LSV1 | Luis Scott-Vargas | Everything You Need to Know About Control | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Control/64752fc2-3dbe-4030-8c42-a177cba13388/ |
| SB1 | Sam Black | The Art Of Sideboarding（2014-12-24） | https://articles.starcitygames.com/?p=8625 |
| GV1 | Gavin Verhey | Real Estate Management 101（2017-09-28）。日本語訳: https://mtg-jp.com/reading/bb/0019594/ | https://magic.wizards.com/en/news/feature/real-estate-management-101-2017-09-28 |
| GV2 | Gavin Verhey | Don't Play Lands（2018-10-11） | https://magic.wizards.com/en/news/feature/dont-play-lands-2018-10-11 |
| JN1 | Jacob Nagro（翻訳） | 晴れる屋の翻訳記事 | https://article.hareruyamtg.com/article/22222/ |
| HA1 | Handy | Tips And Tricks For Proper Land Sequencing | https://articles.starcitygames.com/articles/tips-and-tricks-for-proper-land-sequencing/ |
| AL1 | Ari Lax | These Are The Best Cards In Modern, Here's How To Cast Them | https://articles.starcitygames.com/articles/these-are-the-best-cards-in-modern-heres-how-to-cast-them/ |
| MO1 | 茂里憲之 | 先手後手についてのnote | https://note.com/maddogmtg/n/nc8d13bb7e9e2 |
| MO2 | 茂里憲之 | 紙にはないアリーナの技術（2022-03-04） | https://note.com/maddogmtg/n/nb57c30b4dcef |
| TT1 | 高橋優太、津村健志 | 晴れる屋の記事（マリガンの基準） | https://article.hareruyamtg.com/article/article_3020/ |
| KT1 | 金子真実、塚本 | mtg-jp連載（残りターンの数え方） | https://mtg-jp.com/reading/katerumagic/0016657/ |
| KT2 | 金子真実、塚本 | mtg-jp連載（ブラフ） | https://mtg-jp.com/reading/katerumagic/0016850/ |
| KT3 | 金子真実、塚本 | mtg-jp連載（3色の色マナ源） | https://mtg-jp.com/reading/katerumagic/0015170/ |
| SR1 | 佐藤レイ（インタビュー） | mtg-jp.com（ミシックチャンピオンシップ・シカゴ2019） | https://mtg-jp.com/coverage/mfchi19/article/0032850/ |
| IC1 | 市川ユウキ（インタビュー） | 神インタビュー: 市川 ユウキ（2015-09-11） | https://article.hareruyamtg.com/article/article_1852/ |
| NK1 | 中村修平（インタビュー） | デッキテク「緑単信心」（2022-11） | https://mtg-jp.com/coverage/cc22f1/article/0036514/ |
| WY1 | 渡辺雄也（インタビュー） | スタンダード環境を読み解く手掛かり（GP東京2016） | https://mtg-jp.com/coverage/gptok16/article/016928/ |
| WY2 | 渡辺雄也（インタビュー） | プラチナプレイヤーインタビュー（2014-12-21） | https://article.hareruyamtg.com/article/article_237/ |
| YU1 | 行弘賢（インタビュー） | デッキテク「青単アグロ」（2018-09） | https://mtg-jp.com/coverage/jpnats18/article/0031067/ |
| YU2 | 行弘賢（インタビュー） | デッキテク「セレズニア・オーラ」（2022-11） | https://mtg-jp.com/coverage/cc22f1/article/0036519/ |
| LB1 | Lucas Esper Berthoud（翻訳） | 2021年版「デッキ選択と調整」講座（2021-01-08） | https://article.hareruyamtg.com/article/47446/ |
| BN1 | Brad Nelson | The Standard Mailbag!（2015-05-14） | https://articles.starcitygames.com/articles/the-standard-mailbag/ |

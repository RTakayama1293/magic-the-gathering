# トッププロの判断基準の調査（下の層: マナベース、ゲームの入口、ゲームプラン、局面、マナと手順、操作と時間）

最終更新: 2026-10-31（たたき台）

`notes/knowledge_layers.md` で知見が少なかった層4（マナベース）と層6〜10について、トッププロと強豪の記事を集めた。上の層（取り組み方、メタ、デッキ選択、SB）は `notes/pro_thinking.md` にある。

## 調べた範囲

- 期間: 2026-10-31に1回調べた
- 英語: TCGplayer（旧ChannelFireballの記事を含む）、Star City Games、magic.wizards.com、magic.gg。TCGplayerの記事は本文をAPI経由で全文読んだ
- 日本語: article.hareruyamtg.com、mtg-jp.com、本人のnote
- 対象外: YouTube動画の中身（ユーザーがGemini Notebookで調べる）
- 「マナの捻り方」という語を使った記事は、日本語でも見つからなかった。土地の順番やマナの残し方を扱う記事は「land sequencing」「土地の置き方」「土地管理」の語で見つかった
- 根拠の区分: 一次は本人の記事か本人の発言を直接引用した記事（本人の記事の翻訳を含む）。二次は第三者が本人の言動を書いた記事。未読は記事を開けず検索要約だけ読んだもの

### 晴れる屋YouTube「電撃○○」シリーズ

- 正式名: 固定のシリーズ名は見つからなかった。動画タイトルは「プレミで電撃！」「ミスったら電撃！」「死ぬ気で学ぶ電撃モダン」「恐怖の電撃レガシー」のように回ごとに違う。プロがプレイし、ミスプレイをすると罰ゲームで電撃を受ける形式のプレイ講座である
- チャンネル: 晴れる屋 MTG（https://www.youtube.com/@hareruya_mtg ）
- 再生リスト: チャンネルの再生リスト22件の中に、このシリーズ専用のものは無かった。一部の回は「対戦動画」（https://www.youtube.com/playlist?list=PL-HjF9Jl-4X2mQlImFth0xg_32_fp0o1j ）に入っている
- 本数: プレイ講座の形式は11本（2026-10-31にチャンネル内を「電撃」「プレミで電撃」「死ぬ気で学ぶ」「罰ゲーム」で検索して数えた。検索に出ない回があれば増える）。最も古い回は約4年前、最新は13日前
- パイオニアの回は1本: https://www.youtube.com/watch?v=_AIe3TZd3Lg
- 別形式: カード評価が外れたら電撃を受ける回が3本ある（新セットのカード評価。プレイ講座ではない）

| 動画ID | タイトルに書かれたフォーマット |
|---|---|
| ZeSDHNLunW0 | モダン |
| OEZBeSbmJ2c | レガシー |
| _AIe3TZd3Lg | パイオニア |
| YVntxq8sY-c | レガシー |
| ec9E62VZNZI | スタンダード |
| rHwWt-5AGM8 | レガシー（生放送） |
| uQ2WKCXOpXA | FINAL FANTASY（対戦企画） |
| pmDSFQmK_7k | スタンダード |
| agRM_fxvqfI | 記載なし（エスパー御霊vsボロスエネルギー） |
| 5A6a9YdBmXI | 記載なし（ネオブランド） |
| ecRa4bhEf0M | モダン |

URLは `https://www.youtube.com/watch?v=` に動画IDを付けたもの。

---

## 層4 マナベース（土地の枚数、色マナ源の枚数、2色・3色土地の配分）

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| 60枚デッキで呪文を「安定して」唱えるのに要る色マナ源の表を出した。マナ総量Mの呪文を、Mターン目までに土地をM枚引いた条件で89+M%の確率で唱えられることを基準にした。前提の土地は60枚中25枚 | Frank Karsten | https://www.tcgplayer.com/content/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/ | 一次 |
| 上の表の60枚の値の抜粋: C（1マナ色1つ）14、1C 13、2C 12、3C 10、CC 21、1CC 18、2CC 16、3CC 15、CCC 23、1CCC 21 | Frank Karsten | 同上 | 一次 |
| 土地が22〜28枚の60枚デッキなら、上の表をそのまま使ってよい。それより極端に多い・少ない場合は「土地のうち18/25が青」のように比率で考える | Frank Karsten | 同上 | 一次 |
| 多色の呪文は色ごとに必要数を出し、全部に1を足す。例として、パイオニアのラクドスの税血の収穫者（Bloodtithe Harvester）とDreadboreには黒14・赤14・黒か赤22が要る | Frank Karsten | 同上 | 一次 |
| 1ターン目の呪文にはアンタップで出る土地だけを数える。2ターン目以降はタップインの土地も数える | Frank Karsten | 同上 | 一次 |
| タップインの土地の上限の目安は、1マナ域のあるアグロで3枚、1マナ域のないミッドレンジとコントロールで9枚 | Frank Karsten | 同上 | 一次 |
| 2色デッキでは、どちらかの色を選ぶ土地（Pathway、Fabled Passage）を両方の色の源として数えてよい。3色以上で複数の色を濃く要求するデッキでは、選ぶ土地は完全な源として扱えない | Frank Karsten | 同上 | 一次 |
| 探査（delve）などでコストが下がる呪文は、実際にタップすると見込む土地の枚数でコストを置き換えて表を引く（墓地が早く貯まるデッキならMurktide Regentを1UUとして扱う） | Frank Karsten | 同上 | 一次 |
| パイオニアのラクドス・ミッドレンジの例: 思考囲い（Thoughtseize）と致命的な一押し（Fatal Push）のために、1ターン目にアンタップで出る黒マナ源を14枚確保する。黒18・赤16のうち各14枚が1ターン目にアンタップで出ることを目標にした | Frank Karsten | 同上 | 一次 |
| 鏡割りの寓話（Fable of the Mirror-Breaker）の宝物とルーティングを、4枚で「4マナ以上の呪文に対して黒1・赤1の源」と数えた | Frank Karsten | 同上 | 一次 |
| 60枚デッキで4ターン目までに土地4枚を約81〜82%で引く目標なら、G1は25〜26枚、後手なら24枚、先手なら27枚。ほかの条件が同じなら、後手のときは先手より土地を1枚減らしてよい | Frank Karsten | https://www.tcgplayer.com/content/article/Should-You-Board-Out-a-Land-on-the-Draw/ce818a66-49fd-4867-9528-77df8d2b4ad2/ | 一次 |
| 高いカードを足すときと、相手が干渉してこない対面では土地を増やす。リソースを交換し合う長いゲームの対面では土地を減らす。土地を1枚サイドボードに置いておくと調整できる | Frank Karsten | 同上 | 一次 |
| 標準的な構築デッキの土地は25枚。先手で最初の3回の土地を置ける確率が約90%になる。4マナ目を急がないデッキなら22〜23枚でもよい | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Build-a-Mana-Base-in-MTG/4b5261eb-8999-49a8-84ea-988c217939b9/ | 一次 |
| 寓話の入ったデッキでは土地を多めにする。余った土地を寓話の第2章で捨てて引き直せるから | Reid Duke | 同上 | 一次 |
| マナ・クリーチャーなど土地以外のマナ源で土地を減らしてよいが、土地1枚としては数えない | Reid Duke | 同上 | 一次 |
| 呪文を1ターン遅れて唱えるほうが、唱えられないよりよい。だから色を足すより減らすほうを選ぶ。色の要求が厳しいときは、標準のリストよりタップインの2色土地を1〜2枚多く入れる | Reid Duke | 同上 | 一次 |
| ペインランドやショックランドで払うライフは、攻撃的でない相手にも積み重なる。長いゲームで20でなく13になっていることがある | Reid Duke | 同上 | 一次 |
| 基本土地を減らす罰のあるカード（Field of Ruin、Demolition Field、Blood Moon）がある環境では、基本土地を数枚入れる。3枚あればかなり防げ、1枚でも0枚よりずっとよい | Reid Duke | 同上 | 一次 |
| 構築のリストを写したら土地を1〜2枚足す。土地が少なすぎる危険は多すぎる危険よりずっと大きい。足す土地はミシュラランドなど能力のある土地にする | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 色を「この色が出ない土地は入れない」「この色が無い手札はキープしない」「主な色」「副の色」「タッチ」に分けて土地を配分する。主な色が複数あるときは等分する | Reid Duke | https://www.tcgplayer.com/content/article/Managing-Your-Mana-Base-Deep-Dive/817630e3-756a-481c-8042-b2bf1e8bbd10/ | 一次 |
| ドロー・占術は土地の枚数の調整に役立つ。1〜0マナのものは土地の少ない手札をキープさせるが、5マナのドローは土地を減らす理由にならず、むしろ増やす理由になる | Reid Duke | 同上 | 一次 |
| パイオニアのファストランドは、序盤に展開する2色デッキ（思考囲いや致命的な一押しを使うデッキを含む）に入れる。主な呪文が4マナ以上のコントロールには向かない | Martin Jůza | https://www.tcgplayer.com/content/article/The-Fastlands-Will-Make-a-Huge-Impact-in-Pioneer-MTG/c1801b7e-e5cc-4872-95ea-27407ae3f885/ | 一次 |
| 闇滑りの岸（Darkslick Shores）は1ターン目に置いて、相手の1ターン目を見てからConsiderか致命的な一押しを選べる。Dig Through Timeなど重い呪文の多いディミーアでは入れすぎない | Martin Jůza | 同上 | 一次 |
| ラクドスでは、アンタップで出る土地がすでに十分あるので、硫黄泉（Sulfurous Springs）よりHaunted Ridgeを選ぶ | Martin Jůza | 同上 | 一次 |
| 始まりの町（Starting Town）は、3色のアグロやコンボデッキの色マナの安定を上げる。2025年7月時点のパイオニアで、FINAL FANTASYから最も多く使われた新カードだった | Frank Karsten | https://magic.gg/news/metagame-mentor-pioneer-with-tarkir-dragonstorm-and-magic-the-gathering-final-fantasy | 一次 |
| 3色デッキで3ターン目に3色すべてを80%でそろえるには、各色15枚の源が要る。複数の色が出る土地はできるだけ入れる。ただしタップイン、ダメージ、特殊地形対策のカードの影響を比べる | 金子真実、塚本（mtg-jp連載） | https://mtg-jp.com/reading/katerumagic/0015170/ | 一次 |
| ショックランドは2点が軽くないので、できる限りタップインで置く。そのため2色以上のデッキでは該当色のショックランドを基本的に4枚入れてよい | 富田峻太郎（元プロ志望の講師。大きな成績は無いと本人が書いている） | https://note.com/kawauso_magic/n/nae8ddc889aea | 一次 |

見つからなかったもの: グリクシス（3色）のパイオニアのマナベースを論じた記事、始まりの町と組むときの基本土地の枚数を論じた記事。Karstenの土地の枚数の記事（How Many Lands Do You Need to Consistently Hit Your Land Drops?）とReid Dukeの「Your land count is too low!」は、リンク先が旧サイトで開けなかった。

## 層6 ゲームの入口（先手後手の選択、マリガン、キープの基準）

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| 迷ったら先手を取る。先手を毎回選んでもめったに誤りにならない。マジックはゼロサムなので、速い相手から先手を奪う意味もある。遅いデッキでも普通は先手を取る | Reid Duke | https://magic.wizards.com/en/news/feature/play-or-draw-2015-03-16 | 一次 |
| 後手を選ぶのは次の4つが全部当てはまるとき: どちらも序盤のテンポで長期の優位を得にくい、どちらかが多くのリソース（土地や色）を要る、マナの総量がどちらの制約にもならない、ゲームが長引く。シールドではよく、構築ではまれに当てはまる | Reid Duke | 同上 | 一次 |
| 先手の有利は「あって55%」で、過大評価されている。後手で先手の理想の動きをなぞると負ける。後手で「マナをきれいに使い切る」を目標にすると負ける。後手の勝ち方はカードの交換で、手札1枚の差を使う | 茂里憲之 | https://note.com/maddogmtg/n/nc8d13bb7e9e2 | 一次 |
| パイオニアは先手の有利が大きいという評判がある。後手でさらにタップインの土地から始めると大きく不利になる | Martin Jůza | https://www.tcgplayer.com/content/article/The-Fastlands-Will-Make-a-Huge-Impact-in-Pioneer-MTG/c1801b7e-e5cc-4872-95ea-27407ae3f885/ | 一次 |
| 後手では、相手の動きをなぞるだけでなく、安い干渉で相手の序盤の優位を消すことに集中する。後手のゲームと、手札が良くないゲームで勝つことが強いプレイヤーとの差になる | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 基本の基準は、土地2〜5枚ならキープ、0・1・6・7枚ならマリガン。迷う手札は最良・最悪・平均の3つの展開を想像して判断する | Reid Duke | https://www.tcgplayer.com/content/article/When-Should-You-Mulligan-in-MTG/3c705b90-2d3c-4143-b37f-fbd657d9c62e/ | 一次 |
| どちらかが速いデッキなら少し厳しくマリガンする。両方遅いデッキなら少し緩くする。コントロールで対アグロなら除去か全体除去、対コンボなら妨害（ハンデス、カウンター、除去）を探す | Reid Duke | 同上 | 一次 |
| 最初のドローで土地を引く確率は50%弱、最初の2ドローで75%弱。最初のドローで土地を引く必要がある手札はキープしない。すぐに土地を何枚も引く必要がある手札もキープしない | Reid Duke | 同上 | 一次 |
| 色が1つ欠けた手札は、残りの色で唱えられる呪文が1枚も無ければマリガンする | Reid Duke | 同上 | 一次 |
| パイオニアのラクドス・ミッドレンジの先手で、土地5枚（Takenuma、Haunted Ridge×2、硫黄泉、沼）と税血の収穫者・鏡割りの寓話の手札はキープする。血トークンと寓話の第2章でアクションを探せる | Reid Duke | 同上 | 一次 |
| 7枚から6枚へは積極的にマリガンし、5枚以下は避ける。2回以上マリガンしたら、勝つ道筋が見えればキープする | Reid Duke | 同上 | 一次 |
| 初手7枚を見たら4ターン先まで想像する。各ターンに動けたら1点と数え、パスするターンがあっても点を稼げるならキープする。後手で2ターン目をパスするのは危ない | 高橋優太 | https://article.hareruyamtg.com/article/article_3020/ | 一次 |
| 2ターン目に動き出せるかが重要。「確定3ターン目スタート」の手札は現代のマジックでは許しにくい。後手の2ターン目パスは、3ターン目以降に2点取れる見込みがあるときだけ許す | 津村健志 | 同上 | 一次 |
| SB後に入れたキーカードの有無はキープの基準になる | 津村健志 | 同上 | 一次 |
| マリガンしたくなる初手が多いなら、デッキの構築を変えて防ぐ。キープできるカードを多く入れる | 津村健志、高橋優太 | 同上 | 一次 |
| ミッドレンジで対コンボの妨害が思考囲い4枚だけなら、思考囲いの価値が大きいのでマリガンの基準に入れる | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Midrange/cb9d19d9-09ba-4739-9b5a-e4914197e786/ | 一次 |
| 構えるタイプのデッキでは後手のほうがよいことがある | 渡辺雄也（リミテッドの文脈） | https://mtg-jp.com/coverage/PTNagoya11/prepost/0000215/ | 未読（検索要約のみ） |

## 層7 ゲームプラン（自分の役割、勝ち筋の選択、勝つ・負ける条件の把握）

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| デッキの役割はビートダウンかコントロールの2つで、相手によって入れ替わる。役割を誤るとゲームを落とす。1999年の記事は、先手で1マナ2点のクリーチャーを並べる相手に自分をビートダウンと誤認したチームメイトの負けが元になった | Mike Flores | https://articles.starcitygames.com/articles/eight-core-principles-of-whos-the-beatdown/ | 一次 |
| 役割は「どちらがダメージを多く出せるか」「どちらが除去を多く持つか」で見分け、決めたら役割に沿って動く。相手が取りたい役割に自分が入って、相手の行動を奪うこともできる | Mike Flores | 同上 | 一次 |
| 同じ終盤の勝ち方を持つデッキ同士では、速いほうが有利になる。現在の位置から長いゲームに勝てる側を「inevitability（最終的な勝ちの保証）」があると呼ぶ（Zvi Mowshowitzの定義） | Mike Flores | 同上 | 一次 |
| 先手は攻撃する理由が多く、後手は1枚多い手札でダメージを防ぐことにマナを使える。先手と後手で戦い方を変える | Mike Flores | 同上 | 一次 |
| 自分の本当の役割を隠すと有利になる。Floresは青のコントロールに見せかけ、相手がタップアウトしたところでコンボで勝った。決勝ラウンドで相手がリストを知っているときは使えない | Mike Flores | 同上 | 一次 |
| 悪い相性とは、自分の役割を完全に崩される相性である。最良のデッキは多くの対面でビートダウンとコントロールの両方を取れる | Mike Flores | 同上 | 一次 |
| ミッドレンジのゲームは2段階で進む。最初は守ってマナを伸ばし、相手の計画を除去で崩す。次に攻めに転じる（turning the corner）。カードはどちらかの段階に役立つものにする | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Midrange/cb9d19d9-09ba-4739-9b5a-e4914197e786/ | 一次 |
| ミッドレンジ対アグロでは、まず守って安定させる。レースに乗ると負ける。安定した後は、バーンで負けないよう早くゲームを終わらせる。相手に与えるドローの回数が増えるほど逆転される | Reid Duke | 同上 | 一次 |
| ミッドレンジ対コンボでは、妨害だけで相手を止められないので、妨害で相手を崩しながら一番強い脅威を早く出す。3ターン目に負けても7ターン目に負けても同じなので、圧力をかけるリスクを取る | Reid Duke | 同上 | 一次 |
| 最終目標（ライフを0にする）より手前の「実質勝ち」を目標にする。リソースで勝つか、ライフを削り切るか、テンポで押し切るかを決める。どうすれば負けないかでなく、どう勝つかを考える | 茂里憲之 | https://note.com/maddogmtg/n/nc8d13bb7e9e2 | 一次 |
| 数ターン後のお互いのライフを予想しながら進める。自分があと何ターン持つかと、相手を倒すまで何ターンかを数える。不利なのに保守的に構えると逆転の目が無くなる | 金子真実、塚本（mtg-jp連載） | https://mtg-jp.com/reading/katerumagic/0016657/ | 一次 |
| 自分が有利か不利かを早く決めつけると、攻めか守りに偏る。局面は毎ターン変わるので、一貫性より柔軟性を取る | 佐藤レイ | https://mtg-jp.com/coverage/mfchi19/article/0032850/ | 一次（インタビュー） |
| 対コントロールでは、相手が望む「ゆっくり進んで脅威に1枚ずつ答えられる」ゲームを避ける。速さで押すか、相手の答えが合わない脅威を出すか、コンボやランプなら自分がinevitabilityを持つ側に回る | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Beat-Control-Decks-Deep-Dive/bdb3f548-4bea-4a29-82d7-9f074279861f/ | 一次 |
| 相手のフィニッシャーで負けたように見えても、本当の負けの理由（序盤の展開を止められ、カード差で埋もれた）を見てSBする | Reid Duke | 同上 | 一次 |
| アグロ・コントロールのデッキでは、どちらの役割を取るかを決め、ゲームが変わるまでその役割を続ける | Luis Scott-Vargas | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Control/64752fc2-3dbe-4030-8c42-a177cba13388/ | 一次 |

## 層8 局面の判断（攻撃とブロック、除去やハンデスの対象、カウンター、ブラフ、相手の手札の読み）

### 攻撃とブロック

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| クリーチャーは戦闘に出して初めて価値がある。たくさん攻撃し、たくさんブロックする。2/2で2/2が殴ってきたらブロックして相打ちにし、相手にコンバット・トリックを使わせる | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 相手がマナを残して攻撃してきても、たいていはブロックしてトリックを使わせる。ブロックしないと、その後のゲーム全体をトリックを恐れて進めることになる。例外はブロッカーが勝ち筋の中心のとき | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Play-Around-Cards-in-MTG/96459728-597d-46d4-8dcb-5c7a69ea622a/ | 一次 |
| 攻撃はキルターン（勝てるターン）を確かめながら決める。攻撃するかは「+2点にどれだけ価値があるか」で決まり、相手のライフと手札の枚数で変わる（相手が手札0・ライフ8なら3体で殴り、ライフ16・手札4枚なら殴らない場面がある） | 佐藤レイ | https://mtg-jp.com/coverage/mfchi19/article/0032850/ | 一次（インタビュー） |
| 戦闘には正しいか誤りかしかない。上達には場数が要り、リミテッドを多く遊ぶ | 佐藤レイ | 同上 | 一次（インタビュー） |
| 生き延びるためや最悪の展開を避けるためでなく、勝つためにプレイする。安全策で数ターン先の負けを増やすなら、その安全策は取らない | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |

### 除去・ハンデスの対象と使う時期

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| 思考囲いでは、まず相手の手札の穴（たとえば場に出た脅威への答えが無いこと）を作るカードを抜く。穴が作れなければ一番強いカードを抜く。マナ加速を抜いて相手を土地事故にしようとしない | Reid Duke | https://articles.starcitygames.com/articles/thoughtseize-you/ | 一次 |
| 相手が唱える脅威が問題なら、思考囲いは脅威を止められる範囲でできるだけ遅く撃つ。カウンターなど相手の対応カードが問題なら、自分の重要な呪文を通す前のターンか、その呪文を唱えるターンに撃つ | Reid Duke | 同上 | 一次 |
| 特定の目的が無いなら、クリーチャーやタップインの土地のような時期の決まったプレイを先にし、思考囲いは空いたときに撃つ。1ターン目に撃つのは理由が無ければたいてい誤り | Reid Duke | 同上 | 一次 |
| 思考囲いの優先順位: 相手の一番良いカード、それを止められなければ相手のマナカーブ、自分の脅威に合う相手の答え。単一の重いコンボパーツが無い相手には早く撃つ。Inquisition of Kozilekは思考囲いより先に撃つ | Ari Lax | https://articles.starcitygames.com/articles/these-are-the-best-cards-in-modern-heres-how-to-cast-them/ | 一次 |
| ハンデスは、相手が強い行動を先に取れないようにし、自分の後のターンをタップアウトできるようにする（強迫が構えずに使えるのがミッドレンジに向く理由） | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Midrange/cb9d19d9-09ba-4739-9b5a-e4914197e786/ | 一次 |
| 除去は相手のクリーチャーに対して合う順に使う（軽い除去を小さいクリーチャーに、重い除去を大きいクリーチャーに）。置いておくと得をし続けるカード、たとえばThe Great Hengeがあれば、すぐ除去する | Luis Scott-Vargas | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Control/64752fc2-3dbe-4030-8c42-a177cba13388/ | 一次 |
| 序盤の除去は、相手の最初の展開を止めて後れを取らないために使う（「bolt the bird」）。相手の除去が多いときは、弱いカードから先に出して除去を使わせる | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Sequencing/776349be-d17f-4d9f-8a73-7639b30a9c16/ | 一次 |

### カウンター、パーミッションへの対処

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| カウンター中心のデッキは自分の脅威を「なるべく出さない」か、とても遅く出す。タップアウト型は出せるマナがあり次第出す | Luis Scott-Vargas | https://www.tcgplayer.com/content/article/Deep-Dive-Everything-You-Need-to-Know-About-Control/64752fc2-3dbe-4030-8c42-a177cba13388/ | 一次 |
| 相手のカウンターに対しては、相手が別の強い行動（ドロー呪文など）にマナを使いたいターンに重要な呪文を唱える。相手の切り札の前のターンにカウンターされる呪文を唱えない | Luis Scott-Vargas | 同上 | 一次 |
| 脅威をタップアウトで出してカウンターされると、相手は自分の脅威を通す。カウンターの多い対戦ほど土地を置き続けることが大事になる | Luis Scott-Vargas | 同上 | 一次 |
| 自分の位置が悪いほど、パーミッションを避けるプレイをしない。負けているときは呪文を唱えて相手が持っていないことに賭ける。有利か互角なら、相手のマナの使い方を不便にする | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Beat-Control-Decks-Deep-Dive/bdb3f548-4bea-4a29-82d7-9f074279861f/ | 一次 |
| カウンター相手に一番悪いのは、毎ターン1枚ずつソーサリーのタイミングで唱えること。1ターンに2つ唱えるか、相手のエンドに1つ唱えてから自分のターンにもう1つ唱える | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Play-Around-Cards-in-MTG/96459728-597d-46d4-8dcb-5c7a69ea622a/ | 一次 |
| 相手が2ターン目のランプ呪文をカウンターしなかったなら、序盤に使うべきカウンター、たとえばCensorを持っている証拠は弱い。4ターン目まで双方が何もしていないなら、カウンターを考える。一度ケアしたカードは次のターンもケアする | Reid Duke | 同上 | 一次 |
| 全体除去を恐れて展開しすぎないと、単体除去とブロッカーで負けることがある。迷ったら呪文を唱えて相手に答えを要求する | Reid Duke | 同上 | 一次 |

### ブラフと相手の手札の読み

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| 相手の行動の理由を考える。1ターン目に基本土地を置いたなら、タップインの土地を持っていない可能性が高く、土地の多い手札でない可能性も高い | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 相手が除去を撃てる機会に撃たなかったなら、除去を持っている可能性は下がる。相手が手札を多く持ってマナを残してパスしたら、インスタントの可能性が上がる | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Play-Around-Cards-in-MTG/96459728-597d-46d4-8dcb-5c7a69ea622a/ | 一次 |
| 相手が除去を持っていそうなら、弱い脅威から出す。判断に使う問いは3つ: 相手のここまでのプレイから除去やカウンターを持つ可能性はどれくらいか、持っているなら答えられて一番困らない脅威はどれか、除去を避けるとその後の展開を妨げるか。例として、相手がキープし、2ターン目にアンタップの土地を置き、2マナ域を出さなかったことから除去を読んだ | Frank Karsten | https://www.tcgplayer.com/content/article/Against-Removal-Play-Your-Weaker-Threats-First-Strategy-Bite/0d5e0b93-3fd1-49fe-be19-418b1ba992f6/ | 一次 |
| PVDDRは、大きな攻撃の後でEmbercleaveを唱えずに優先権を渡し、相手にAether Gustを先に使わせてからEmbercleaveで勝った。相手がマナを残して除去を持っていそうなら、先に動かせる | PVDDR（Reid Dukeが試合映像を解説） | https://www.tcgplayer.com/content/article/Deep-Dive-Believe-in-the-Embercleave/4166ce3a-1968-4bdb-9982-5a09c25b4177/ | 二次 |
| 相手のサイドボーディングを決めつけない。予想はするが、不確かさを残して動く | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| ブラフは失敗するリスクのある行動で、プロでも意見が分かれる。成功しやすいのは自分が不利なときか相手が有利なとき。何も無いときに毎回何もしないと手札を読まれるので、ときどき行動を変える | 金子真実、塚本（mtg-jp連載） | https://mtg-jp.com/reading/katerumagic/0016850/ | 一次 |
| ブラフで土地を手札に残すのはたいてい誤りで、相手の行動はあまり変わらない。相手のデッキに入っていると知っているカードだけをケアする | Jacob Nagro | https://article.hareruyamtg.com/article/22222/ | 一次（翻訳） |
| 土地を複数枚手札に残すと、ほとんど損なく相手を慎重にさせられる。最後の1枚の土地は、次のターンに要る呪文を引いたときのために残す | Gavin Verhey | https://magic.wizards.com/en/news/feature/dont-play-lands-2018-10-11 | 一次 |
| 本当に持っているカードを強く意識させるのは手札を見せるのと同じ不利益になる。カードを構えたいときこそ、基本土地をそのまま置く | 富田峻太郎 | https://note.com/kawauso_magic/n/nae8ddc889aea | 一次 |
| 自分の本当の役割（デッキの正体）を隠すと有利になる | Mike Flores | https://articles.starcitygames.com/articles/eight-core-principles-of-whos-the-beatdown/ | 一次 |
| 投了しない。投了すれば勝率は0になる。いつも相手に最後まで呪文を唱えさせれば、本当に何か持っているときに読まれにくくなる | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |

## 層9 マナと手順（土地を置く順番、タップする土地、呪文の順番、構えるマナ、フェッチやサーチの時期、情報を隠す手順）

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| 自分のターンは、アンタップしてドローしたら止まり、そのターンにすることを全部考えてから動く。どの土地を置くか、何で攻撃するか、何を唱えるか、相手の予想できる対応にどう返すかを先に決める。途中で止まって考えると相手に情報を渡す | Reid Duke（Jon FinkelとPVDDRがしている方法として紹介） | https://www.tcgplayer.com/content/article/Deep-Dive-Sequencing/776349be-d17f-4d9f-8a73-7639b30a9c16/ | 一次 |
| 自分に情報をくれる行動と相手に判断を迫る行動はターンの早いうちに、相手に情報を渡す行動と自分が判断を迫られる行動は後にする | Reid Duke | 同上 | 一次 |
| 速攻や関係する能力の無いクリーチャーは、攻撃の後に唱える。先に唱えると、相手のブロックや除去の判断に情報を渡す | Reid Duke | 同上 | 一次 |
| 土地は普通は戦闘後に置いて情報を隠す。ただし戦闘前に土地を置くとトリックを持っているように見せられるので、戦闘前に置くほうが情報を隠せる場面もある（手札にEmbercleaveが無いことを見せない例） | Reid Duke | 同上 | 一次 |
| 占術は情報が多いほど正しく判断できるので、ドローしてから占術ランドを置く | Reid Duke | 同上 | 一次 |
| 対全体除去のデッキで4ターン目に全体除去を撃つなら、4枚目の土地がアンタップで出るように計画する。1〜3ターン目のプレイを1つ諦めてもよい | Reid Duke | 同上 | 一次 |
| 「沼＋強迫」を1ターン目にして2ターン目がタップイン土地だけになるより、1ターン目にタップイン土地、2ターン目に強迫とタップイン土地を置いて、アンタップの土地を中盤のために残す | Reid Duke | 同上 | 一次 |
| マナを使い切る。3マナで2マナ域と3マナ域があるなら3マナ域を唱え、2マナ域は後で2つ同時に唱える機会に使う | Reid Duke | 同上 | 一次 |
| 呪文を唱える前と後のどちらで攻撃するか、Brainstormの前と後のどちらで土地を置くか、どの土地を置くか、フェッチをいつ切るかは小さい判断だが、ときどき勝敗を分ける。土地を置く順番に注意を払う | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 土地は「このターンにしたいことを諦めずに、先のターンのマナを最大にするにはどうするか」で選ぶ。1ターン目に唱えるものが無ければ、タップインの土地やショックランドをタップ状態で置き、ライフ2点を払わずに済ませる | Gavin Verhey | https://magic.wizards.com/en/news/feature/real-estate-management-101-2017-09-28 | 一次 |
| 序盤だけアンタップで出る土地（ファストランドのCopperline Gorge）を先に置き、2枚目のファストランドもアンタップで出せる順にする | Gavin Verhey | 同上 | 一次 |
| ダブルシンボルの呪文や起動型能力に要る色の土地を先に置く。青赤コントロールでも山を先に置いて赤のアグロに見せることがある | Gavin Verhey | 同上 | 一次 |
| 同じ内容の日本語訳: 実践土地管理・基礎編 | Gavin Verhey（翻訳） | https://mtg-jp.com/reading/bb/0019594/ | 一次（翻訳） |
| 土地は「置くか」「どれを置くか」「いつ置くか」を考える。タップインの土地を置くなら、土地の枚数を参照するカードが無い限り、戦闘後に置くのがほぼ毎回正しい | Jacob Nagro | https://article.hareruyamtg.com/article/22222/ | 一次（翻訳） |
| 3ターン目にアンタップの神聖なる泉で2マナを残すと「2マナのインスタントを構えている」と相手に伝えることになる | Jacob Nagro（Cedric Phillipsの例として） | 同上 | 一次（翻訳） |
| 置く土地の順番は手札だけでなく、次に引きうるカードも考えて決める。タップインの土地、たとえばPrairie Streamは2ターン目に置かず、1ターン目か3ターン目に置く | Handy（署名はCarmen Handy、本文の紹介はEmma Handy） | https://articles.starcitygames.com/articles/tips-and-tricks-for-proper-land-sequencing/ | 一次 |
| 黒の1マナ呪文を多く使うデッキでは、2枚目の黒の源を1枚目の赤の源より優先して持ってくる | Handy（同上） | 同上 | 一次 |
| 2ターン目にショックランドをアンタップで置くと手札のカウンターが透けるので、3ターン目に基本土地を置く順にする | 富田峻太郎 | https://note.com/kawauso_magic/n/nae8ddc889aea | 一次 |
| フェッチランドは本当に必要なときだけ起動する（寓話の小道の説明として） | 富田峻太郎 | 同上 | 一次 |
| 除去が使われそうなら、一番強い呪文でなく弱い脅威を先に唱える（マナ効率の原則の例外） | Frank Karsten | https://www.tcgplayer.com/content/article/Against-Removal-Play-Your-Weaker-Threats-First-Strategy-Bite/0d5e0b93-3fd1-49fe-be19-418b1ba992f6/ | 一次 |
| 全体除去が来そうなターンは非クリーチャーの脅威やミシュラランドを使い、一番強い脅威は全体除去の後の立て直しに取っておく | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Beat-Control-Decks-Deep-Dive/bdb3f548-4bea-4a29-82d7-9f074279861f/ | 一次 |
| Serum Visionsは同じターンのほかのキャントリップの後に唱え、フェッチでシャッフルする予定があるなら唱えない | Ari Lax | https://articles.starcitygames.com/articles/these-are-the-best-cards-in-modern-heres-how-to-cast-them/ | 一次 |
| ドロー呪文のHieroglyphic Illuminationをサイクリングしてからカウンターを唱えると、別のカウンターを引けたときに選び直せ、相手に手札の情報も渡さない | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Sequencing/776349be-d17f-4d9f-8a73-7639b30a9c16/ | 一次 |

## 層10 操作と時間（Arenaの操作、タイマー、紙の大会での時間）

| 知見 | 誰 | 出典URL | 区分 |
|---|---|---|---|
| ArenaではCtrlでそのターンだけフルコントロール、Ctrl+Shiftでターンをまたいで維持する。フルコントロールにすると、インスタントを持っているかどうかを相手に知られにくくなる。毎ターン約7回パスが要るので、操作の多いデッキでは時間切れのおそれがある | 茂里憲之 | https://note.com/maddogmtg/n/nb57c30b4dcef | 一次 |
| フェイズストップ: メイン1とエンドで止めると、いつでも使えるアクションを持っているように見せられる。メインで土地を置いた後に止めると、フラッシュのクリーチャーを持っていないことを隠せる | 茂里憲之 | 同上 | 一次 |
| 相手ターンの開始時にEnter（対応できる機会まで自動でパス）を押しておくと、相手のメイン2移行では止まらず、クリーチャーを唱えられたときだけ止まってインスタントの除去を使える | 茂里憲之 | 同上 | 一次 |
| Shift+Enterはターン終了まで全部パスする。相手のエンドにストップを入れてからShift+Enterを押すと、メインでは止まらずエンドで優先権を得られる | 茂里憲之 | 同上 | 一次 |
| 茂里の記事の挙動は2022-03-04時点で、更新で変わる可能性があると本人が書いている | 茂里憲之 | 同上 | 一次 |
| Arenaでは、相手が優先権を得ているか得ていないかに注意する。自分の手札を隠すためにストップを余分に入れる。MTGOでも、F6で早く進めるためにクリーチャーを先に唱える順にせず、攻撃してから唱える | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| ArenaとMTGOは手早くプレイする悪い習慣を作る。土地を置いてすぐクリーチャーを唱え、攻撃に進めるのをやめ、正しい順番を守る習慣をつける | Reid Duke | https://www.tcgplayer.com/content/article/Deep-Dive-Sequencing/776349be-d17f-4d9f-8a73-7639b30a9c16/ | 一次 |
| 相手のターン中も考える。相手の時間を使って次の自分の行動を決め、相手のプレイから情報を拾う | Reid Duke | https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ | 一次 |
| 紙の大会で投了する理由になるのは時計の時間を節約することだけ。オンラインでは相手のチェスクロックのほうが多く減るので、投了の時間の得はほとんど無い。投了するのは、逆転がほぼ無く、ゲームが長くかかり、次のゲームのほうが学べるときに限る | Reid Duke | https://www.tcgplayer.com/content/article/How-to-Beat-Control-Decks-Deep-Dive/bdb3f548-4bea-4a29-82d7-9f074279861f/ | 一次 |
| 50分には相手の時間とシャッフルの時間も入る。ゲームの方針を先に決めて選択肢を減らす。価値が同じ選択肢で迷い続けない。予想から大きく外れたときだけ長考する。相手の手番中に、相手の行動ごとの対応を決めておく | しょ〜た（N）（実績の記載なし） | https://note.com/shot_a33/n/n6ceca789f077 | 一次 |
| Arenaで相手が時間切れに見えるときは自分の回線切れのことがある。Ctrlでフルコントロールに入れなければ自分の回線を疑って再起動する | lilium（実績の記載なし） | https://note.com/lilium761/n/na91537f98b57 | 一次 |
| 紙の大会のラウンドは50分で、時間切れの後に5ターンの延長があり、決着しなければ引き分けになる。意図的な遅延は禁止されている | 公式規定の要約 | https://magic.gg/news/world-championship-32-fact-sheet-for-competitors | 未読（検索要約のみ） |
| Arena ChampionshipのDirect Challengeでは、クライアントが30分の持ち時間を管理する | 公式の要項 | https://magic.gg/news/arena-championship-13-fact-sheet-for-competitors | 未読（検索要約のみ） |

見つからなかったもの: トッププロが紙の大会での時間配分を正面から論じた記事、Arenaのタイマー（ロープ）の使い方を論じたプロの記事。

---

## Archfiend Alterationと魂剥ぎに直接当てはまる知見

この節の「当てはめ方」はすべてClaudeの推論で、戦績DBで確かめていない。デッキリストは `decks/archfiend_alteration_v0.md`（v0.1）から取った。リストのExclusive Nightclub 1枚は、オズコープ社（Oscorp Industries）のArenaでの名前で、タップインで{U}{B}{R}のどれかを出す（`oracle/cards.csv`）。最初の版ではこの1枚を数え漏らしていたので、2026-10-31にメインが下の数を直した。

| 知見（出典の主張） | 誰・出典 | 当てはめ方（Claudeの推論） |
|---|---|---|
| 1マナの色呪文を1ターン目に唱えるには、アンタップで出る源が14枚要る | Karsten（層4） | 思考囲い4枚と致命的な一押し4枚のために、1ターン目にアンタップで出る黒の源を数えると、Blood Crypt 4、Watery Grave 4、硫黄泉2、黒割れの崖3、闇滑りの岸1、目玉の暴君の住処1、始まりの町2、Swamp 1の18枚になり、14枚を上回る |
| 1CCCは21枚、2CCは16枚 | Karsten（層4） | 鏡に願いを（Beseech the Mirror、1BBB）は黒21枚、ドロスの魔神（Archfiend of the Dross、2BB）は黒16枚が目安になる。2ターン目以降はタップインも数えるので、上の18枚に難破船の湿地3、ザンダーの居室1、オズコープ社1を足すと黒は23枚で、21枚を上回る |
| 多色の呪文は各色の必要数に1を足す。2Cは12枚、1Cは13枚 | Karsten（層4） | マナコストがBRの税血の収穫者は黒14・赤14が目安。赤の源はBlood Crypt 4、Steam Vents 2、硫黄泉2、黒割れの崖3、ザンダーの居室1、オズコープ社1、始まりの町2の15枚で、目安の14枚を上回る。変態変異（Metamorphic Alteration、1U）の青13枚は、Watery Grave 4、Steam Vents 2、難破船の湿地3、闇滑りの岸1、ザンダーの居室1、オズコープ社1、始まりの町2の14枚で、目安の13枚を上回る。始まりの町を各色の完全な源として数えたのはClaudeの判断で、Karstenは始まりの町を扱っていない |
| 1マナ域のあるデッキはタップインの土地を少なくする（アグロで3枚、1マナ域の無いミッドレンジで9枚） | Karsten（層4） | このデッキは1マナ域があるミッドレンジで、Karstenの2つの目安の間に入る。1ターン目に必ずタップインになる土地は難破船の湿地3、ザンダーの居室1、オズコープ社1の5枚 |
| 序盤だけアンタップで出る土地を先に置く | Verhey（層9） | 始まりの町（3ターン目まで）、ファストランド（他の土地が2枚以下のとき）、目玉の暴君の住処（他の土地が1枚以下のとき）は序盤に置き、難破船の湿地（他の土地が2枚以上でアンタップ）は3枚目以降に回す順が、この原則に沿う |
| 1ターン目にタップイン、2ターン目に強迫とタップインの順で、アンタップの土地を中盤に残す | Reid Duke（層9） | 思考囲いを1ターン目に撃たずに、1ターン目にショックランドをタップ状態で置く手順に当たる。Reid Dukeの思考囲いの記事も、理由が無ければ1ターン目に撃つのはたいてい誤りとしている |
| 対応カード（カウンター）が問題なら、思考囲いは重要な呪文を通す前のターンか、その呪文を唱えるターンに撃つ。妨害を貯めてから一気に勝ちの手段を通す。LSVの例は思考囲いからBolas's Citadelを通す手順 | Reid Duke、LSV（層8） | 変態変異でドロスの魔神をコピーするコンボを通すターンの直前か同じターンに、思考囲いで相手の除去やカウンターを抜く順に当たる |
| 除去が来そうなら弱い脅威から出す | Karsten（層8・9） | 相手が除去を持っていそうな序盤は、ドロスの魔神より先に税血の収穫者や鏡割りの寓話を出して除去を使わせる判断に当たる |
| 寓話のデッキでは土地を多めにし、余った土地を第2章で捨てる | Reid Duke（層4） | このデッキは寓話4枚で土地25枚。Reid Dukeの基準と同じ側にある |
| パイオニアのラクドス・ミッドレンジの土地5枚と税血の収穫者・寓話の手札はキープ | Reid Duke（層6） | 同じカードを使うこのデッキで、土地の多い手札をキープするときの参考になる |
| ハンデスが対コンボの主な妨害なら、マリガンの基準に入れる | Reid Duke（層6） | 対コンボの対面では、思考囲いの有無をキープの判断材料にすることに当たる |
| 茂里のEnterの手順（相手ターンの開始時に押し、クリーチャーを唱えられたときだけ止まる） | 茂里憲之（層10） | Arenaで致命的な一押しや喉首狙い（Go for the Throat）を構えていることを隠しながら、相手のクリーチャーに撃つ手順に当たる |
| デッキの正体を隠すと有利になる | Flores（層7） | 戦績DBの#102・#105の「相手がこのデッキをライフゲインのデーモンデッキと誤認する」という記録と同じ方向の主張である |
| 墓地を取り合う2枚（Murktide RegentとTarmogoyf）の相性の悪さは細かい例外で、気にしすぎない。どちらも強く同じ型のデッキに入る | Reid Duke（https://www.tcgplayer.com/content/article/Valuable-MTG-Tips-to-Become-a-Better-Player-Deep-Dive/e435c483-2562-40cd-aaf2-1bd4dd92b192/ 、一次） | 魂剥ぎ（Soulflayer）と最後の贈り物の運び手を「墓地を取り合う」と評価したClaudeの誤り（CLAUDE.md）について、ユーザーの方針と同じ方向の主張である |
| 探査の呪文は実際にタップすると見込む土地の数でコストを置き換えて色マナ源を数える | Karsten（層4） | 魂剥ぎ（4BB、探査）は、BBを残したまま総マナを低く見積もって黒の源を数える。何ターン目に何マナで唱えるかの見込みはユーザーの実戦の値で決める |

## 確かめられなかったこと

- 「マナの捻り方」という語の出典: 見つからなかった
- 晴れる屋の電撃シリーズの公式の名前と専用の再生リスト: 見つからなかった。本数はチャンネル内検索で数えたので、検索に出ない回があれば増える
- Mike Floresの1999年の原文「Who's the Beatdown」: 読んでいない。読んだのは2012年のFlores本人による要約の記事「Eight Core Principles」
- Karstenの土地の枚数の記事と、Reid Dukeの「Your land count is too low!」: リンク先の旧サイトが開けず読んでいない
- PVDDR本人のプレイ記事: 今回は見つからなかった。PVDDRの行動は、Reid Dukeの解説（二次）だけ
- 渡辺雄也の先手後手の記事（リミテッド）: 検索要約のみ
- 公式の大会規定（50分、5ターンの延長）とArena Championshipの持ち時間: 検索要約のみ
- 日本のトッププロが書いたカウンターの使い方、除去の対象選び、紙の大会の時間配分の記事: 見つからなかった

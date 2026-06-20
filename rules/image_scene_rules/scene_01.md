# scene_01

## このシーンの役割

scene_01は、Book Base動画の最初の入口。統計・ニュース・調査データをもとにしたクイズを出し、視聴者に「え、どれだろう？」「自分も間違えているかも」と思わせる。答えはこのシーンでは絶対に出さず、問題提起だけにする。

## 画像の目的

- 動画の入口として視聴者の注意を引く。
- クイズ形式で興味を引き、「自分も当てはまりそう」と思わせる。
- 統計・ニュース・調査データ由来の問いであることを伝える。
- 本編テーマへの導線にする。
- 答え・解説・ネタバレは含めない。

## 所属ブロック・重要ポイント

- 所属ブロック：冒頭導入・クイズ・本紹介・重要ポイント提示
- 重要ポイント番号：該当なし
- 20シーン全体の流れの中での位置づけ：各シーン単体ではなく、前後シーンとの接続を踏まえて画像化する。

## 必須条件

- アスペクト比16:9の横長。
- Book Baseらしい動画内画像にする。
- 水彩画風。
- 高級感のある落ち着いた雰囲気。
- 淡いクリーム、ベージュ、ティール、控えめなゴールド系を使う。
- 日本の会社員向けビジネス書YouTubeチャンネルらしい知的な印象にする。
- Book Baseロゴを左下に小さく自然に入れる。
- 長文は載せない。
- 文字数は最小限。
- 1画像1メッセージ。
- scene_02以降と構図が被りにくいようにする。
- クイズの答えは書かない。
- ネタバレしない。

## 表現の方向性

- 視聴者が「どれが正解？」と一瞬で考えたくなる見せ方にする。
- 統計・調査データ・ニュース由来のクイズであることが伝わるようにする。
- ただの黒板クイズではなく、知的で洗練された印象にする。
- クイズのテーマは今回の本の内容に沿わせる。
- 原稿本文から画像用テキストを抽出するときは、固定挨拶、長い出典説明文、テーマ接続文、固定締め文は除き、大見出し用の短いクイズ文、統計ソース表記、数値入りA/B/C選択肢だけを使う。
- 会社員が自分ごと化しやすいテーマにする。

## テキストの方向性

画像内テキストは短く、以下の構成を基本にする。

- 左側の大見出しに短いクイズ文。例：「能力開発・人材育成に問題がある事業所は何％？」
- 大見出しの近くに統計ソース表記。例：「株式会社R&G 2026年調査」「厚生労働省 2025年調査」
- A / B / C の選択肢カードには必ず数字も含める。例：「A 39.9％」「B 59.9％」「C 79.9％」
- 答え・解説・長文説明は入れない。

## 構図の方向性

以下のような表現を使ってよい。ただし、毎回黒板だけに固定せず、自然に variation を持たせる。

- 左側に大きなクイズ見出しと選択肢カード、右側に考え込む会社員または会議室の人物を配置する。
- ノートやカードに書かれたクイズ。
- 付箋、資料、簡単なグラフ、調査票。
- A/B/Cの選択肢パネルは、文字だけでなく数値を必ず同じカード内に表示する。
- 黒板、ホワイトボード、デスク上の資料、紙面など。
- 余白を活かした引きの構図。
- クイズを見て迷っている様子。

## 避けること

- 答えを書く。
- A/B/Cだけを大きく表示し、選択肢の数字を省略する。
- 解説を書く。
- 文字を詰め込みすぎる。
- 原稿本文をそのまま入れる。
- うるさい配色。
- 漫画っぽすぎる表現。
- 安っぽいクイズ番組風デザイン。
- scene_02のような「答え発表」感を出す。
- 統計・調査クイズ感がない単なる人物イラストにする。

## 生成手順

1. 今回の原稿本文から、scene_01の統計クイズ文を大見出しとして1つ抽出する。固定挨拶、長い出典説明文、テーマ接続文、固定締め文は画像内に入れない。
2. 調査会社・団体名と年を短く抽出し、「株式会社R&G 2026年調査」のような統計ソース表記を作る。
3. そのクイズ文に対して、％・人数・社数など具体的な数値単位を含む短いA/B/Cの選択肢を抽出する。
4. クイズは実在する会社・団体の調査や統計データ由来に見えるようにする。
5. 画像内の文字は、大見出し、統計ソース、数値入りA/B/C選択肢に絞る。
6. 答えは絶対に含めない。
7. 左側にクイズパネル、右側に考え込む会社員、左下にBook Baseロゴを置く構図にする。
8. Book Baseらしい水彩画風・高級感を保つ。

## 出力する画像プロンプトのテンプレート

以下の形式で、最終的な画像生成プロンプトを組み立てる。

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm atmosphere. Use a soft cream white and beige background with teal and subtle gold accents. Place a small natural Book Base logo in the lower-left corner. This is Scene 01, the opening statistics quiz scene. The quiz content must be understandable at a glance. Do not reveal the answer. Do not show only large A/B/C letters; each option card must include the numeric value. Layout: left side has a large Japanese quiz headline, a small survey source label, and three stacked A/B/C option cards with numbers. Right side has a thoughtful Japanese office worker or meeting-room people thinking. Use only the following text elements: {scene_01_quiz_question}, {scene_01_source_label}, {scene_01_option_a}, {scene_01_option_b}, {scene_01_option_c}. Avoid clutter, avoid explanation, avoid English text, and avoid correct-answer marks.
```

## 可変項目

Codexは以下を毎回埋めること。

- `{scene_01_quiz_topic}`
- `{scene_01_quiz_question}`
- `{scene_01_source_label}`
- `{scene_01_option_a}`
- `{scene_01_option_b}`
- `{scene_01_option_c}`
- `{scene_01_composition_hint}`

## scene_01の最終チェック

- クイズになっているか。
- 統計・調査・ニュース感があるか。
- 答えを出していないか。
- 文字が多すぎないか。
- 1画像1メッセージになっているか。
- Book Baseらしい高級感があるか。
- scene_01の入口として機能するか。

## 共通指定

- アスペクト比16:9。
- 水彩画風で、高級感のある落ち着いたビジネス書チャンネル向けの雰囲気にする。
- 文字数は少なく簡潔にし、原稿本文をそのまま長文で載せない。
- 1画像1メッセージにする。
- 前後画像と構図を被らせない。
- Book Baseロゴを左下に小さく自然に配置する。
- サムネイルのように煽りすぎず、ナレーション理解を助ける補助ビジュアルにする。


## 恒久ルール化メモ

scene_01の固定役割は、オープニングの統計・ニュース・調査データ風クイズである。A/B/Cの選択肢を数値付きで出し、答えは出さず、視聴者が自分ごととして考えられる問いにする。クイズのテーマ、問い、選択肢は現在の本・原稿から毎回抽出し、特定テーマの内容を恒久テンプレートに固定しない。

```json
{
  "scene": 1,
  "fixed_role": "オープニングの統計・ニュース・調査データ風クイズ",
  "quiz_topic": "現在の本に合わせたクイズテーマ",
  "quiz_question": "現在の本に合わせた短い問い",
  "source_label": "株式会社R&G 2026年調査",
  "option_a": "A 39.9％",
  "option_b": "B 59.9％",
  "option_c": "C 79.9％",
  "do_not_reveal_answer": true
}
```

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.

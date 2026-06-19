# scene_12

## 固定役割

scene_12 の固定役割は「コメントCTA」。視聴者に、現在のテーマに関連する自分の経験をコメントしてもらう。押しつけがましくなく、自然に参加したくなる雰囲気を作る。

## 画像の目的

scene_09〜scene_11で扱った重要ポイント②の流れを受けて、視聴者が「自分の場合はどうだったか」を考え、コメント欄で経験共有しやすい雰囲気を作る。

## 所属ブロック・重要ポイント

- 所属ブロック：重要ポイント②
- 重要ポイント番号：重要ポイント②
- 20シーン全体の流れの中での位置づけ：scene_11の実話・具体例から、視聴者自身の経験へ橋渡しする。

## 固定してよいもの

- コメントCTA
- あなたの経験は？
- コメントで教えてください
- やわらかい吹き出し
- 視聴者参加の雰囲気

## 固定してはいけないもの

以下は毎回の原稿から可変内容として生成し、テンプレートに固定しない。

- 今回の本のテーマ
- 今回の重要ポイント②の具体語句
- 特定の仕事場面
- 特定の悩み
- 特定の人物名や企業名

## コメントCTAの文体ルール

キーワード型にしない。「〇〇」と一言だけでもコメントしてください、キーワードは「〇〇」です、は禁止。本文では「〇〇した経験はありますか？」「もし似たような経験があれば、ぜひコメント欄で教えてください。」のように自然に質問する。ただし画像内には全文を入れず短くする。

## 画像内テキストルール

画像内テキストは3つ以内。以下の構成を推奨し、この3要素だけを使う。

1. あなたの経験は？
2. `{experience_label}`
3. コメントで教えてください

`experience_label` は現在の原稿から抽出する。例：伝え方で迷った経験、時間の使い方で悩んだ経験、お金の不安を感じた経験、休み方を見直した経験。これらは例であり固定しない。

## 可変データ構造

scene_12用に毎回以下のデータを作成する。

```json
{
  "scene": 12,
  "fixed_role": "コメントCTA",
  "current_theme": "現在の動画テーマ",
  "comment_question": "原稿内のコメントCTA質問",
  "experience_label": "視聴者に聞きたい経験を短く表す言葉",
  "cta_label": "コメントで教えてください",
  "visual_structure": "comment_card / speech_bubbles / viewer_participation / notebook_comment のいずれか",
  "exact_text_elements": [
    "あなたの経験は？",
    "experience_label",
    "コメントで教えてください"
  ]
}
```

## visual_structure の選び方

- `comment_card`：コメント欄風のカードを中心にする。CTAを分かりやすく見せたい、視聴者参加感を出したい場面。
- `speech_bubbles`：吹き出しを使って、やわらかい参加感を出す。会話、考え方、経験共有、人とのやり取りを連想させたい場面。
- `viewer_participation`：視聴者がコメントしようとしている雰囲気を出す。自分ごと化を強めたい場面。
- `notebook_comment`：ノートやメモを使って落ち着いた雰囲気でコメントを促す。本・学び・振り返りの雰囲気を出したい場面。

## 推奨構図

- 構図A：コメントカード型。中央に上品なコメントカード、「あなたの経験は？」、下に短いexperience_label、右下に「コメントで教えてください」。
- 構図B：吹き出し共有型。複数のやわらかい吹き出し、人物は小さく、または手元だけ。
- 構図C：デスク＋コメント欄型。本とノートのある落ち着いたデスク、タブレットやカードにコメント欄風デザイン。
- 構図D：自分ごと化型。会社員が少し考えながらコメントを書こうとしている。背景にやわらかい吹き出し。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 12. Its fixed role is a comment CTA. The image should gently invite viewers to share their own similar experiences related to the current video theme. It should feel warm, calm, and easy to participate in, not pushy or promotional. Do not hard-code any topic from a previous book. Build the experience label from the current script only.

Current comment question:
{comment_question}

Experience label:
{experience_label}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. あなたの経験は？
2. {experience_label}
3. コメントで教えてください

Visual structure:
{visual_structure}

Composition:
{scene_12_composition}

Visual motifs:
- soft comment card
- speech bubbles
- notebook or tablet
- calm desk setup
- gentle viewer participation mood
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid English text, avoid keyword-comment prompts, avoid aggressive CTA design, avoid clutter, and avoid repeating the Scene 08 subscription CTA composition.
```

## 避けること

- 英語テキスト
- `Similar experience?`
- Subscribe風の表現
- scene_08のチャンネル登録CTAと似た構図
- キーワード型コメント促し
- 長文コメント文
- 原稿のコメントCTA全文
- 派手な吹き出しだらけのデザイン
- サムネイル風の煽り

## 画像生成前チェック

scene_12の画像プロンプトを作る前に、必ず以下を確認する。

1. scene_12本文からコメントCTA質問を抽出しているか
2. experience_label を現在のテーマに合わせて短く作っているか
3. 画像内テキストが3つ以内か
4. scene_08の登録CTAと混ざっていないか
5. キーワード型コメント促しになっていないか

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK / NG
コメントCTAだと分かる：OK / NG
現在のテーマに合う経験質問になっている：OK / NG
experience_label が原稿から生成されている：OK / NG
キーワード型コメント促しになっていない：OK / NG
英語テキストなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_08と構図が違う：OK / NG
押しつけがましくない：OK / NG
```

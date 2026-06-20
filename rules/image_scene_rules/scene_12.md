# scene_12

## 固定役割

scene_12 の固定役割は「コメントCTA」。ただし、コメント促し自体を画像の主役にしない。scene_09〜scene_11で扱った重要ポイント②の流れを受けて、本の内容・学び・考え方・図解・要点整理を前面に出し、視聴者が自然に自分の経験を重ねたくなる控えめなコメント導線を作る。

## 画像の目的

scene_09〜scene_11で扱った重要ポイント②を、視聴者がひと目で振り返れる図解・概念整理・要点カードとして見せる。そのうえで、学びに関連する短い問いかけを小さく添え、コメント欄で経験共有しやすい雰囲気を作る。

## 所属ブロック・重要ポイント

- 所属ブロック：重要ポイント②
- 重要ポイント番号：重要ポイント②
- 20シーン全体の流れの中での位置づけ：scene_11の実話・具体例を、本の学びとして整理し直し、視聴者自身の経験へ自然に橋渡しする。

## 固定してよいもの

- コメントCTAという役割
- 本の学びを主役にした図解・概念整理・要点カード
- 右下または端の小さな吹き出し・付箋・補助エリア
- Book Baseロゴの小さく自然な配置
- 視聴者参加の雰囲気

## 固定してはいけないもの

以下は毎回の原稿から可変内容として生成し、テンプレートに固定しない。

- 今回の本のテーマ
- 今回の重要ポイント②の具体語句
- 特定の仕事場面
- 特定の悩み
- 特定の人物名や企業名
- 「あなたの経験は？」「{experience_label}」「コメントで教えてください」の3点セット

## コメントCTAの文体ルール

コメント促しは、画像の一部に小さく添える短い日本語1要素までにする。キーワード型にしない。「〇〇」と一言だけでもコメントしてください、キーワードは「〇〇」です、は禁止。本文から自然なコメント質問を抽出しても、画像内には全文を入れない。

推奨表現例：

- 似た経験はコメントで
- あなたならどうしますか？
- 似たことありますか？
- コメントで教えてください

## 画像内テキストルール

画像内テキストは3つ以内。基本は以下の考え方にする。

1. メインテキスト：本の内容に関する要点・見出し・図解ラベル
2. メイン補助テキスト：図解や整理カードの短いラベル
3. コメントCTA：補助的な短い日本語1要素まで

英語テキストは禁止。長文は禁止。CTAを複数行で大きく入れない。コメントCTAだけの画像にしない。

## 可変データ構造

scene_12用に毎回以下のデータを作成する。

```json
{
  "scene": 12,
  "fixed_role": "コメントCTA",
  "current_theme": "現在の動画テーマ",
  "comment_question": "原稿内のコメントCTA質問",
  "learning_label": "scene_09〜scene_11から抽出した本の学びの短い見出し",
  "cta_label": "短く自然なコメントCTA 1要素",
  "visual_structure": "learning_diagram / concept_map / notebook_summary / key_point_card のいずれか",
  "exact_text_elements": [
    "learning_label",
    "要点整理などの短い図解補助ラベル",
    "cta_label"
  ]
}
```

## visual_structure の選び方

- `learning_diagram`：重要ポイント②の考え方を整理図・2〜3個の要点カードとして見せる。
- `concept_map`：概念同士の関係、考え方の転換、会話や判断の流れを図解する。
- `notebook_summary`：本とノートの落ち着いたデスクで、学びのメモや整理カードを主役にする。
- `key_point_card`：重要ポイント②の結論や型を、上品な中央カードで端的に見せる。

## 推奨構図

- メイン：本の内容を表す図解・概念整理・要点カードを中央または大きな領域に配置する。
- サブ：右下の吹き出し、付箋、または小さな補助エリアにコメント促しを1要素だけ入れる。
- Book Baseロゴ：左下や右下に小さく自然に配置する。
- scene_08の登録CTAに似た大きなCTAカード構図にしない。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is Scene 12. Its fixed role is a comment CTA, but the CTA must not be the main subject. Make the book's learning, key idea, diagram, and conceptual summary from Scenes 09-11 the visual focus. Add the comment prompt only as one small supporting Japanese text element in a lower-corner speech bubble or small auxiliary area. Do not hard-code any topic from a previous book. Build all labels from the current script only.

Current comment question:
{comment_question}

Learning label:
{learning_label}

Comment CTA label:
{cta_label}

Use only the following Japanese text elements exactly as written. The first two are main learning/diagram text; the comment CTA is the final single small supporting element. Do not add any other Japanese or English text:
1. {learning_label}
2. 要点整理
3. {cta_label}

Visual structure:
{visual_structure}

Composition:
{scene_12_composition}

Visual motifs:
- book learning diagram
- key point summary cards
- concept map or notebook labels
- small lower-corner speech bubble for the CTA
- calm desk setup
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid English text, avoid keyword-comment prompts, avoid making the comment CTA the main subject, avoid the fixed three-part CTA set, avoid aggressive CTA design, avoid clutter, and avoid repeating the Scene 08 subscription CTA composition.
```

## 避けること

- コメントCTAを画像の主役にすること
- 「あなたの経験は？」「{experience_label}」「コメントで教えてください」の3つを毎回必須にすること
- 英語テキスト
- `Similar experience?`
- Subscribe風の表現
- scene_08のチャンネル登録CTAと似た構図
- キーワード型コメント促し
- 長文コメント文
- 原稿のコメントCTA全文
- 派手な吹き出しだらけのデザイン
- サムネイル風の煽り
- コメント欄誘導だけの単調な画像

## 画像生成前チェック

scene_12の画像プロンプトを作る前に、必ず以下を確認する。

1. scene_09〜scene_11から本の学び・重要ポイント②の要点を抽出しているか
2. 図解・概念整理・要点カードが主役になっているか
3. scene_12本文からコメントCTA質問を抽出しているか
4. コメントCTAが短い日本語1要素までになっているか
5. 画像内テキストが3つ以内か
6. scene_08の登録CTAと混ざっていないか
7. キーワード型コメント促しになっていないか

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK / NG
本の学び・要点整理が主役：OK / NG
コメントCTAが補助的に小さい：OK / NG
コメントCTAが短い1要素まで：OK / NG
現在のテーマに合う経験質問になっている：OK / NG
キーワード型コメント促しになっていない：OK / NG
英語テキストなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_08と構図が違う：OK / NG
押しつけがましくない：OK / NG
```

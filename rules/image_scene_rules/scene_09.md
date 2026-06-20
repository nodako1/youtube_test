# scene_09

## このシーンの固定役割

重要ポイント②の導入。scene_05〜scene_08で扱った重要ポイント①から、次の重要ポイント②へ話を進める。

scene_09は、2つ目の視点・方法・考え方・実践ポイントに入ったことを、一目で分かる形にする。

## 固定してはいけない内容

以下は特定の本に依存するため、恒久テンプレートに固定しない。

- 会話
- 言い換え
- 受け取り方
- 視点を変える
- 2人のビジネスパーソン
- コミュニケーション
- 相手に伝える

必要な場合だけ、現在の原稿から可変内容として抽出する。

## 毎回抽出する可変データ

scene_09用に、現在の原稿から以下を作成する。

```json
{
  "scene": 9,
  "fixed_role": "重要ポイント②の導入",
  "point_2_label": "重要ポイント②を短く表す言葉",
  "point_2_core_message": "scene_09で一番伝えるべき内容",
  "point_2_type": "method / mindset / habit / process / contrast / skill / framework のいずれか",
  "visual_metaphor": "重要ポイント②に合う視覚的な比喩",
  "exact_text_elements": [
    "重要ポイント②",
    "短いラベル",
    "短い補足メッセージ"
  ]
}
```

## point_2_type の選び方

- `method`：やり方、手順、コツなど具体的な方法。
- `mindset`：考え方、視点、前提。
- `habit`：習慣、毎日の行動、続ける工夫。
- `process`：流れ、ステップ、進め方。
- `contrast`：普通のやり方と本書の視点の違い。
- `skill`：技術、使い方、実践スキル。
- `framework`：型、フレーム、整理法。

## 画像内テキストルール

- 固定してよいテキストは「重要ポイント②」のみ。
- その他は原稿から生成した短いラベルと補足メッセージだけにする。
- 画像内テキストは3つ以内。
- 原稿本文のコピペ、20文字以上の長い説明、英語テキスト、4つ以上のテキスト要素は禁止。

## 推奨構図

- 構図A：第2ポイントカード型。中央または左側に「重要ポイント②」のカード、右側に現在のpoint_2_typeに合う象徴モチーフ。
- 構図B：次のステップ型。階段、矢印、ロードマップ、2つ目のカードなどで重要ポイント①から一歩進むイメージ。
- 構図C：視点切り替え型。`mindset` / `contrast` の場合のみ使用し、左右の違いや見方の変化を上品に表現。
- 構図D：実践方法の入口型。`method` / `skill` / `process` の場合に使用し、ノート、カード、手順アイコンなどで具体的な方法に入る雰囲気を出す。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is Scene 09. Its fixed role is to introduce Key Point 2. The image should make viewers understand that the video is moving into the second important point. Do not create a generic business conversation image. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 2:
{point_2_label}

Current Scene 09 core message:
{point_2_core_message}

Point 2 type:
{point_2_type}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. 重要ポイント②
2. {point_2_label}
3. {point_2_short_message}

Visual metaphor:
{visual_metaphor}

Composition:
{scene_09_composition}

Visual motifs:
{visual_motifs}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic conversation scenes, avoid over-explaining, avoid English text, and avoid repeating the Scene 08 CTA composition or Scene 05 Key Point 1 composition.
```

## 避けること

会話シーン固定、視点変更固定、特定の本の言葉固定、ただの人物イラスト、scene_05と同じ構図、scene_08のCTAカード構図、長文、英語テキスト。

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK / NG
重要ポイント②の導入だと分かる：OK / NG
現在の原稿内容に沿っている：OK / NG
point_2_label が原稿から生成されている：OK / NG
point_2_type が適切：OK / NG
過去テーマのハードコードなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_08と構図が違う：OK / NG
scene_05と構図が違う：OK / NG
generic business image になっていない：OK / NG
```

# scene_06

## 固定役割

scene_06は、重要ポイント①の理由・背景・仕組みを説明するシーンである。scene_05で提示した重要ポイント①について、「なぜそうなのか」「何が起きているのか」「どういう構造なのか」を一目で伝える。

特定の本の内容を固定テンプレートに入れず、毎回の原稿から可変内容を抽出する。

## 毎回抽出する可変データ

scene_06用に以下を毎回作成する。

```json
{
  "scene": 6,
  "fixed_role": "重要ポイント①の理由・背景・仕組み説明",
  "point_1_label": "重要ポイント①を短く表す言葉",
  "scene_06_core_message": "scene_06で一番伝えるべき理由・背景・仕組み",
  "reason_label": "理由を短く表す言葉",
  "mechanism_label": "仕組みや背景を短く表す言葉",
  "effect_label": "結果や影響を短く表す言葉",
  "visual_metaphor": "この内容に合う視覚的な比喩",
  "visual_structure": "cause_to_effect / before_after / hidden_mechanism / obstacle_and_solution / contrast のいずれか",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## ラベル作成ルール

- `exact_text_elements` は毎回の原稿から生成する。
- 1つのラベルは原則8〜12文字程度、長くても15文字以内。
- 3つ以内。
- 説明文ではなく短い見出しにする。
- 原稿本文をそのまま長く入れない。
- 過去動画のキーワードを使い回さない。
- 今回の本に関係ない汎用語だけで済ませない。

## visual_structure の選び方

- `cause_to_effect`：理由から結果への流れを見せる。原因と結果がある場合に使う。
- `before_after`：変化前と変化後を比較する。やる前と後、気づく前と後の差を見せたい場合に使う。
- `hidden_mechanism`：見えない仕組みを図解する。心理、構造、思考、習慣、感情、判断などを扱う場合に使う。
- `obstacle_and_solution`：障害と解決の関係を見せる。詰まりや障害を取り除くイメージが合う場合に使う。
- `contrast`：2つの状態や考え方の違いを並べる。勘違いと正しい見方、普通のやり方と本書の視点を比べる場合に使う。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 06. Its fixed role is to explain the reason, background, or mechanism behind Key Point 1. The image should visually clarify why the first key point matters, based on the current script. Do not create a generic business person image. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 1:
{point_1_label}

Current Scene 06 core message:
{scene_06_core_message}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. {reason_label}
2. {mechanism_label}
3. {effect_label}

Visual structure:
{visual_structure}

Visual metaphor:
{visual_metaphor}

Composition:
{scene_06_composition}

Visual motifs:
{visual_motifs}

Keep the image clean and easy to understand at a glance. Use minimal text only. Do not place long script text. Avoid clutter, avoid generic emotional icons, avoid a generic desk-only scene, avoid over-explaining, and avoid repeating the Scene 05 composition.
```

## 構図作成ルール

- `cause_to_effect`：左から右へ、理由・仕組み・結果が自然に流れる構図にする。
- `hidden_mechanism`：表面上の人物や仕事場面の背後に、内側の仕組みを示すカードや線を配置する。
- `contrast`：左側に一般的な状態、右側に本書が示す視点を配置する。
- その他の構造でも、scene_05と構図を明確に変える。

## 避けること

- 特定の本の内容を固定で入れる。
- 過去テーマの語句を使い回す。
- `emotional expression icons` を安易に並べる。
- ただのビジネス人物イラストにする。
- 机、付箋、ノートだけの雰囲気画像にする。
- scene_05と同じ構図にする。
- 研究データやグラフ中心の構図にする。
- 文字が多い図解にする。
- サムネイルのような煽りデザインにする。

## 画像生成前チェック

scene_06の画像プロンプトを作る前に、必ず以下を確認する。

1. scene_05の重要ポイント①を取得しているか。
2. scene_06本文から理由・背景・仕組みを抽出しているか。
3. exact_text_elementsが今回の原稿由来か。
4. 過去の本のキーワードが残っていないか。
5. scene_05と構図が被っていないか。

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK / NG
現在の原稿内容に沿っている：OK / NG
重要ポイント①の理由・背景・仕組みが見える：OK / NG
可変ラベルが原稿から生成されている：OK / NG
過去テーマのハードコードなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
visual_structure が適切：OK / NG
scene_05と構図が違う：OK / NG
generic business image になっていない：OK / NG
```

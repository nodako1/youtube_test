# scene_10

## 固定役割

重要ポイント②の具体化。

scene_10は、scene_09で提示した重要ポイント②を、具体例・比較・手順・実践場面などで分かりやすくする。視聴者が「なるほど、こう使うのか」と理解できるように、重要ポイント②を一段具体化する。

## 固定してはいけないもの

次の内容は特定の本に依存するため、恒久テンプレートに固定しない。

- cause and effect
- flowchart
- split-screen
- business people in conversation
- コミュニケーション
- 言い換え
- 視点変更
- 原因と結果

これらは現在の本や原稿に合う場合のみ、可変内容として使う。

## scene_10 可変データ構造

scene_10用に毎回以下を作成する。

```json
{
  "scene": 10,
  "fixed_role": "重要ポイント②の具体化",
  "point_2_label": "重要ポイント②を短く表す言葉",
  "scene_10_core_message": "scene_10で一番伝えるべき具体内容",
  "example_label": "具体例や場面を短く表す言葉",
  "application_label": "実践・使い方を短く表す言葉",
  "result_label": "得られる変化や理解を短く表す言葉",
  "visual_structure": "before_after / step_demo / example_scene / comparison / action_map / framework_demo のいずれか",
  "visual_metaphor": "現在の内容に合う視覚的な比喩",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## visual_structure の選び方

- `before_after`：変化前と変化後を見せる場合。
- `step_demo`：3ステップなど、順番に進める手順を見せる場合。
- `example_scene`：会議、仕事、日常、読書、整理、学習など、1つの具体場面で見せた方が伝わる場合。
- `comparison`：普通のやり方と本書のやり方、間違いやすい方法と良い方法、旧習慣と新習慣などを比べる場合。
- `action_map`：やることが複数あり、実践手順を地図のように見せたい場合。
- `framework_demo`：考え方の型、整理法、チェックリスト、判断基準を見せる場合。

## 画像内テキストルール

画像内テキストは3つ以内にする。

基本形式：

1. 重要ポイント②の短い内容
2. 具体例ラベル
3. 実践・変化ラベル

ただし、毎回の原稿から生成する。

禁止：原稿本文のコピペ、20文字以上の長い説明、4つ以上のテキスト要素、英語テキスト、今回の本の言葉の固定化、原因と結果の固定表示。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 10. Its fixed role is to make Key Point 2 concrete through an example, comparison, practical step, or application image. The image should help viewers understand how Key Point 2 works in practice. Do not create a generic cause-and-effect flowchart unless the current script actually requires it. Do not hard-code any topic from a previous book. Build the visual message from the current script only.

Current Key Point 2:
{point_2_label}

Current Scene 10 core message:
{scene_10_core_message}

Visual structure:
{visual_structure}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. {example_label}
2. {application_label}
3. {result_label}

Visual metaphor:
{visual_metaphor}

Composition:
{scene_10_composition}

Visual motifs:
{visual_motifs}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid generic split-screen flowcharts, avoid generic business people, avoid English text, and avoid repeating the Scene 09 composition.
```

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK / NG
重要ポイント②の具体化になっている：OK / NG
現在の原稿内容に沿っている：OK / NG
visual_structure が適切：OK / NG
可変ラベルが原稿から生成されている：OK / NG
過去テーマのハードコードなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_09と構図が違う：OK / NG
generic flowchart image になっていない：OK / NG
```

# scene_18

## 固定役割

scene_18 の恒久的な役割は「本の学びを、仕事や日常の行動に変える場面として見せる」こと。
「理解した」で終わらせず、視聴者が「明日から試してみる」「自分でも実践できそう」と直感できる実践画像にする。

scene_18 は scene_17 の総まとめ、scene_19 の過去動画接続、scene_20 の締めの余韻とは混ぜない。

## 毎回抽出する可変データ

画像プロンプト作成前に、現在の原稿から以下を作る。

```json
{
  "scene": 18,
  "fixed_role": "本の学びを仕事や日常に落とし込む実践シーン",
  "practice_theme_label": "今回の本の実践テーマを短く表す言葉",
  "application_context": "work / daily_life / both のいずれか",
  "practice_action_label": "どのように行動へ変えるかを短く表す言葉",
  "viewer_takeaway_label": "視聴者に伝えたい実践メッセージ",
  "practice_type": "planning / communication / habit_building / reflection / task_execution / emotional_control / decision_making のいずれか",
  "visual_structure": "desk_focus / morning_planning / checklist_flow / calm_action_scene / notebook_and_tasks / work_life_bridge のいずれか",
  "supporting_objects": ["実践を自然に見せる小物"],
  "exact_text_elements": ["画像内に表示する短い日本語テキスト"]
}
```

本ごとに変わる具体キーワード、著者名、理論名、章タイトル、原稿固有フレーズ、具体的な実践項目、特定業界に寄りすぎる作業表現は固定テンプレートに入れず、毎回の原稿から可変生成する。

## practice_type

scene_18 はただ「机で作業する人」にしない。必ず実践の種類を定義し、人物の行動・小物・構図・テキストへ反映する。

- `planning`：計画、整理、優先順位づけ。
- `communication`：人との関わり方、伝え方。
- `habit_building`：習慣として少しずつ続ける。
- `reflection`：振り返り、内省、気づきを行動に変える。
- `task_execution`：実務の進め方として実践する。
- `emotional_control`：ストレス対策、気持ちの整え方。
- `decision_making`：考え方や判断軸を日常判断に活かす。

## visual_structure

- `desk_focus`：整理された机の上に、実践の準備と行動が見える構図。
- `morning_planning`：朝の光の中で、1日の行動を整えている構図。
- `checklist_flow`：チェックリストやカードの流れで、実践の順序を見せる構図。
- `calm_action_scene`：手元や所作を中心に、静かに実践している様子を見せる構図。
- `notebook_and_tasks`：ノート・手帳・タスクカードを中心にした構図。
- `work_life_bridge`：仕事と日常が自然に連続しているように見せる構図。

## 固定してよい要素

実践、仕事に活かす、日常で試す、行動に変える、小さく始める、整理されたデスク、ノート、手帳、チェックリスト、付箋、タスクカード、朝のやわらかい光、落ち着いた集中感、Book Base らしい上品で見やすい水彩イラスト、視聴者が「自分もやってみよう」と思える実用感。

## 画像内テキスト

- 最大1要素まで。
- 短い日本語のみ。
- 10〜12文字前後を目安にし、長くても15文字程度まで。
- 説明文、本タイトル、著者名、英語テキスト、CTA風テキストは入れない。

固定見出し候補は必要に応じて1つだけ使う。

- 今日から実践
- 仕事に活かす
- 行動に変える
- 小さく試す

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is Scene 18. Its fixed role is to show how the learning from the book can be applied in work or daily life. The image should help viewers imagine putting the ideas into action. It must not become a generic office scene or a simple desk-working image.

Practice theme:
{practice_theme_label}

Application context:
{application_context}

Practice action:
{practice_action_label}

Viewer takeaway:
{viewer_takeaway_label}

Practice type:
{practice_type}

Visual structure:
{visual_structure}

Supporting objects:
{supporting_objects}

Use only the following Japanese text element exactly as written. Do not add any other Japanese or English text:
1. {practice_text}

Composition:
{scene_18_composition}

Visual motifs:
- organized desk
- notebook, planner, checklist, sticky notes, or task cards
- soft morning light
- hopeful and focused atmosphere
- calm structured whitespace
- premium watercolor texture
- gentle teal and subtle gold accents

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid English text, avoid generic office stock-image feeling, avoid broken Japanese text, and avoid turning the image into a closing or recap scene.
```

## 避けること

ただPCに向かっているだけの人物、ただのオフィス風景、汎用的なビジネス素材風の構図、本の学びと無関係な雑然とした作業風景、長文説明、行動手順の文章列挙、英語テキスト、意味不明な文字、崩れた日本語、scene_17 のまとめ図、scene_20 の締め画像、CTA風表現、安っぽいアイコン風表現、派手な広告風表現。

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK / NG
本の学びを仕事や日常に落とし込む画像になっている：OK / NG
単なるデスクワーク画像になっていない：OK / NG
practice_theme_label が定義されている：OK / NG
practice_action_label が定義されている：OK / NG
practice_type が設定されている：OK / NG
visual_structure が設定されている：OK / NG
supporting_objects が適切：OK / NG
画像内テキストが1要素以内：OK / NG
英語テキストなし：OK / NG
指定外テキストなし：OK / NG
文字量が多すぎない：OK / NG
scene_17の総まとめ画像と役割が混ざっていない：OK / NG
scene_20の締め画像と役割が混ざっていない：OK / NG
generic office image になっていない：OK / NG
```

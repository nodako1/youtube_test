# scene_11

## このシーンの固定役割

重要ポイント②を、確認可能な実話エピソードで補強する。

scene_11は、scene_10で具体化した重要ポイント②に対して、「実際にこういう考え方や行動をした人・組織がいる」という形で説得力を加えるシーンである。

## 固定してはいけないもの

以下をテンプレートに固定しない。

- Toyota、トヨタ、豊田喜一郎、元社長
- 特定企業名、特定人物名
- 特定の歴史エピソード、特定の業界

具体的な人物・企業・出来事は、毎回の原稿と調査結果から可変内容として抽出する。

## scene_11 可変データ構造

scene_11用に毎回以下を作成する。

```json
{
  "scene": 11,
  "fixed_role": "重要ポイント②の実話エピソード補強",
  "point_2_label": "重要ポイント②を短く表す言葉",
  "scene_11_core_message": "実話エピソードによって補強したい内容",
  "episode_type": "person / company / historical_event / public_case / symbolic_only のいずれか",
  "episode_name": "検証済みの場合のみ、人物名・企業名・出来事名。未確認ならnull",
  "episode_role_label": "人物や企業の立場を短く表す言葉",
  "episode_action_label": "実話内の行動を短く表す言葉",
  "lesson_label": "重要ポイント②とのつながりを短く表す言葉",
  "verification_status": "verified / needs_review / unverified",
  "visual_mode": "named_episode / silhouette_episode / symbolic_action のいずれか",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## verification_status

- `verified`：信頼できる情報源で確認でき、人物名または企業名が明確で、エピソードと重要ポイント②のつながりが自然で、過度な脚色がない場合のみ。画像内に人物名・企業名を短く入れてよい。
- `needs_review`：根拠が弱い、出典が曖昧、人物名や企業名の使用に不安がある、つながりがやや弱い場合。人物名や企業名は出さず、シルエットまたは象徴表現にする。
- `unverified`：実話か確認できない、AIが作った可能性がある、人物名や企業名が不確か、根拠がない場合。成功扱いにせず、`NEEDS_REVIEW`として`failed_images.md`または`quality_report.md`に記録する。

## visual_mode

- `named_episode`：検証済みの人物・企業・出来事を扱う。顔をリアルに再現しすぎない。参照画像がない場合は実在人物の顔を正確に描こうとしない。
- `silhouette_episode`：人物・企業は分かるが、顔や詳細を出さない方がよい場合。後ろ姿、シルエット、資料、仕事場面で表現する。
- `symbolic_action`：検証が弱い、または人物名を出さない方が安全な場合。資料を渡す、チームで確認する、記録する、決断する、小さな改善を積み重ねるなど、行動を象徴する。

## 画像内テキストルール

画像内テキストは3つ以内にする。

verified の場合：

```text
実話エピソード
{episode_name}
{lesson_label}
```

needs_review の場合：

```text
実話エピソード
象徴シーン
{lesson_label}
```

unverified の場合は画像生成を成功扱いにしない。

## 顔・人物表現ルール

- 参照画像がない場合、実在人物の顔を正確に再現しようとしない。
- 写真のような写実表現にしない。
- 必要ならシルエット、後ろ姿、象徴的な行動場面にする。
- 顔よりも、行動やエピソードの意味を主役にする。
- 権威ある人物の肖像画風に寄せすぎない。

## 推奨構図

- 構図A：実話エピソードカード型。中央に「実話エピソード」のカード、周囲に人物シルエット、資料、行動シーンを置く。
- 構図B：象徴的な行動シーン型。人物名よりも、相談する、決断する、書き直す、共有する、記録するなどの行動を見せる。
- 構図C：歴史・企業エピソード型。verified の場合のみ、資料、建物、会議室、手紙、ノートなどを控えめに使う。
- 構図D：シルエット補強型。人物を特定しすぎず、背景に資料や行動モチーフを置く。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is Scene 11. Its fixed role is to reinforce Key Point 2 with a real-life episode. The episode must be based on current script research. Do not hard-code any person, company, or historical figure from a previous book. Do not invent a real-life episode. If verification is weak, use a silhouette or symbolic action scene instead of a named person.

Current Key Point 2:
{point_2_label}

Current Scene 11 core message:
{scene_11_core_message}

Episode type:
{episode_type}

Verification status:
{verification_status}

Visual mode:
{visual_mode}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. {text_element_1}
2. {text_element_2}
3. {text_element_3}

Composition:
{scene_11_composition}

Visual motifs:
{visual_motifs}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid fake historical portraits, avoid invented company imagery, avoid overly realistic faces, avoid hard-coded Toyota or any previous-book topic, and avoid repeating the Scene 10 composition.
```

## quality_report.md への記録

`quality_report.md`に以下を記録する。

```text
【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK / NG
重要ポイント②の実話補強になっている：OK / NG
エピソードが現在の原稿に基づいている：OK / NG
verification_status を記録している：OK / NG
検証が弱い場合に人物名を出していない：OK / NG
検証が弱い場合に顔を描いていない：OK / NG
過去テーマのハードコードなし：OK / NG
Toyota等の固定企業名なし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_10と構図が違う：OK / NG
```

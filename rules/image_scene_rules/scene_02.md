# scene_02

## このシーンの役割

scene_02は、scene_01で出したクイズの正解を発表し、その正解が今回の動画テーマにつながることを示すシーンです。単なる正解発表ではなく、次の4つを同時に満たしてください。

1. クイズの答えを明確に示す
2. 視聴者に「なるほど」と思わせる
3. 今回のテーマに自然につなげる
4. scene_03の本紹介に向けて期待感を作る

## 画像プロンプト生成の基本方針

scene_02の画像プロンプトは、単純な「共通プロンプト + Scene説明 + Base prompt」の連結にしないでください。以下の要素を分けて設計し、最終プロンプトで自然に統合してください。

1. scene_role：クイズの正解発表とテーマへの橋渡し
2. core_message：否定しない言い換えによって、相手が話しやすくなる
3. exact_text_elements：画像内に入れてよい日本語テキスト
4. composition：構図
5. visual_motifs：使用するモチーフ
6. style：Book Base共通の画風
7. negative_rules：避けること
8. variation_key：前後シーンと構図を変えるための指定

## Book Base共通スタイル

- 16:9 landscape
- watercolor illustration
- premium calm atmosphere
- Japanese business book YouTube channel
- soft cream white and beige background
- teal and subtle gold accents
- clean composition
- enough whitespace
- small natural Book Base logo
- minimal concise Japanese text only
- one clear message
- do not place long script text
- do not use loud thumbnail-like design
- avoid clutter

## 画像内に入れてよい文字

画像内テキストは以下の3つ以内にしてください。

```text
正解はB
相手が話しやすくなる
否定しない言い換え
```

画像生成プロンプトには必ず次の英文を入れてください。

```text
Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.
```

## 推奨構図

### 構図案A：答えカード型

左側に大きな答えカードを置き、「正解はB」「相手が話しやすくなる」を見せる。右側に納得した表情の会社員を配置し、小さく「否定しない言い換え」のキーワードカードを添える。

### 構図案B：クイズからテーマへ橋渡し型

左側にscene_01のクイズカードの一部、中央に正解Bの表示、右側に会話がやわらかくなるイメージを配置する。

### 構図案C：対話の空気が変わる型

中央に「正解はB」のカードを置き、背景に2人の会話アイコン、周囲に柔らかい矢印や光、右下に「否定しない言い換え」を配置する。

毎回同じ構図にならないように、`variation_key`で構図差分を明示してください。

## 避けること

- 大きすぎる人物の顔アップ
- クイズ番組のような派手な演出
- 文字が4つ以上ある画面
- 英語テキスト
- 長い説明文
- 正解発表だけでテーマ接続がない画像
- scene_01とほぼ同じ黒板クイズ構図
- サムネイルのような煽りデザイン

## 出力JSON構造

scene_02は、少なくとも以下の構造を持つJSONとして出力してください。

```json
{
  "scene": 2,
  "scene_role": "クイズの正解発表とテーマへの橋渡し",
  "core_message": "否定しない言い換えによって、相手が話しやすくなる",
  "exact_text_elements": ["正解はB", "相手が話しやすくなる", "否定しない言い換え"],
  "composition": "左側に大きな答えカード、右側に納得した表情の会社員、小さな会話アイコンを背景に配置する",
  "visual_motifs": ["答えカード", "会社員", "会話アイコン", "やわらかい矢印", "淡い光"],
  "negative_rules": ["長文を入れない", "指定外の文字を入れない", "派手なクイズ番組風にしない", "scene_01と同じ構図にしない"],
  "final_prompt": "..."
}
```

## 画像品質チェック

画像生成後、`quality_report.md`に以下を記録してください。

```text
【scene_02 画像品質チェック】

scene_role反映：OK / NG
正解Bが一目で分かる：OK / NG
テーマへの橋渡しがある：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
Book Baseらしい高級感：OK / NG
scene_01と構図が違う：OK / NG
サムネイルっぽくなりすぎていない：OK / NG
```

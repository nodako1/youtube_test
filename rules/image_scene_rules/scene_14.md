# scene_14

## このシーンの固定役割

重要ポイント③の具体化。

scene_13で提示した重要ポイント③について、具体例・実践場面・使い方・手順などで分かりやすく見せる。視聴者が「こう使えばいいのか」「こういう場面で役立つのか」と理解できるように、重要ポイント③を一段具体化する。

## 固定してはいけないもの

以下は特定の本やテーマに依存するため、恒久テンプレートに固定しない。

- meeting
- businessperson calmly responding
- 会議
- 返答
- 上司への対応
- コミュニケーション
- 言い換え
- 具体的フレーズ

## 毎回抽出する可変データ

```json
{
  "scene": 14,
  "fixed_role": "重要ポイント③の具体化",
  "point_3_label": "重要ポイント③を短く表す言葉",
  "scene_14_core_message": "scene_14で一番伝えるべき具体内容",
  "example_context_label": "具体場面を短く表す言葉",
  "action_label": "実践する行動を短く表す言葉",
  "result_label": "得られる変化や効果を短く表す言葉",
  "visual_structure": "practical_example / step_demo / before_after / tool_use / scenario_demo / framework_application のいずれか",
  "visual_metaphor": "現在の内容に合う視覚的な比喩",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## visual_structure の選び方

- `practical_example`：仕事や日常の1場面で説明した方が伝わる場合。
- `step_demo`：順番にやること、3ステップや流れで見せたい場合。
- `before_after`：実践前後の違い、改善や変化を見せたい場合。
- `tool_use`：ノート、チェックリスト、表、カード、フレームなどを道具として見せたい場合。
- `scenario_demo`：原稿に具体場面がある場合。ただし会議に固定しない。
- `framework_application`：重要ポイント③がフレームワークや判断基準の場合。

## 画像内テキストルール

画像内テキストは3つ以内にする。

基本形式：

1. 具体場面ラベル
2. 実践ラベル
3. 変化ラベル

禁止：原稿本文のコピペ、20文字以上の長い説明、4つ以上のテキスト要素、英語テキスト、会議や返答の固定、今回の本の言葉の固定化。

## 推奨プロンプトテンプレート

scene_14では、Book Base共通の水彩・高級感スタイルを使い、以下を必ず含める。

- Scene 14の固定役割は「重要ポイント③の具体化」
- Current Key Point 3
- Current Scene 14 core message
- Visual structure
- `Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.`
- Visual metaphor
- Composition
- Visual motifs
- scene_13の導入構図とscene_18の全体実践構図を避ける指示

## 品質チェック

`quality_report.md` に以下を記録する。

```text
【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK / NG
重要ポイント③の具体化になっている：OK / NG
現在の原稿内容に沿っている：OK / NG
visual_structure が適切：OK / NG
可変ラベルが原稿から生成されている：OK / NG
過去テーマのハードコードなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_13と構図が違う：OK / NG
scene_18と役割が混ざっていない：OK / NG
generic meeting image になっていない：OK / NG
```

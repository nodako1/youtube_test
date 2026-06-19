# scene_20

## 固定役割

動画全体を温かく締め、読後感・余韻・感謝・前向きな気持ちを残すクロージングシーン。
本の内容を強く説明するのではなく、視聴者が学びを静かに受け取って終われる画像にする。

scene_20 は scene_17 の「3つの重要ポイントの総整理」、scene_18 の「仕事や日常への実践シーン」、scene_19 の「過去動画との接続シーン」と混ぜない。

## 毎回作成する可変データ

```json
{
  "scene": 20,
  "fixed_role": "動画全体を温かく締めるクロージングシーン",
  "final_message_label": "動画全体の最後に残したい短い言葉",
  "closing_emotion": "warm / serene / appreciative / hopeful / reflective のいずれか",
  "viewer_aftertaste_label": "視聴者に残したい読後感を短く表す言葉",
  "closing_type": "gentle_finish / learning_takeaway / next_book_invitation / quiet_reflection / warm_thank_you のいずれか",
  "visual_structure": "closing_book / quiet_desk / window_light / hand_and_book / home_office_wide / calm_tabletop のいずれか",
  "supporting_objects": ["締めの雰囲気を自然に見せる小物"],
  "exact_text_elements": ["画像内に表示する短い日本語テキスト"]
}
```

## 固定してよい方向性

締めくくり、読後感、余韻、感謝、また次の一冊へ、本を閉じる手元、静かなホームオフィス、やわらかい朝の光、整った机、本、ノート、ペン、コーヒー、窓辺、Book Baseらしい上品で温かい水彩イラスト、視聴者が学びを持ち帰るような穏やかな雰囲気。

## 固定してはいけないもの

今回の本の具体的なタイトル、特定の著者名、今回の本の具体的キーワード、特定の章タイトル、今回の原稿にしか出てこない結論、特定のテーマ語句、過去動画のタイトルを固定テンプレートに入れない。必要な場合は毎回の原稿から可変内容として抽出する。

## 画像内テキストルール

- 最大1要素まで。
- 短い日本語のみ。
- 10〜14文字前後を目安にし、長くても16文字程度まで。
- 本のタイトル、著者名、強いCTA、英語テキストを入れない。
- 固定候補は「今日の学びを明日へ」「学びを、日常へ」「また次の一冊で」「読んで終わりにしない」のうち1つだけ。

## 推奨構図

- closing_book：静かなホームオフィスで、やさしく本を閉じる手元。
- quiet_desk：整った机に本・ノート・ペンを余白多めに置く。
- window_light：窓からやわらかい光が入り、机上の本とノートを包む。
- hand_and_book：手元と本を近めに見せ、人の温度感を出す。
- home_office_wide：静かな部屋全体を少し引いて見せる。
- calm_tabletop：本、ペン、ノート、コーヒーを俯瞰で静物画のように置く。

## 避けること

3つのポイントをまとめる構図、チェックリストやタスクカード中心の実践構図、過去動画との接続を示す2冊の本、関連動画を見てください、チャンネル登録してください、高評価お願いします、クリック誘導、CTA風の大きな文字、派手な広告バナー、長文テキスト、英語テキスト、意味不明な文字、崩れた日本語、雑然とした机、暗すぎる背景、安っぽいビジネス素材風の人物。

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK / NG
動画全体を温かく締める画像になっている：OK / NG
読後感・余韻・感謝が伝わる：OK / NG
final_message_label が定義されている：OK / NG
closing_emotion が設定されている：OK / NG
closing_type が設定されている：OK / NG
visual_structure が設定されている：OK / NG
supporting_objects が適切：OK / NG
画像内テキストが1要素以内：OK / NG
英語テキストなし：OK / NG
指定外テキストなし：OK / NG
文字量が多すぎない：OK / NG
scene_18の実践画像と役割が混ざっていない：OK / NG
scene_19の関連動画接続画像と役割が混ざっていない：OK / NG
CTA・広告バナー風になっていない：OK / NG
```

# scene_02

## 固定役割

scene_02は、scene_01のクイズの正解を発表し、今回の動画テーマへ自然につなげるシーンである。

## 恒久ルール

- 正解発表シーンにする。
- scene_01の答えを一目で見せる。
- 今回のテーマへ橋渡しする。
- 派手なクイズ番組風にしない。
- 短いテキストで見せる。
- 特定の本・著者・テーマに依存した言葉を固定しない。

## 可変データ

毎回、scene_01とscene_02の原稿、および `image_context.json` から以下を抽出する。

```json
{
  "scene": 2,
  "fixed_role": "クイズ正解発表とテーマへの橋渡し",
  "quiz_correct_answer": "A / B / C のいずれか",
  "answer_short_label": "正解の内容を短く表す言葉",
  "theme_bridge_label": "今回の動画テーマに接続する短い言葉",
  "exact_text_elements": ["正解は〇", "答えの短い内容", "テーマ接続キーワード"]
}
```

## プロンプト必須文

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.

## 最終チェック

- 固定役割と可変内容が分離されているか。
- 正解記号・答えの内容・テーマ接続語は原稿から生成されているか。
- 特定動画の語句が恒久テンプレートに固定されていないか。

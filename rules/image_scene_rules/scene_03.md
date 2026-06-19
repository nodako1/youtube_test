# scene_03

## 固定役割

scene_03は、今回紹介する本を視覚的に見せ、動画全体の結論や読む価値を短く伝えるシーンである。

## 恒久ルール

- 現在のブックカバーを大きく表示する。
- AIにブックカバーを再生成させない。
- 実際のbook_cover画像を使用する。
- 背景はBook Baseらしい水彩・高級感のあるデスク風にする。
- 本紹介シーンとして機能させる。
- book_coverパスは固定せず、毎回 `input/YYYYMMDD_book_cover.*` から動的に取得する。

## 可変データ

毎回、input内の現在日付ファイルと原稿から以下を抽出する。

```json
{
  "scene": 3,
  "fixed_role": "今回の本紹介と動画全体の結論提示",
  "current_book_cover_path": "現在の本のbook_cover画像パス",
  "book_title": "現在の本のタイトル",
  "author_name": "現在の著者名",
  "short_value_message": "動画全体の結論を短く表す言葉",
  "exact_text_elements": ["今回の一冊", "短い価値メッセージ"]
}
```

## プロンプト必須文

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.

## 最終チェック

- 実ブックカバー合成用の余白があるか。
- 固定パスや特定タイトルをテンプレートに入れていないか。
- 価値メッセージは今回の原稿から生成されているか。

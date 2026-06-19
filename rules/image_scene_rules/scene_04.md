# scene_04

## 固定役割

scene_04は、著者紹介と、動画で扱う3つの重要ポイントの見取り図を示すシーンである。

## 恒久ルール

- 著者参考画像があれば使う。
- 著者写真をそのまま貼らず、水彩画風の上品な著者イラストにする。
- 著者画像がなければ、顔を想像せずシルエットや本のモチーフにする。
- 3つの重要ポイントを短いカードで見せる。
- 長文の著者経歴は入れない。
- author画像パスは固定せず、毎回 `input/YYYYMMDD_author.*` から動的に取得する。

## 可変データ

毎回、現在の原稿とinputから以下を抽出する。

```json
{
  "scene": 4,
  "fixed_role": "著者紹介と3つの重要ポイント提示",
  "author_reference_path": "現在のauthor画像パス。なければnull",
  "author_name": "現在の著者名",
  "point_1_label": "重要ポイント①を短く表す言葉",
  "point_2_label": "重要ポイント②を短く表す言葉",
  "point_3_label": "重要ポイント③を短く表す言葉",
  "exact_text_elements": ["著者紹介", "3つの重要ポイント", "①〇〇", "②〇〇", "③〇〇"]
}
```

## プロンプト必須文

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text.

## 最終チェック

- 3つのポイントは毎回の原稿から生成されているか。
- 著者名・画像パス・ポイント語句を固定していないか。
- scene_03の本中心構図と差別化されているか。

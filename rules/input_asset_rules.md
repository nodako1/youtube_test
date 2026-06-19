# Book Base input直下配置ルール

## 目的

Book Base自動化では、ユーザーの運用負荷を下げるため、`assets/` フォルダは使用しない。
テキストファイル、ブックカバー画像、著者画像、過去動画用素材は、すべて `input/` 直下に配置する。
Codexは、ファイル名の先頭8桁の日付と拡張子を読み取り、今回の動画用素材か、scene_19で使う過去動画・関連動画用素材かを判定する。

## 基本方針

```text
input/
├── YYYYMMDD_author.jpg
├── YYYYMMDD_book_cover.webp
├── YYYYMMDD_今回の本タイトル.rtfd.zip
├── YYYYMMDD_過去動画の本タイトル.rtfd.zip
└── YYYYMMDD_book_cover.webp
```

日付はファイル名の先頭8桁で判定する。実行日の日本時間を基準に、今日の日付を `YYYYMMDD` 形式で取得する。
今日の日付が付いているファイルは今回の動画で扱う素材、今日より前の日付が付いているファイルはscene_19で紹介する過去動画・関連動画用素材とする。

## 今回の本の原稿材料

```text
YYYYMMDD_本タイトル.rtfd.zip
```

判定条件は、ファイル名の先頭8桁が今日の日付、拡張子が `.rtfd.zip`、ファイル名に `book_cover` や `author` を含まないこと。
Codexはこの `.rtfd.zip` を解凍し、中の `.rtf` または `.txt` からテキストを読み取って原稿作成に使用する。

## 今回の本のブックカバー

```text
YYYYMMDD_book_cover.webp
```

判定条件は、ファイル名の先頭8桁が今日の日付、ファイル名が `YYYYMMDD_book_cover`、拡張子が `.webp`, `.png`, `.jpg`, `.jpeg` のいずれかであること。
scene_03とサムネイルA/B/Cで使用する。存在しない場合、scene_03画像とサムネイル生成は `needs_review` とし、架空のブックカバーは作らない。

## 今回の著者画像

```text
YYYYMMDD_author.jpg
```

判定条件は、ファイル名の先頭8桁が今日の日付、ファイル名が `YYYYMMDD_author`、拡張子が `.jpg`, `.jpeg`, `.png`, `.webp` のいずれかであること。
scene_04で著者イラストを作成するための参考画像として扱う。任意だが推奨とし、存在しない場合は著者の顔を想像で描かず、人物シルエット、本、3つの重要ポイントを中心にした構図で代替する。

## scene_19用の過去動画・関連動画の原稿材料

```text
YYYYMMDD_過去動画の本タイトル.rtfd.zip
```

判定条件は、ファイル名の先頭8桁が今日より前の日付、拡張子が `.rtfd.zip`、ファイル名に `book_cover` や `author` を含まないこと。
Codexはこのファイルをscene_19用の関連動画素材として読み取り、今回の動画の内容と過去動画の内容がどうつながるかを判断し、scene_19の原稿と画像に反映する。

## scene_19用の過去動画ブックカバー

```text
YYYYMMDD_book_cover.webp
```

判定条件は、ファイル名の先頭8桁が今日より前の日付、ファイル名が `YYYYMMDD_book_cover`、拡張子が `.webp`, `.png`, `.jpg`, `.jpeg` のいずれかであること。
scene_19画像で使用し、今回の本と過去の本が自然につながっている構図にする。

## 複数ファイルがある場合のルール

- 今日の日付の `.rtfd.zip` が複数ある場合、処理を停止し `needs_review` とする。
- 今日の日付の `book_cover` が複数ある場合、処理を停止し `needs_review` とする。
- 過去日付の `.rtfd.zip` が複数ある場合、処理を停止し `needs_review` とする。
- 過去日付の `book_cover` が複数ある場合、処理を停止し `needs_review` とする。

## scene_11 と scene_15 の人物画像について

以下の画像はinputに置かない。

```text
scene_11_story_person_reference.png
scene_15_quote_person_reference.png
```

scene_11で使う有名人・経営者・歴史上の人物、scene_15で使う名言の人物は、原稿生成後にCodexが内容に合わせて選定・検索・確認する。

## 処理後のファイル移動

処理が成功した場合、Codexは今回使用したinputファイルをすべて `archive/` に移動する。処理成功後、`input/` は空になる想定。
処理に失敗した場合は、使用対象ファイルを `error/` に移動し、エラー原因が分かるように `error_report.md` を出力する。

## quality_report.md に記録する内容

```text
【inputファイル判定】

実行日：
今日の日付キー：

今回の原稿材料：
今回のブックカバー：
今回の著者画像：
scene_19用原稿材料：
scene_19用ブックカバー：

【判定結果】
今回の原稿材料：OK / MISSING / DUPLICATED
今回のブックカバー：OK / MISSING / DUPLICATED
今回の著者画像：OK / MISSING / OPTIONAL
scene_19用原稿材料：OK / MISSING / DUPLICATED
scene_19用ブックカバー：OK / MISSING / DUPLICATED
```

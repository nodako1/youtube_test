# Book Base 入力ファイル構成・人物画像取得ルール

## 目的

Book Base自動化では、動画ごとの入力フォルダに、原稿作成用のメモと必要な画像素材を配置する。
scene_11 と scene_15 に登場する人物は原稿作成後に決まるため、ユーザーが事前に人物画像を格納する運用にはしない。
scene_11 と scene_15 の人物画像は、原稿生成後に確定した人物名をもとに検索・確認し、画像生成または画像プロンプト作成に反映する。

## 最新の入力フォルダ構成

```text
input/
└── YYYYMMDD_book_slug/
    ├── source.txt
    ├── scene_19_related_video.txt
    └── assets/
        ├── scene_03_current_book_cover.png
        ├── scene_04_author_reference.png
        └── scene_19_related_book_cover.png
```

## ユーザーが事前に用意するファイル

### 必須ファイル

```text
source.txt
assets/scene_03_current_book_cover.png
scene_19_related_video.txt
assets/scene_19_related_book_cover.png
```

### 任意だが推奨

```text
assets/scene_04_author_reference.png
```

### ユーザーが事前に用意しないファイル

```text
assets/scene_11_story_person_reference.png
assets/scene_15_quote_person_reference.png
```

scene_11 と scene_15 の人物は、原稿作成後にCodexが対象人物を確定し、検索・確認して画像生成に反映する。

## 各ファイルの役割

| ファイル名 | 役割 |
| --- | --- |
| `source.txt` | 本の内容・読書メモ・原稿作成の材料 |
| `assets/scene_03_current_book_cover.png` | 今回紹介する本のブックカバー。scene_03とサムネイルで使用 |
| `assets/scene_04_author_reference.png` | 著者イラスト作成用の参考画像。任意だが推奨 |
| `scene_19_related_video.txt` | scene_19で接続する過去動画・関連動画の情報 |
| `assets/scene_19_related_book_cover.png` | scene_19で紹介する過去動画・関連動画側の本のブックカバー |

## scene_11 の人物取得ルール

scene_11 は、重要ポイント②を補強する実話エピソードを入れるシーンである。
Codexは原稿生成時に、重要ポイント②を補強できる実話エピソードを選び、人物名・エピソード概要・出典情報を記録する。
事実確認できない逸話、出典不明の美談、重要ポイント②とつながらない人物紹介は使わない。
人物画像が取得できない場合は顔を想像で描かず、人物シルエット、行動場面、歴史的・ビジネス的な象徴モチーフで代替する。

出力記録は以下に保存する。

```text
research/scene_11_story_person.md
```

## scene_15 の人物取得ルール

scene_15 は、重要ポイント③を補強する名言を入れるシーンである。
Codexは原稿生成時に、重要ポイント③を補強できる名言を選び、発言者・原文・文脈を確認する。
誤引用が多い名言や出典が確認できない名言は避け、必要なら別の名言に差し替える。
人物画像が取得できない場合は顔を想像で描かず、名言カード、ノートに書かれた短い言葉、本とペン、静かな読書空間で代替する。

出力記録は以下に保存する。

```text
research/scene_15_quote_person.md
```

## scene_19 関連動画情報の入力ルール

scene_19では、ユーザーが事前に指定した過去動画・関連動画へ接続する。
ユーザーは以下の2つを事前に用意する。

```text
scene_19_related_video.txt
assets/scene_19_related_book_cover.png
```

`scene_19_related_video.txt` は以下の形式で入力する。

```text
関連動画タイトル：
関連動画で紹介した本：
著者名：
今回の動画とのつながり：
scene_19で伝えたい接続文：
関連動画URL：
```

URLがない場合は空欄でもよい。ただし、関連動画タイトル、関連動画で紹介した本、今回の動画とのつながりは必須とする。
scene_19 の原稿では、単なる宣伝ではなく、今回の動画と過去動画・関連動画がなぜつながるのかを自然に説明する。
scene_19 の画像では `assets/scene_19_related_book_cover.png` を使い、今回の本とのつながりを視覚的に表現する。

## quality_report.mdへの記録

```text
【入力ファイルチェック】

source.txt：OK / MISSING
scene_19_related_video.txt：OK / MISSING
scene_03_current_book_cover：OK / MISSING
scene_04_author_reference：OK / MISSING / OPTIONAL
scene_19_related_book_cover：OK / MISSING

【自動取得情報チェック】

scene_11_story_person：OK / NEEDS_REVIEW
scene_11_story_person_source：OK / NEEDS_REVIEW
scene_15_quote_person：OK / NEEDS_REVIEW
scene_15_quote_source：OK / NEEDS_REVIEW
```

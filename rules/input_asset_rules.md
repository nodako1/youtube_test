# Book Base 入力ファイル判定・人物画像取得ルール

## 目的

Book Base自動化では、GitHub上の`input/`直下に置かれた日付付き素材ファイルをもとに、動画ごとの原稿・画像プロンプト・画像ファイル・品質レポートを生成する。
サブフォルダは作らず、ファイル名の先頭8桁の日付と、ファイル名・拡張子から役割を判定する。

## 最新の入力ファイル構成

```text
input/
├── 今日の日付_author.jpg
├── 今日の日付_book_cover.webp
├── 今日の日付_今回の本タイトル.rtfd.zip
├── 過去日付_関連動画の本タイトル.rtfd.zip
└── 過去日付_book_cover.webp
```

具体例：

```text
input/
├── 20260619_author.jpg
├── 20260619_book_cover.webp
├── 20260619_否定しない言い換え事典.rtfd.zip
├── 20260616_雑談する人はなぜかうまくいく.rtfd.zip
└── 20260616_book_cover.webp
```

## 今日の日付が付いたファイル

今日の日付が付いたファイルは、今回の動画用素材として扱う。

```text
YYYYMMDD_author.jpg / .jpeg / .png / .webp
→ 今回の著者参考画像。scene_04で使用。

YYYYMMDD_book_cover.webp / .png / .jpg / .jpeg
→ 今回の本のブックカバー。scene_03とサムネイルで使用。

YYYYMMDD_本タイトル.rtfd.zip
→ 今回の動画の原稿材料。
```

## 過去日付が付いたファイル

今日より前の日付が付いたファイルは、scene_19で紹介する過去動画・関連動画用素材として扱う。

```text
過去日付_本タイトル.rtfd.zip
→ scene_19で紹介する過去動画・関連動画の内容。

過去日付_book_cover.webp / .png / .jpg / .jpeg
→ scene_19で使う過去動画・関連動画のブックカバー。
```

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

## quality_report.mdへの記録

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

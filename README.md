# Book Base Automation

Book Base向けのYouTube制作補助ツールです。Koichiさんが`input/`直下に日付付きの原稿素材・ブックカバー・著者画像・過去動画素材を置くと、定時実行で原稿・タイトル・説明文・サムネイル案・画像プロンプト・人物確認メモ・品質レポートを生成します。

YouTube投稿は自動化せず、人間が確認してから手動投稿する前提です。

## フォルダ構成

```text
input/       未処理の本テキスト・画像素材を直下に置く
processing/  処理中ファイルの一時置き場
output/      生成結果を動画単位で保存
archive/     処理済み入力ファイルを保管
error/       失敗したファイルとエラーレポートを保存
rules/       Book Baseの制作ルール
src/         自動化コード
```

## 入力ファイル構成

`assets/`フォルダは使いません。すべて`input/`直下に置きます。ファイル名の先頭8桁の日付で、今回の動画用かscene_19の関連動画用かを判定します。

```text
input/
├── YYYYMMDD_author.jpg
├── YYYYMMDD_book_cover.webp
├── YYYYMMDD_今回の本タイトル.rtfd.zip
├── YYYYMMDD_過去動画の本タイトル.rtfd.zip
└── YYYYMMDD_book_cover.webp
```

実行日の日本時間と同じ日付のファイルは今回の動画素材、今日より前の日付のファイルはscene_19の過去動画・関連動画素材として扱います。

例：

```text
input/
├── 20260619_author.jpg
├── 20260619_book_cover.webp
├── 20260619_否定しない言い換え事典.rtfd.zip
├── 20260616_雑談する人はなぜかうまくいく.rtfd.zip
└── 20260616_book_cover.webp
```

必須ファイルは、今日の日付の`.rtfd.zip`、今日の日付の`book_cover`画像、過去日付の`.rtfd.zip`、過去日付の`book_cover`画像です。今日の日付の`author`画像は任意ですが推奨です。

`scene_11_story_person_reference.png`と`scene_15_quote_person_reference.png`は置きません。scene_11とscene_15の人物は、原稿生成後に選定・出典確認し、`research/`配下に確認メモを出力します。

## 実行方法

AI APIを使わず、ローカルの動作確認用下書きを生成する場合：

```bash
python -m bookbase_automation.cli --root . --allow-fallback
```

本番実行ではフォールバック生成を誤って使わないよう、必ずOpenAI APIを有効にします：

```bash
OPENAI_API_KEY=... python -m bookbase_automation.cli --root . --use-ai
```

## 出力例

```text
output/
└── 2026-06-19_否定しない言い換え事典/
    ├── 00_input.txt
    ├── 01_script.md
    ├── 02_titles.md
    ├── 03_description.md
    ├── 04_thumbnail_ideas.md
    ├── 05_image_prompts.json
    ├── 06_thumbnail_comments.md
    ├── metadata.md
    ├── research/
    │   ├── scene_11_story_person.md
    │   └── scene_15_quote_person.md
    ├── images/
    ├── thumbnails/
    └── quality_report.md
```

## 定時実行

`.github/workflows/daily.yml`により、GitHub Actions上で毎日7:00 JSTに実行できます。GitHub Actionsの本番実行ではフォールバック生成を使わず、Repository Secretsの`OPENAI_API_KEY`が未設定の場合は失敗させます。

## v1の範囲

- `input/`直下の日付付きファイル判定
- 1回につき1本の動画素材を処理
- `.rtfd.zip`から原稿素材を抽出
- `processing/`への移動
- 20シーン原稿生成
- タイトル案A/B/C生成
- 50〜60文字の説明文生成
- サムネイル案A/B/C生成
- 20シーン分の画像プロンプト生成
- scene_11の実話人物・scene_15の名言人物の確認メモ生成
- scene_19関連動画素材と関連本カバーの参照
- 各シーン180〜220字、全体3600〜4400字の品質チェック
- 50〜60文字説明文の品質チェック
- シーン19固定開始文の品質チェック
- タイトルの【】フック重複チェック
- `quality_report.md`生成
- 成功時は使用済みinputファイルを`archive/`へ移動
- 失敗時は使用対象ファイルを`error/`へ移動

画像ファイルそのものの生成はv2で追加する想定です。

# Book Base Automation

Book Base向けのYouTube制作補助ツールです。Koichiさんが本の内容をまとめた動画別フォルダを`input/`に置くと、定時実行で原稿・タイトル・説明文・サムネイル案・画像プロンプト・人物確認メモ・品質レポートを生成します。

YouTube投稿は自動化せず、人間が確認してから手動投稿する前提です。

## フォルダ構成

```text
input/       未処理の本テキストを置く
processing/  処理中ファイルの一時置き場
output/      生成結果を動画単位で保存
archive/     処理済み入力ファイルを保管
error/       失敗したファイルとエラーレポートを保存
rules/       Book Baseの制作ルール
src/         自動化コード
```

## 入力フォルダ構成

1本の動画につき、推奨形式は以下です。

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

必須ファイルは`source.txt`、`scene_19_related_video.txt`、`assets/scene_03_current_book_cover.png`、`assets/scene_19_related_book_cover.png`です。`assets/scene_04_author_reference.png`は任意ですが推奨です。

`scene_11_story_person_reference.png`と`scene_15_quote_person_reference.png`は事前に置きません。scene_11とscene_15の人物は、原稿生成後に選定・出典確認し、`research/`配下に確認メモを出力します。

`scene_19_related_video.txt`は以下の形式で記入します。

```text
関連動画タイトル：
関連動画で紹介した本：
著者名：
今回の動画とのつながり：
scene_19で伝えたい接続文：
関連動画URL：
```

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
└── 2026-06-18_新版思考の整理学/
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

- `input/`の動画別フォルダ確認
- 1回につき1ファイル処理
- `processing/`への移動
- 20シーン原稿生成
- タイトル案A/B/C生成
- 50〜60文字の説明文生成
- サムネイル案A/B/C生成
- 20シーン分の画像プロンプト生成
- scene_11の実話人物・scene_15の名言人物の確認メモ生成
- scene_19関連動画情報と関連本カバーの参照
- 各シーン180〜220字、全体3600〜4400字の品質チェック
- 50〜60文字説明文の品質チェック
- シーン19固定開始文の品質チェック
- タイトルの【】フック重複チェック
- `quality_report.md`生成
- 成功時は`archive/`へ移動
- 失敗時は`error/`へ移動

画像ファイルそのものの生成は、input直下運用で`--generate-images`を指定した場合にOpenAI Images APIで実行できます。

## input直下運用とOpenAI画像生成

`assets/`フォルダや`source.txt`を使わず、`input/`直下のファイル名から役割を判定する運用にも対応しています。
ファイル名の先頭8桁を日付キーとして扱います。

```text
input/
├── 20260619_author.jpg
├── 20260619_book_cover.webp
├── 20260619_否定しない言い換え事典.rtfd.zip
├── 20260616_雑談する人はなぜかうまくいく.rtfd.zip
└── 20260616_book_cover.webp
```

判定ルールは以下です。

- 今日の日付の `.rtfd.zip`：今回の動画の原稿材料
- 今日の日付の `_book_cover` 画像：今回の本のブックカバー。`scene_03`とサムネイルで参照
- 今日の日付の `_author` 画像：今回の著者参考画像。`scene_04`で参照。任意
- 過去日付の `.rtfd.zip`：`scene_19`で紹介する過去動画・関連動画の内容
- 過去日付の `_book_cover` 画像：`scene_19`で紹介する過去動画・関連動画のブックカバー

OpenAI APIで画像ファイルを生成する場合は、環境変数`OPENAI_API_KEY`を設定し、`--generate-images`を指定します。
画像生成はOpenAI Images APIを使用し、参照画像がある場合は画像編集エンドポイント、参照画像がない場合は画像生成エンドポイントを使います。

まず`scene_03`だけをテスト生成する場合：

```bash
PYTHONPATH=src python -m bookbase_automation.cli --root . --use-ai --generate-images --image-scene03-only
```

全20シーンとサムネイル3枚を生成する場合：

```bash
PYTHONPATH=src python -m bookbase_automation.cli --root . --use-ai --generate-images
```

出力例：

```text
output/
└── YYYY-MM-DD_book_slug/
    ├── script.md
    ├── image_prompts.md
    ├── metadata.md
    ├── quality_report.md
    ├── failed_images.md
    ├── research/
    │   ├── scene_11_story_person.md
    │   └── scene_15_quote_person.md
    ├── images/
    │   ├── scene_01.png
    │   ├── scene_02.png
    │   ├── scene_03.png
    │   └── scene_20.png
    └── thumbnails/
        ├── thumbnail_A_loss_aversion.png
        ├── thumbnail_B_benefit.png
        └── thumbnail_C_curiosity.png
```

画像生成に失敗しても処理全体は止めず、成功した画像は保存し、失敗した画像は`failed_images.md`と`quality_report.md`に記録します。
`scene_11`と`scene_15`の人物画像はinputでは受け取らず、原稿・確認メモに基づき、確認が弱い場合は顔を想像せずシルエットや象徴表現、名言カード、静物構図へフォールバックします。

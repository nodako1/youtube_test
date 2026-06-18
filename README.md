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

画像ファイルそのものの生成はv2で追加する想定です。

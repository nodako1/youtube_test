# Book Base Automation

Book Base向けのYouTube制作補助ツールです。Koichiさんが本の内容をまとめた`.txt`ファイルを`input/`に置くと、定時実行で原稿・タイトル・説明文・サムネイル案・画像プロンプト・品質レポートを生成します。

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

## 入力ファイル名

推奨形式は以下です。

```text
YYYYMMDD_書籍名.txt
```

例：

```text
20260618_新版思考の整理学.txt
```

## 実行方法

AI APIを使わず、動作確認用の下書きを生成する場合：

```bash
python -m bookbase_automation.cli --root .
```

OpenAI APIで生成する場合：

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
    ├── images/
    ├── thumbnails/
    └── quality_report.md
```

## 定時実行

`.github/workflows/daily.yml`により、GitHub Actions上で毎日7:00 JSTに実行できます。GitHub ActionsでAI生成を使う場合は、Repository Secretsに`OPENAI_API_KEY`を設定してください。

## v1の範囲

- `input/`の`.txt`確認
- 1回につき1ファイル処理
- `processing/`への移動
- 20シーン原稿生成
- タイトル案A/B/C生成
- 50〜60文字の説明文生成
- サムネイル案A/B/C生成
- 20シーン分の画像プロンプト生成
- `quality_report.md`生成
- 成功時は`archive/`へ移動
- 失敗時は`error/`へ移動

画像ファイルそのものの生成はv2で追加する想定です。

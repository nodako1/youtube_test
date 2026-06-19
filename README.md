# Book Base Automation

Book Base向けのYouTube制作補助ツールです。GitHub上で`input/`直下に日付付き素材ファイルをアップロードし、GitHub Actionsで原稿・タイトル・説明文・コメント・画像プロンプト・動画内画像・サムネイル画像・人物確認メモ・品質レポートを生成します。

YouTube投稿は自動化せず、人間が確認してから手動投稿する前提です。ユーザーがMacのターミナルでコマンドを実行する必要はありません。

## フォルダ構成

```text
input/       未処理の素材ファイルを置く
output/      生成結果を動画単位で保存
archive/     処理済み入力ファイルを保管
error/       失敗したファイルとエラーレポートを保存
rules/       Book Baseの制作ルール
src/         自動化コード
```

## 入力ファイルの置き方

ユーザーは、GitHub上の`input/`直下にファイルをアップロードします。サブフォルダは作りません。

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

## ファイルの意味

```text
20260619_author.jpg
→ 今回の著者画像。scene_04で使用。

20260619_book_cover.webp
→ 今回の本のブックカバー。scene_03とサムネイルで使用。

20260619_否定しない言い換え事典.rtfd.zip
→ 今回の動画の原稿材料。

20260616_雑談する人はなぜかうまくいく.rtfd.zip
→ scene_19で紹介する過去動画の内容。

20260616_book_cover.webp
→ scene_19で使う過去動画のブックカバー。
```

## 判定ルール

ファイル名の先頭8桁の日付と、ファイル名・拡張子から役割を判定します。

### 今日の日付が付いたファイル

今日の日付が付いたファイルは、今回の動画用素材として扱います。

```text
YYYYMMDD_author.jpg / .jpeg / .png / .webp
→ 今回の著者参考画像。scene_04で使用。

YYYYMMDD_book_cover.webp / .png / .jpg / .jpeg
→ 今回の本のブックカバー。scene_03とサムネイルで使用。

YYYYMMDD_本タイトル.rtfd.zip
→ 今回の動画の原稿材料。
```

### 過去日付が付いたファイル

今日より前の日付が付いたファイルは、scene_19で紹介する過去動画・関連動画用素材として扱います。

```text
過去日付_本タイトル.rtfd.zip
→ scene_19で紹介する過去動画・関連動画の内容。

過去日付_book_cover.webp / .png / .jpg / .jpeg
→ scene_19で使う過去動画・関連動画のブックカバー。
```

scene_11とscene_15の人物画像は`input/`では受け取りません。原稿生成後に対象人物・出典確認メモを`research/`配下へ出力し、確認が弱い場合は顔を想像せず、シルエット・象徴表現・名言カード・静物構図で代替します。

## GitHub Actionsでの運用

1. GitHub上で`input/`直下に素材ファイルをアップロードする
2. `Actions`タブを開く
3. `Book Base automation` workflowを選ぶ
4. `Run workflow`を押す
5. 処理完了後、`output/`を確認する
6. 使用済みファイルは`archive/`に移動される
7. 成功時、`input/`は空になる
8. エラー時は`error/`と`error_report.md`を確認する

workflowは手動実行に加え、毎日JST 7:00（UTC 22:00）にも実行できます。

GitHub Actions内では以下のコマンドを実行します。ユーザーがローカルで実行する必要はありません。

```bash
PYTHONPATH=src python -m bookbase_automation.cli --root . --use-ai --generate-images
```

## GitHub Actionsの処理内容

workflowでは以下を行います。

1. repositoryをcheckoutする
2. Pythonをセットアップする
3. OpenAI API用の依存関係をインストールする
4. `OPENAI_API_KEY`をGitHub Secretsから読み込む
5. 原稿生成・画像プロンプト生成・画像ファイル生成を実行する
6. `input/`、`output/`、`archive/`、`error/`の変更を確認する
7. 変更がある場合は`Generate Book Base assets for YYYYMMDD`の形式でcommit & pushする

GitHub Actionsの実行環境は一時的なため、処理後にcommit & pushしないと生成結果やファイル移動結果はGitHub上に残りません。

## Secrets

Repository Secretsに以下を設定してください。

```text
OPENAI_API_KEY
```

`OPENAI_API_KEY`が存在しない場合、画像生成は成功しません。その場合は処理対象ファイルを`error/`に移動し、`error_report.md`にエラー内容を記録します。

## 処理後の状態

成功時：

```text
input/
└── 空

output/
└── YYYYMMDD_book_slug/
    ├── script.md
    ├── metadata.md
    ├── image_prompts.md
    ├── quality_report.md
    ├── images/
    │   ├── scene_01.png
    │   └── scene_20.png
    └── thumbnails/
        ├── thumbnail_A_loss_aversion.png
        ├── thumbnail_B_benefit.png
        └── thumbnail_C_curiosity.png

archive/
└── YYYYMMDD_book_slug/
    ├── 使用済みinputファイル一式
```

失敗時：

```text
error/
└── YYYYMMDD_book_slug/
    ├── error_report.md
    └── 使用対象ファイル一式
```

画像生成に失敗しても、成功した画像や生成済みの原稿・メタデータは可能な範囲で残し、失敗した画像は`failed_images.md`と`quality_report.md`に記録します。

# scene_07

scene_07は、重要ポイント①を現在の本や原稿に合った研究・データ・公的情報・調査結果・実績などで補強するシーンである。scene_05〜06で説明した重要ポイント①について、「これはただの感覚論ではなく、根拠がある話なんだ」と視聴者に伝える。

## 固定役割

scene_07の固定役割は「重要ポイント①の根拠補強」。具体的な根拠内容は、毎回の原稿・調査結果から抽出する。

## 固定してはいけないもの

以下をテンプレートに固定しない。

- 心理学研究
- 脳科学研究
- お金のデータ
- 時間術の調査
- 健康統計
- コミュニケーション学
- 特定の論文名
- 特定の機関名
- 特定の数字

## scene_07 可変データ構造

scene_07用に以下を毎回作成する。

```json
{
  "scene": 7,
  "fixed_role": "重要ポイント①の根拠補強",
  "point_1_label": "重要ポイント①を短く表す言葉",
  "scene_07_core_message": "根拠によって補強したい一番大事な内容",
  "evidence_type": "research / survey / public_data / report / experiment / case_data / book_claim のいずれか",
  "evidence_label": "根拠の種類を短く表す言葉",
  "key_finding_label": "根拠から分かることを短く表す言葉",
  "source_confidence": "verified / needs_review / unavailable",
  "visual_structure": "evidence_card / data_report / research_board / document_review / chart_focus のいずれか",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## evidence_type

- `research`：論文・研究・実験などで補強する場合。
- `survey`：アンケート調査や読者・利用者調査で補強する場合。
- `public_data`：官公庁・公的機関・統計データで補強する場合。
- `report`：企業レポート・業界レポート・市場調査で補強する場合。
- `case_data`：実例や実績データで補強する場合。
- `book_claim`：外部根拠が弱く、本書内の主張を整理して補強する場合。断定しない。

## source_confidence

- `verified`：根拠が確認できている。画像内に「研究データ」「調査結果」「公的データ」などの短い根拠ラベルを使ってよい。
- `needs_review`：根拠の確認が不十分。「研究で証明」「検証済み」「科学的に証明」は避け、「根拠を確認」「データで見る」「参考データ」にする。
- `unavailable`：外部根拠が見つからない。架空の研究や数字を作らず、`quality_report.md` に `NEEDS_REVIEW` を記録する。

## 画像内テキスト

画像内テキストは3つ以内にする。基本形式は以下。

1. 根拠ラベル
2. 重要ポイント①の短い言葉
3. 結論ラベル

ただし、固定文言にせず、現在の原稿から生成する。

## 数字・グラフ

禁止：

- 実在しない数字を大きく表示する。
- 架空の割合を表示する。
- 出典不明のグラフを本物のように見せる。
- 特定の研究機関名を確認なしで入れる。
- 「科学的に証明」と断定する。

OK：

- 抽象化された棒グラフ。
- 出典名のない資料カード。
- 根拠を象徴するレポート。
- 小さなグラフアイコン。
- 確認済みの場合のみ、短い数字や出典風ラベル。

## 推奨構図

- evidence_card：中央に大きな evidence card。周囲に資料、レポート、グラフを配置。人物は小さめ、または不要。
- data_report：左側に資料・グラフ、右側に重要ポイント①の短い結論。根拠から結論へ視線が流れる。
- research_board：ホワイトボードや資料ボードに、短い根拠ラベルと簡単な図。文字は少なく上品にする。
- document_review：会社員が落ち着いて資料を確認している。机上にグラフ、レポート、データカード。重要な根拠ラベルを1つだけ強調。
- chart_focus：抽象化されたチャートで裏付けを象徴する。詳細な数字は入れない。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Leave the lower-left corner clean because the fixed Book Base logo will be composited after generation.

This is Scene 07. Its fixed role is to reinforce Key Point 1 with evidence, such as research, survey results, public data, reports, experiments, or documented examples. The evidence type must be based on the current script and current research data. Do not hard-code psychology research or any topic from a previous book. Do not invent specific numbers, sources, or study names.

Current Key Point 1:
{point_1_label}

Current Scene 07 core message:
{scene_07_core_message}

Evidence type:
{evidence_type}

Source confidence:
{source_confidence}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. {evidence_label}
2. {point_1_label}
3. {key_finding_label}

Visual structure:
{visual_structure}

Composition:
{scene_07_composition}

Visual motifs:
- elegant evidence card
- report documents
- simple abstract charts
- calm business desk
- subtle data icons
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal text only. Do not place long script text. Avoid clutter, avoid fake detailed charts, avoid invented statistics, avoid hard-coded psychology research, and avoid repeating the Scene 06 composition.
```

## 生成前チェック

1. scene_05の重要ポイント①を取得しているか。
2. scene_07本文から根拠情報を抽出しているか。
3. evidence_type を現在の内容に合わせて選んでいるか。
4. source_confidence を設定しているか。
5. 架空の研究・数字・機関名を入れていないか。
6. scene_06と構図が被っていないか。

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK / NG
重要ポイント①の根拠補強になっている：OK / NG
evidence_type が現在の原稿に基づいている：OK / NG
source_confidence を記録している：OK / NG
過去テーマのハードコードなし：OK / NG
架空の数字・出典なし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_06と構図が違う：OK / NG
generic report image になっていない：OK / NG
```

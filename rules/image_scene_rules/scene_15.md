# scene_15

## 固定役割

重要ポイント③を、名言・引用・一節・思想の要約で補強する。scene_14で具体化した重要ポイント③に対して、「この考え方は、こうした言葉にも通じている」と印象づける。

引用元や発言者が十分に確認できる場合のみ、人物名や人物イメージを限定的に使う。確認が弱い場合は、人物ではなく、quote card / still-life / symbolic composition で表現する。

## 固定してはいけないもの

以下は毎回の原稿と調査結果に基づく可変内容のため、テンプレートに固定しない。

- 特定の名言
- 特定の人物名
- 特定の心理学者名
- 特定の著作名
- 特定テーマの固定フレーズ
- 過去に生成した引用文や英語引用

## 毎回作成する可変データ

scene_15用に以下を毎回作成する。

```json
{
  "scene": 15,
  "fixed_role": "重要ポイント③の引用・名言補強",
  "point_3_label": "重要ポイント③を短く表す言葉",
  "scene_15_core_message": "引用や一節で補強したい内容",
  "quote_source_type": "person / book / public_domain_quote / paraphrase / symbolic_only のいずれか",
  "quote_source_name": "確認できる場合のみ、発言者名または出典名。未確認ならnull",
  "quote_excerpt_label": "画像内に入れる短い引用句または要約句",
  "lesson_label": "重要ポイント③とのつながりを短く表す言葉",
  "attribution_status": "verified / needs_review / unverified",
  "visual_mode": "named_quote / quote_card / still_life / symbolic_quote_scene のいずれか",
  "exact_text_elements": ["短い文字1", "短い文字2", "短い文字3"]
}
```

## attribution_status

- `verified`：引用文または要約元、発言者または出典、重要ポイント③との自然なつながりを確認でき、誤引用の可能性が低い場合のみ。人物名や出典名を画像内に短く入れてよい。
- `needs_review`：有名な言葉として流通しているが原典確認が弱い、要約か直引用か曖昧、人物名や出典名の表示に不安がある場合。人物名は画像に出さず、quote card / still-life / symbolic composition にする。
- `unverified`：出典不明、AI生成の可能性、誰の言葉か不明、引用文として危険な場合。引用として断定せず、必要なら「考え方の要約カード」に切り替える。

## visual_mode

- `named_quote`：verified の場合のみ。短い引用句、発言者名、控えめな象徴的人物表現を使える。ただし参照画像なしに実在人物の顔を正確に再現しない。
- `quote_card`：最も安全な基本形。引用カード、短い引用句、小さな出典ラベルまたは lesson label、余白を活かした静かな構図。
- `still_life`：人物を出さず、本・カード・ノート・ペン・しおり・デスクなどで表現する。
- `symbolic_quote_scene`：光、道、扉、整う机、支え合う手、小さな変化など、言葉の意味を象徴する場面で表現する。

## 引用文・画像内テキスト

- 画像内に長い引用文を入れない。
- `quote_excerpt_label` は原則6〜18文字程度、長くても1行で収まる短い一節にする。
- 直引用に不安がある場合は、要約ラベルにする。
- 画像内テキストは3つ以内にする。
- verified：引用・一節、`quote_excerpt_label`、`quote_source_name`。
- needs_review：印象的な一節、`quote_excerpt_label`、`lesson_label`。
- unverified：考え方のヒント、`quote_excerpt_label`、`lesson_label`。
- 英語テキストを入れない。

## 顔・人物表現

- 参照画像がない場合、実在人物の顔を正確に再現しようとしない。
- 写実的な肖像画にしない。
- 人物を出す場合も、象徴的・控えめにする。
- 顔よりも、言葉の意味や余韻を主役にする。
- `attribution_status` が needs_review / unverified の場合は、人物名や顔を出さない。

## 推奨構図

- 構図A：引用カード型。中央に上品な quote card、短い引用句、下に小さな出典名または lesson label、周囲に本・ノート・しおり。
- 構図B：静物・余白型。ノート、カード、ペン、しおり、本などの still life。短い一節をカードで見せ、余白を多めに使う。
- 構図C：象徴場面型。言葉の意味を象徴する小さな場面。例：一歩進む、整う、開く、受け止める、変わる、続ける。
- 構図D：控えめ人物＋引用型。verified の場合のみ。人物は小さく控えめにし、主役は引用カードにする。

## 推奨プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 15. Its fixed role is to reinforce Key Point 3 with a quotation, short excerpt, notable line, or distilled idea. The quote or idea must be based on the current script and current research. Do not hard-code any quote from a previous book. If attribution is uncertain, do not show a named person or face. Use a quote card, still-life composition, or symbolic quote scene instead.

Current Key Point 3:
{point_3_label}

Current Scene 15 core message:
{scene_15_core_message}

Quote source type:
{quote_source_type}

Attribution status:
{attribution_status}

Visual mode:
{visual_mode}

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. {text_element_1}
2. {text_element_2}
3. {text_element_3}

Composition:
{scene_15_composition}

Visual motifs:
{visual_motifs}

Keep the image clean and easy to understand at a glance. Use minimal Japanese text only. Do not place long script text. Avoid clutter, avoid long verbatim quotes, avoid invented attributions, avoid realistic faces, avoid hard-coded previous-book quotes, and avoid repeating the Scene 14 composition.
```

## quality_report.md への記録

`quality_report.md` に以下を記録する。

```text
【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK / NG
重要ポイント③の引用・一節補強になっている：OK / NG
引用または要約が現在の原稿に基づいている：OK / NG
attribution_status を記録している：OK / NG
attribution が弱い場合に人物名を出していない：OK / NG
attribution が弱い場合に顔を描いていない：OK / NG
長い引用文を入れていない：OK / NG
過去テーマのハードコードなし：OK / NG
指定外テキストなし：OK / NG
文字量が少ない：OK / NG
scene_14と構図が違う：OK / NG
```

## 避けること

- 特定の名言を固定する。
- 特定人物名を固定する。
- 引用文全文を長く載せる。
- 出典不明の名言を断定的に扱う。
- attribution が弱いのに人物名を出す。
- attribution が弱いのに顔を描く。
- 写実的な肖像画。
- ただのノート画像で終わる。
- scene_14の具体例画像と役割が混ざる。
- 英語テキストを入れる。

# scene_05 画像生成品質向上ルール

## このシーンの役割

scene_05 は重要ポイント①の導入シーンです。単なる考えごとシーンではなく、「否定を避けることには心理学的な効果がある」という最初の重要ポイントを一目で伝える入口画像にします。

1. 重要ポイント①の開始を示す。
2. 「否定を避ける心理学的効果」というテーマを見せる。
3. 視聴者に「人は否定されると閉じる、受け入れられると開く」という方向性を伝える。
4. scene_06 の詳しい説明につなぐ。

## コアメッセージ

否定を避けると、相手の心は閉じにくくなり、話を聞いてもらいやすくなる。

## 画像内テキストルール

scene_05 では画像内テキストを最小限にし、以下の日本語テキストだけを使います。

```text
重要ポイント①
否定しない心理効果
心が開きやすい
```

以下は禁止します。

- 長文説明
- 原稿本文のコピペ
- 「否定されると人は防御的になり…」のような文章表示
- 英語テキスト
- 箇条書き3行以上
- 心理学の説明文を細かく載せること

## 推奨構図

### 構図A：対話の空気変化型

左側に少し緊張した会話の空気、右側にやわらいだ対話の空気を置く。中央に会社員1人または2人を配置し、小さく「重要ポイント①」「否定しない心理効果」を入れる。

### 構図B：心が開くイメージ型

中央に会話中の会社員を置き、周囲に閉じた吹き出しから、やわらかく開いた吹き出しへ変化するモチーフを配置する。テキストは短く3つ以内にする。

### 構図C：ポイント導入カード型

左側に大きめのポイントカード「重要ポイント①」、右側にやさしく会話する2人の会社員を配置する。背景はノートや付箋ではなく、会話・印象・心理を象徴する柔らかなモチーフにする。

### 構図D：心理イメージ＋人物型

左に考えこむ会社員、右に受け入れられて安心した相手、中央にやわらかい矢印や光の流れを置く。

## 避けること

- ただ机に向かって考えているだけの人物
- sticky notes と notebook だけで終わる構図
- scene_04 の著者＋3ポイントと似たカード構図
- 長い説明テキスト
- 研究グラフや統計中心の構図（scene_07 寄り）
- サムネイルのような煽り感
- ネガティブすぎる表情
- ドラマチックすぎる感情表現

## 最終プロンプトテンプレート

```text
Create a 16:9 landscape video-insert image for Book Base, a Japanese business book YouTube channel. Use a refined watercolor illustration style with a premium, calm, elegant atmosphere. Use a soft cream-white and beige background with teal and subtle gold accents. Include a small natural Book Base logo placed unobtrusively.

This is Scene 05. Its role is to begin Key Point 1 and clearly introduce the idea that avoiding negation has a psychological effect. The image should show that when people are not immediately否定された, they become more open, less defensive, and more willing to listen. This is the opening image for the first major point, so it should feel clear, calm, and easy to understand at a glance.

Use only the following Japanese text elements exactly as written. Do not add any other Japanese or English text:
1. 重要ポイント①
2. 否定しない心理効果
3. 心が開きやすい

Composition:
{scene_05_composition}

Visual motifs:
- calm Japanese office worker or two office workers in conversation
- gentle speech bubbles or conversation icons
- visual contrast between tense communication and open communication
- subtle arrows, light, or soft transition motifs
- enough whitespace
- premium watercolor texture

Keep the image clean and easy to understand at a glance. Use minimal text only. Do not place long script text. Avoid clutter, avoid research-chart-heavy design, avoid a generic desk-only scene, and avoid repeating the Scene 04 composition.
```

## scene_05 JSON構造

```json
{
  "scene": 5,
  "scene_role": "重要ポイント①の導入。否定を避ける心理学的効果を示す",
  "core_message": "否定を避けると、相手の心が閉じにくくなり、話を聞いてもらいやすくなる",
  "exact_text_elements": [
    "重要ポイント①",
    "否定しない心理効果",
    "心が開きやすい"
  ],
  "composition": "中央に会話する会社員2人を置き、対話の空気がやわらかく変化する様子を見せる",
  "visual_motifs": [
    "会社員",
    "吹き出し",
    "対話アイコン",
    "やわらかな矢印",
    "淡い光"
  ],
  "negative_rules": [
    "机で考えるだけの画像にしない",
    "長文を入れない",
    "研究グラフ中心にしない",
    "scene_04と似た構図にしない",
    "サムネイル風にしない"
  ],
  "final_prompt": "..."
}
```

## quality_report.md への記録

```text
【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK / NG
否定を避ける心理効果が伝わる：OK / NG
一目でメッセージが分かる：OK / NG
文字量が少ない：OK / NG
指定外テキストなし：OK / NG
Book Baseらしい高級感：OK / NG
scene_04と構図が違う：OK / NG
ただの雰囲気画像になっていない：OK / NG
```

## 最重要修正点

scene_05 は「考える人物の雰囲気画像」ではなく、「重要ポイント①＝否定を避ける心理学的効果」の入口画像として作ります。本編のスタート感が大事なので、“重要ポイント①”の見出し感をしっかり持たせます。

from __future__ import annotations

import json
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class GeneratedAssets:
    script: str
    titles: str
    description: str
    thumbnail_ideas: str
    image_prompts: str


def _split_summary(source_text: str, scene_count: int = 20) -> list[str]:
    compact = " ".join(source_text.split())
    if not compact:
        return ["入力本文の要点を追記してください。"] * scene_count
    chunk_size = max(1, len(compact) // scene_count)
    chunks = [compact[i : i + chunk_size] for i in range(0, len(compact), chunk_size)]
    if len(chunks) < scene_count:
        chunks.extend([chunks[-1]] * (scene_count - len(chunks)))
    return chunks[:scene_count]


def _fit_scene(text: str, *, min_chars: int = 180, max_chars: int = 220) -> str:
    filler = "会社員の現実に置き換えると、評価や納期に追われる場面でも、論点を一つずつ整理して行動へ移す助けになります。"
    while len(text) < min_chars:
        text += filler
    return text[:max_chars]


def generate_fallback_assets(source_text: str, book_name: str) -> GeneratedAssets:
    chunks = _split_summary(source_text)
    book_title = book_name.replace("_", " ")
    author = "著者"
    scene_leads = {
        1: "人材サービス会社が社会人に行った調査では、仕事の悩みは知識不足より整理不足から生まれることが多いとされています。では、忙しい会社員が最初に見直すべきものは何でしょうか。A.根性 B.思考の整理 C.残業時間。それでは正解を発表します。",
        2: "正解はBの思考の整理です。数字や調査結果を見ると、会社員の悩みは能力そのものより、情報をどう扱うかで大きく変わります。今回のテーマは、本の内容を仕事の判断に変える方法です。",
        3: f"今回紹介するのは、{author}さんの『{book_title}』こちらの本になります。本書の要点は、知識を増やすだけでなく、目の前の課題に使える形へ整えることです。会社員にとっては、迷いを減らし行動を早める武器になります。",
        4: "著者の経歴で注目したいのは、複雑なテーマを実生活に結びつけて語っている点です。今回の重要ポイントは3つあります。問題を見える化すること、背景を捉えること、最後に小さく実践へ移すことです。",
        5: "重要ポイントの1つ目は問題を見える化することです。仕事で迷う時ほど、原因は能力不足ではなく、考える材料が頭の中で混ざっていることにあります。まず何に困っているのかを言葉にすると、次の行動が見えます。",
        6: "問題を見える化すると、上司の評価、納期、会議の発言なども分けて考えられます。本書のメモでは、感情と事実を切り分ける視点が重要です。不安をそのまま抱えるより、事実を書き出す方が前に進めます。",
        7: "心理学の研究でも、悩みを書き出す行為は認知的負荷を下げると説明されます。公的データや調査でも、仕事のストレスは曖昧な不安で強まりやすいものです。本書の整理法は、科学的にも納得しやすい考え方です。",
        8: f"問題を整理できると、毎日の仕事で無駄に消耗しにくくなります。{ 'このチャンネルでは、話題の本を、日々の仕事や年収アップにどう活かせるかという視点でお届けしています。興味のある方は、ぜひチャンネル登録お願いします。' }",
        9: "重要ポイントの2つ目は原因や背景を捉えることです。目の前の失敗だけを見ると落ち込みますが、背景まで見ると対策が変わります。報連相が遅れたなら、性格ではなく仕組みや優先順位の問題かもしれません。",
        10: "背景を捉える人は、同じ失敗を繰り返しにくくなります。本書の内容も、表面の出来事に反応するのではなく、なぜそうなったのかを見に行く姿勢を重視しています。これは管理職にも若手にも役立つ視点です。",
        11: "実話エピソードとして、経営者が失敗の原因を個人の根性ではなく仕組みで見直す話は多く語られます。たとえば改善を続ける企業ほど、失敗を責めるより記録し、次の判断材料に変えます。",
        12: "背景を見直すと、自分を責めすぎず改善点を探せます。みなさんも仕事で、失敗の原因を後から整理して次に活かせた経験はありますか？もし似たような経験があれば、ぜひコメント欄で教えてください。",
        13: "重要ポイントの3つ目は小さく実践へ移すことです。学びは理解しただけでは変化になりません。会議前に論点を一つ書く、退勤前に明日の判断材料を整理するなど、小さな行動へ落とすことで意味が出ます。",
        14: "小さな実践は、忙しい会社員に向いています。大きな改革を狙うと続きませんが、毎日一つだけ判断を楽にする工夫なら続けやすいです。本書の価値は、読後に仕事の見方が少し変わる点にあります。",
        15: "名言として、ピーター・ドラッカーの言葉に、測定できないものは管理できないという考え方があります。行動も同じで、何を変えるかが見えていなければ続きません。本書の学びも、見える化して初めて実践できます。",
        16: "ここで紹介した以外にも、本書には考え方を整えるヒントが残っています。動画では扱いきれない具体例もあるので、自分の仕事に引き寄せて読むほど発見があります。もし気になった方は、ぜひ本書を手に取ってみてください。",
        17: "今回の内容をおさらいすると、まず問題を見える化し、次に原因や背景を捉え、最後に小さく実践する流れが大切でした。知識を増やすだけでなく、仕事の判断に使える形へ整えることが本書の価値です。",
        18: "明日から実践するなら、まず一つの悩みを紙に書き出してみてください。評価、納期、人間関係のどれが問題なのかを分けるだけでも、行動は選びやすくなります。日常の小さな整理が、判断の速さを変えます。",
        19: "この考え方は、過去動画で扱った習慣化や時間管理のテーマともつながります。考えを整理してから行動するほど、毎日の改善は続きやすくなります。気になる方は、ぜひそちらもあわせてご視聴ください。",
        20: "最後に、本は読むだけで終わらせるより、仕事の一場面に使って初めて力になります。今日の内容から一つだけ選び、明日の判断に活かしてみてください。参考になった方は、高評価やハイプで応援していただけると嬉しいです。それでは、また次回の動画でお会いしましょう。最後までご視聴ありがとうございました。",
    }
    scenes = []
    for index in range(1, 21):
        body = scene_leads[index]
        if index not in {1, 2, 3, 4, 8, 12, 16, 17, 19, 20}:
            body += f" 入力メモの要素として「{chunks[index - 1][:30]}」も踏まえます。"
        scenes.append(f"【シーン{index}】\n{_fit_scene(body)}")

    script = "\n".join(scenes) + "\n"
    titles = "\n".join(
        [
            f"# タイトル案：{book_name}",
            f"A. 【思考が整う】{book_name}を仕事に活かす方法",
            f"B. 【迷いが減る】{book_name}が教える判断の作り方",
            f"C. 【明日から実践】{book_name}の要点を20シーンで解説",
        ]
    ) + "\n"
    description = f"{book_name}の要点を仕事と日常で使える視点に絞り、明日から実践できる行動までわかりやすく丁寧に解説します。"
    thumbnail_ideas = "\n".join(
        [
            "# サムネイル案",
            "A. 悩む会社員の横顔＋大きな文字『思考が整う』",
            "B. 散らかったメモが整理される構図＋文字『迷いが減る本』",
            "C. 本と朝のデスク＋文字『明日から使える知恵』",
        ]
    ) + "\n"
    prompts = [
        {
            "scene": index,
            "prompt": f"Japanese business YouTube illustration, scene {index}, office worker applying book insights, clean cinematic lighting, no text in image",
        }
        for index in range(1, 21)
    ]
    image_prompts = json.dumps(prompts, ensure_ascii=False, indent=2) + "\n"
    return GeneratedAssets(script, titles, description + "\n", thumbnail_ideas, image_prompts)

def generate_ai_assets(source_text: str, book_name: str, rules_text: str, *, model: str) -> GeneratedAssets:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = f"""
Book BaseのYouTube制作補助として、以下の入力本文から成果物を作成してください。
必ずルールを守り、JSONのみを返してください。

書籍名: {book_name}

制作ルール:
{rules_text}

入力本文:
{source_text}

返却JSONキー:
script, titles, description, thumbnail_ideas, image_prompts

scriptは必ず【シーン1】〜【シーン20】形式にし、各シーンの本文はシーン内改行なしの1段落にしてください。
""".strip()
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    text = response.output_text
    data = json.loads(text)
    return GeneratedAssets(
        script=data["script"].rstrip() + "\n",
        titles=data["titles"].rstrip() + "\n",
        description=data["description"].rstrip() + "\n",
        thumbnail_ideas=data["thumbnail_ideas"].rstrip() + "\n",
        image_prompts=json.dumps(data["image_prompts"], ensure_ascii=False, indent=2) + "\n"
        if not isinstance(data["image_prompts"], str)
        else data["image_prompts"].rstrip() + "\n",
    )

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


def generate_fallback_assets(source_text: str, book_name: str) -> GeneratedAssets:
    chunks = _split_summary(source_text)
    scenes = []
    for index, chunk in enumerate(chunks, start=1):
        if index == 1:
            lead = "この本を読むと、日々の悩みの見え方が少し変わります。"
        elif index == 2:
            lead = "結論から言うと、重要なのは知識を増やすことではなく使い方を変えることです。"
        elif index == 8:
            lead = "ここまで役に立つと感じた方は、ぜひチャンネル登録して続きを見逃さないでください。"
        elif index == 12:
            lead = "あなたならこの考えをどんな場面で使いますか。ぜひコメントで教えてください。"
        elif index == 17:
            lead = "ここで全体を総評すると、この本の強みは行動に移しやすい点です。"
        elif index == 19:
            lead = "最後に、今日からできる一歩を整理します。"
        else:
            lead = "この場面で注目したいのは、考え方を現実の行動に落とし込む視点です。"
        scenes.append(f"## Scene {index:02d}\n\n{lead} 本文メモでは「{chunk[:160]}」という要素が確認できます。会社員の日常に置き換えると、判断に迷った時ほど一度立ち止まり、何を優先するかを言語化することが大切です。")

    script = f"# 20シーン原稿：{book_name}\n\n" + "\n\n".join(scenes) + "\n"
    titles = "\n".join(
        [
            f"# タイトル案：{book_name}",
            f"A. 【思考が変わる】{book_name}から学ぶ仕事の判断術",
            f"B. 【人生が軽くなる】{book_name}が教える悩みの整理法",
            f"C. 【明日から使える】{book_name}の本質を20シーンで解説",
        ]
    ) + "\n"
    description = f"{book_name}の要点を仕事と日常で使える視点に絞り、明日から実践できる形で解説します。"
    thumbnail_ideas = "\n".join(
        [
            "# サムネイル案",
            "A. 悩む会社員の横顔＋大きな文字『考え方が変わる』",
            "B. 散らかったメモが整理される構図＋文字『悩みが消える本』",
            "C. 本と朝のデスク＋文字『明日から使える知恵』",
        ]
    ) + "\n"
    prompts = [
        {
            "scene": index,
            "prompt": f"Japanese business YouTube illustration, scene {index}, thoughtful office worker, clean cinematic lighting, book learning theme, no text in image",
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

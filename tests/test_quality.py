from bookbase_automation.quality import SCENE_19_PREFIX, build_quality_report


def _scene(index: int, lead: str = "") -> str:
    base = "これは品質チェック用の本文です。会社員の日常に置き換えて、判断、習慣、行動を具体的に説明します。迷った時に何を優先するかを整理し、小さな一歩へつなげる内容です。視聴者が実践しやすいよう、抽象論ではなく場面を想像できる表現にします。"
    body = lead + base + base
    return f"## Scene {index:02d}\n\n{body[:190]}"


def test_quality_report_checks_latest_rules():
    scenes = []
    for index in range(1, 21):
        lead = ""
        if index == 8:
            lead = "チャンネル登録をお願いします。"
        elif index == 12:
            lead = "コメントで教えてください。"
        elif index == 17:
            lead = "総評として整理します。"
        elif index == 19:
            lead = SCENE_19_PREFIX
        scenes.append(_scene(index, lead))
    script = "# script\n\n" + "\n\n".join(scenes)
    titles = "A. 【思考が変わる】タイトル\nB. 【人生が軽くなる】タイトル\nC. 【明日から使える】タイトル"
    description = "この本の要点を仕事と日常で使える視点に絞り、明日から実践できる行動まで分かりやすく丁寧に解説します。"
    prompts = "\n".join(f'{{"scene": {index}, "prompt": "p"}}' for index in range(1, 21))

    report = build_quality_report(script, titles, prompts, description)

    assert "各シーン180〜220字: OK" in report
    assert "全体3600〜4400字: OK" in report
    assert "50〜60文字説明: OK" in report
    assert "シーン19開始文固定: OK" in report
    assert "タイトルの【】フック重複: OK" in report


def test_quality_report_detects_duplicate_title_hooks():
    report = build_quality_report(
        "## Scene 01\n\n短い本文",
        "A. 【同じ】タイトル\nB. 【同じ】タイトル\nC. 【別】タイトル",
        "",
        "短い説明",
    )

    assert "タイトルの【】フック重複: NG" in report

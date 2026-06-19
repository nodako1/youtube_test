import json

from bookbase_automation.generator import _build_image_prompt_item
from bookbase_automation.quality import (
    SCENE_8_CTA,
    SCENE_16_BOOK_GUIDE,
    SCENE_17_PREFIX,
    SCENE_20_CLOSING,
    build_quality_report,
)


def _fit(text: str) -> str:
    filler = "会社員の現実に置き換えると、評価や納期に追われる場面でも、論点を整理して行動へ移す助けになります。"
    while len(text) < 180:
        text += filler
    return text[:210]


def _valid_script() -> str:
    bodies = {
        1: "人材サービス会社が社会人に行った調査では、仕事の悩みは知識不足より整理不足から生まれることが多いとされています。A.根性 B.思考の整理 C.残業時間。それでは正解を発表します。",
        2: "正解はBの思考の整理です。今回のテーマは、本の内容を会社員の判断に変える方法です。忙しい日常でも、考える順番を整えるだけで行動は選びやすくなります。",
        3: "今回紹介するのは、著者さんの『テスト本』こちらの本になります。本書の結論は、知識を増やすだけでなく、目の前の課題に使える形へ整えることです。会社員にとって判断を助けます。",
        4: "著者の経歴で注目したいのは、複雑なテーマを実生活に結びつけて語っている点です。今回の重要ポイントは3つあり、問題を見える化し、背景を捉え、実践へ移す流れです。",
        5: "重要ポイントの1つ目は問題を見える化することです。仕事で迷う時ほど、原因は能力不足ではなく、考える材料が頭の中で混ざっていることにあります。まず困りごとを言葉にします。",
        6: "問題を見える化すると、上司の評価、納期、会議の発言なども分けて考えられます。本書のメモでは、感情と事実を切り分ける視点が重要です。不安を事実に戻します。",
        7: "心理学の研究でも、悩みを書き出す行為は認知的負荷を下げると説明されます。公的データや調査でも、仕事のストレスは曖昧な不安で強まりやすいものです。",
        8: f"問題を整理できると、毎日の仕事で無駄に消耗しにくくなります。{SCENE_8_CTA}",
        9: "重要ポイントの2つ目は原因や背景を捉えることです。目の前の失敗だけを見ると落ち込みますが、背景まで見ると対策が変わります。報連相の遅れも仕組みで見直せます。",
        10: "背景を捉える人は、同じ失敗を繰り返しにくくなります。本書の内容も、表面の出来事に反応するのではなく、なぜそうなったのかを見に行く姿勢を重視しています。",
        11: "実話エピソードとして、経営者が失敗の原因を個人の根性ではなく仕組みで見直す話は多く語られます。改善を続ける企業ほど、失敗を記録し次の判断材料に変えます。",
        12: "背景を見直すと、自分を責めすぎず改善点を探せます。みなさんも仕事で、失敗の原因を後から整理して次に活かせた経験はありますか？もし似たような経験があれば、ぜひコメント欄で教えてください。",
        13: "重要ポイントの3つ目は小さく実践へ移すことです。学びは理解しただけでは変化になりません。会議前に論点を一つ書くなど、小さな行動へ落とすことで意味が出ます。",
        14: "小さな実践は、忙しい会社員に向いています。大きな改革を狙うと続きませんが、毎日一つだけ判断を楽にする工夫なら続けやすいです。本書の価値は行動化です。",
        15: "名言として、ピーター・ドラッカーの言葉に、測定できないものは管理できないという考え方があります。行動も同じで、何を変えるかが見えていなければ続きません。",
        16: f"ここで紹介した以外にも、本書には考え方を整えるヒントが残っています。動画では扱いきれない具体例もあるので、自分の仕事に引き寄せて読むほど発見があります。{SCENE_16_BOOK_GUIDE}",
        17: f"{SCENE_17_PREFIX}、まず問題を見える化し、次に原因や背景を捉え、最後に小さく実践する流れが大切でした。知識を仕事の判断に使える形へ整えることが本書の価値です。",
        18: "明日から実践するなら、まず一つの悩みを紙に書き出してみてください。評価、納期、人間関係のどれが問題なのかを分けるだけでも、行動は選びやすくなります。",
        19: "この考え方は、過去動画で扱った習慣化や時間管理のテーマともつながります。考えを整理してから行動するほど、毎日の改善は続きやすくなります。気になる方は、ぜひそちらもあわせてご視聴ください。",
        20: f"最後に、本は読むだけで終わらせるより、仕事の一場面に使って初めて力になります。今日の内容から一つ選び、明日の判断に活かしてみてください。{SCENE_20_CLOSING}",
    }
    return "\n".join(f"【シーン{index}】\n{_fit(bodies[index])}" for index in range(1, 21))


def test_quality_report_checks_latest_script_rules():
    titles = "A. 【角が立つ一言に注意】タイトルで直すNG表現7選【信頼を削る前に】\nB. 【会議の返しがやわらぐ】タイトルの言い換え10例【評価される伝え方へ】\nC. 【正論ほど嫌われる？】タイトルが教える否定しない話し方【まず受け止める技術】"
    description = "この本の要点を仕事と日常で使える視点に絞り、明日から実践できる行動までわかりやすく丁寧に解説します。"
    prompts = json.dumps([_build_image_prompt_item(index) for index in range(1, 21)], ensure_ascii=False)

    report = build_quality_report(_valid_script(), titles, prompts, description)

    assert "【シーン1】〜【シーン20】形式: OK" in report
    assert "各シーン180〜220字: OK" in report
    assert "シーン8チャンネル登録固定文: OK" in report
    assert "シーン17おさらい開始: OK" in report
    assert "シーン20締め固定文: OK" in report
    assert "タイトルの【】フック重複: OK" in report
    assert "タイトル前後の【】: OK" in report
    assert "タイトル弱いフックなし: OK" in report
    assert "タイトル数字検討: OK" in report
    assert "画像プロンプト必須メタ情報: OK" in report
    assert "画像プロンプト所属ブロック: OK" in report
    assert "重要ポイント画像の理解の流れ: OK" in report
    assert "【文体品質チェック】" in report
    assert "平均点：" in report
    assert "判定：" in report


def test_quality_report_detects_duplicate_title_hooks():
    report = build_quality_report(
        "【シーン1】\n短い本文",
        "A. 【同じ】タイトル\nB. 【同じ】タイトル\nC. 【別】タイトル",
        "",
        "短い説明",
    )

    assert "タイトルの【】フック重複: NG" in report


def test_quality_report_detects_weak_and_one_sided_title_hooks():
    report = build_quality_report(
        "【シーン1】\n短い本文",
        "A. 【知っておかないと損】タイトル\nB. 【会議の返しがやわらぐ】タイトルの言い換え10例【評価される伝え方へ】\nC. 【正論ほど嫌われる？】タイトルが教える否定しない話し方【まず受け止める技術】",
        "",
        "短い説明",
    )

    assert "タイトル前後の【】: NG" in report
    assert "タイトル弱いフックなし: NG" in report




def test_image_quality_report_includes_thumbnail_b_benefit_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【thumbnail_B_benefit 画像品質チェック】" in report
    assert "thumbnail_B_benefit固定役割に合っている：OK" in report
    assert "ベネフィット訴求型サムネになっている：OK" in report
    assert "benefit_trigger_label が定義されている：OK" in report
    assert "benefit_style が設定されている：OK" in report
    assert "visual_structure が設定されている：OK" in report
    assert "thumbnail_Aと役割が混ざっていない：OK" in report


def test_image_quality_report_includes_thumbnail_c_curiosity_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【thumbnail_C_curiosity 画像品質チェック】" in report
    assert "thumbnail_C_curiosity固定役割に合っている：OK" in report
    assert "逆張り・好奇心訴求型サムネになっている：OK" in report
    assert "意味のない奇抜サムネになっていない：OK" in report
    assert "curiosity_trigger_label が定義されている：OK" in report
    assert "contrarian_angle_label が定義されている：OK" in report
    assert "curiosity_style が設定されている：OK" in report
    assert "visual_structure が設定されている：OK" in report
    assert "thumbnail_Aと役割が混ざっていない：OK" in report
    assert "thumbnail_Bと役割が混ざっていない：OK" in report

def test_image_quality_report_includes_scene_06_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_06 画像品質チェック】" in report
    assert "scene_06固定役割に合っている：OK" in report
    assert "visual_structure が適切：OK" in report
    assert "generic business image になっていない：OK" in report


def test_image_quality_report_includes_scene_07_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_07 画像品質チェック】" in report
    assert "scene_07固定役割に合っている：OK" in report
    assert "evidence_type が現在の原稿に基づいている：OK" in report
    assert "source_confidence を記録している：OK" in report
    assert "架空の数字・出典なし：OK" in report


def test_image_quality_report_includes_scene_08_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_08 画像品質チェック】" in report
    assert "チャンネル登録CTAだと分かる：OK" in report
    assert "押し売り感がない：OK" in report
    assert "英語テキストなし：OK" in report
    assert "赤い派手な登録ボタンになっていない：OK" in report
    assert "scene_07と構図が違う：OK" in report

def test_image_quality_report_includes_scene_09_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_09 画像品質チェック】" in report
    assert "scene_09固定役割に合っている：OK" in report
    assert "重要ポイント②の導入だと分かる：OK" in report
    assert "point_2_label が原稿から生成されている：OK" in report
    assert "point_2_type が適切：OK" in report
    assert "scene_08と構図が違う：OK" in report
    assert "scene_05と構図が違う：OK" in report

def test_image_quality_report_includes_scene_10_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_10 画像品質チェック】" in report
    assert "scene_10固定役割に合っている：OK" in report
    assert "重要ポイント②の具体化になっている：OK" in report
    assert "visual_structure が適切：OK" in report
    assert "可変ラベルが原稿から生成されている：OK" in report
    assert "scene_09と構図が違う：OK" in report
    assert "generic flowchart image になっていない：OK" in report


def test_image_quality_report_includes_scene_11_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_11 画像品質チェック】" in report
    assert "scene_11固定役割に合っている：OK" in report
    assert "重要ポイント②の実話補強になっている：OK" in report
    assert "verification_status を記録している：OK" in report
    assert "Toyota等の固定企業名なし：OK" in report
    assert "scene_10と構図が違う：OK" in report


def test_scene_11_prompt_uses_variable_episode_safety_rules():
    from bookbase_automation.generator import _build_image_prompt_item, build_image_context

    script = _valid_script()
    context = build_image_context(script, "テスト本", [])
    item = _build_image_prompt_item(11, context)

    assert item["fixed_role"] == "重要ポイント②の実話エピソード補強"
    assert item["verification_status"] in {"verified", "needs_review", "unverified"}
    assert item["visual_mode"] in {"named_episode", "silhouette_episode", "symbolic_action"}
    assert "Do not hard-code any person" in item["final_prompt"]
    assert "avoid hard-coded Toyota" in item["final_prompt"]
    assert "Use only the following Japanese text elements exactly as written" in item["final_prompt"]
    assert "Toyota's former president" not in item["final_prompt"]


def test_image_quality_report_includes_scene_12_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_12 画像品質チェック】" in report
    assert "scene_12固定役割に合っている：OK" in report
    assert "コメントCTAだと分かる：OK" in report
    assert "experience_label が原稿から生成されている：OK" in report
    assert "キーワード型コメント促しになっていない：OK" in report
    assert "scene_08と構図が違う：OK" in report

def test_image_quality_report_includes_scene_13_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_13 画像品質チェック】" in report
    assert "scene_13固定役割に合っている：OK" in report
    assert "重要ポイント③の導入だと分かる：OK" in report
    assert "point_3_label が原稿から生成されている：OK" in report
    assert "point_3_type が適切：OK" in report
    assert "scene_09と構図が違う：OK" in report
    assert "scene_12と構図が違う：OK" in report
    assert "scene_18の実践画像と役割が混ざっていない：OK" in report


def test_scene_13_prompt_uses_variable_key_point_three_rules():
    from bookbase_automation.generator import _build_image_prompt_item, build_image_context

    script = _valid_script()
    context = build_image_context(script, "テスト本", [])
    item = _build_image_prompt_item(13, context)

    assert item["fixed_role"] == "重要ポイント③の導入"
    assert item["point_3_type"] in {"practice", "solution", "mindset", "framework", "habit", "decision_rule", "final_perspective"}
    assert len(item["exact_text_elements"]) <= 3
    assert item["exact_text_elements"][0] == "重要ポイント③"
    assert "Current Key Point 3" in item["final_prompt"]
    assert "Point 3 type" in item["final_prompt"]
    assert "Do not create a generic checklist or planner image" in item["final_prompt"]
    assert "avoid repeating the Scene 09 or Scene 12 composition" in item["final_prompt"]
    assert "hands checking off" not in item["final_prompt"]
    assert "planner" not in item["composition"]

def test_image_quality_report_includes_scene_14_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_14 画像品質チェック】" in report
    assert "scene_14固定役割に合っている：OK" in report
    assert "重要ポイント③の具体化になっている：OK" in report
    assert "visual_structure が適切：OK" in report
    assert "可変ラベルが原稿から生成されている：OK" in report
    assert "scene_13と構図が違う：OK" in report
    assert "scene_18と役割が混ざっていない：OK" in report
    assert "generic meeting image になっていない：OK" in report


def test_scene_14_prompt_uses_variable_key_point_three_concretization_rules():
    from bookbase_automation.generator import _build_image_prompt_item, build_image_context

    script = _valid_script()
    context = build_image_context(script, "テスト本", [])
    item = _build_image_prompt_item(14, context)

    assert item["fixed_role"] == "重要ポイント③の具体化"
    assert item["visual_structure"] in {"practical_example", "step_demo", "before_after", "tool_use", "scenario_demo", "framework_application"}
    assert len(item["exact_text_elements"]) <= 3
    assert "Current Key Point 3" in item["final_prompt"]
    assert "Current Scene 14 core message" in item["final_prompt"]
    assert "Visual structure" in item["final_prompt"]
    assert "Do not create a generic meeting scene unless the current script actually requires it" in item["final_prompt"]
    assert "avoid repeating the Scene 13 composition or the later Scene 18 implementation composition" in item["final_prompt"]
    assert "businessperson calmly responding" not in item["final_prompt"]
    assert "Watercolor image of a businessperson calmly responding in a meeting" not in item["final_prompt"]


def test_image_quality_report_includes_scene_15_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_15 画像品質チェック】" in report
    assert "scene_15固定役割に合っている：OK" in report
    assert "重要ポイント③の引用・一節補強になっている：OK" in report
    assert "attribution_status を記録している：OK" in report
    assert "attribution が弱い場合に人物名を出していない：OK" in report
    assert "長い引用文を入れていない：OK" in report
    assert "scene_14と構図が違う：OK" in report


def test_scene_15_prompt_uses_variable_quote_attribution_rules():
    from bookbase_automation.generator import _build_image_prompt_item, build_image_context

    script = _valid_script()
    context = build_image_context(script, "テスト本", [])
    item = _build_image_prompt_item(15, context)

    assert item["fixed_role"] == "重要ポイント③の引用・名言補強"
    assert item["quote_source_type"] in {"person", "book", "public_domain_quote", "paraphrase", "symbolic_only"}
    assert item["attribution_status"] in {"verified", "needs_review", "unverified"}
    assert item["visual_mode"] in {"named_quote", "quote_card", "still_life", "symbolic_quote_scene"}
    assert len(item["exact_text_elements"]) <= 3
    assert "Current Key Point 3" in item["final_prompt"]
    assert "Current Scene 15 core message" in item["final_prompt"]
    assert "Attribution status" in item["final_prompt"]
    assert "Do not hard-code any quote from a previous book" in item["final_prompt"]
    assert "Use only the following Japanese text elements exactly as written" in item["final_prompt"]
    assert "avoid repeating the Scene 14 composition" in item["final_prompt"]
    assert "Acceptance is the source of change" not in item["final_prompt"]


def test_image_quality_report_includes_scene_17_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_17 画像品質チェック】" in report
    assert "scene_17固定役割に合っている：OK" in report
    assert "3ポイントが順番のある流れとして見える：OK" in report
    assert "point_1_label / point_2_label / point_3_label が原稿から生成されている：OK" in report
    assert "generic three-card image になっていない：OK" in report


def test_image_quality_report_includes_scene_18_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_18 画像品質チェック】" in report
    assert "scene_18固定役割に合っている：OK" in report
    assert "practice_theme_label が定義されている：OK" in report
    assert "practice_type が設定されている：OK" in report
    assert "visual_structure が設定されている：OK" in report
    assert "scene_17の総まとめ画像と役割が混ざっていない：OK" in report
    assert "generic office image になっていない：OK" in report


def test_image_quality_report_includes_scene_20_checks():
    from bookbase_automation.image_generation import build_image_quality_report

    report = build_image_quality_report([])

    assert "## 【scene_20 画像品質チェック】" in report
    assert "scene_20固定役割に合っている：OK" in report
    assert "final_message_label が定義されている：OK" in report
    assert "closing_emotion が設定されている：OK" in report
    assert "closing_type が設定されている：OK" in report
    assert "visual_structure が設定されている：OK" in report
    assert "scene_18の実践画像と役割が混ざっていない：OK" in report
    assert "scene_19の関連動画接続画像と役割が混ざっていない：OK" in report
    assert "CTA・広告バナー風になっていない：OK" in report

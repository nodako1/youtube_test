# 品質チェック結果

【原稿形式チェック】

シーン数：20 / 20
見出し形式：OK
シーン間空行：OK
本文1段落：OK
全体文字数：3847字 / 3600〜4400字

【シーン別文字数】

シーン1：184字 OK
シーン2：181字 OK
シーン3：200字 OK
シーン4：188字 OK
シーン5：182字 OK
シーン6：197字 OK
シーン7：180字 OK
シーン8：190字 OK
シーン9：198字 OK
シーン10：184字 OK
シーン11：195字 OK
シーン12：182字 OK
シーン13：188字 OK
シーン14：184字 OK
シーン15：187字 OK
シーン16：218字 OK
シーン17：190字 OK
シーン18：214字 OK
シーン19：211字 OK
シーン20：194字 OK

【文体品質チェック】

読みたくなる言い回し：5/5
一文の長さの変化：5/5
句読点の自然さ：5/5
接続詞の自然さ：3/5
語尾の変化：4/5
会社員目線：4/5
AIっぽさの少なさ：5/5
本の内容との一致：4/5
シーン間の流れ：5/5
平均点：4.4/5
判定：OK

【画像プロンプト恒久ルールチェック】

scene_01：固定役割と可変内容を分離：NG
scene_02：固定役割と可変内容を分離：NG
scene_03：固定役割と可変内容を分離：NG
scene_04：固定役割と可変内容を分離：NG
scene_05：固定役割と可変内容を分離：NG
今回テーマ固有語句のハードコードなし：NG
exact_text_elementsを原稿から生成：OK
隣接シーンとの差別化：OK
検出語句：否定しない言い換え, 否定しない言い換え事典

【scene_19 画像品質チェック】

scene_19固定役割に合っている：NG
現在の本と関連過去動画の本をつなぐ画像になっている：NG
単なる広告・CTA画像になっていない：NG
2冊の本の関係性が connection_reason として定義されている：NG
connection_type が設定されている：NG
visual_structure が設定されている：NG
参照画像が現在の本として扱われている：NG
過去動画側の本が省略されていない：NG
画像内テキストが1要素以内：OK
英語テキストなし：NG
指定外テキストなし：NG
文字量が多すぎない：OK
scene_20の締め画像と役割が混ざっていない：NG
広告バナー風になっていない：NG

## 詳細チェック

- 【シーン1】〜【シーン20】形式: OK（検出シーン: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]）
- シーン本文1段落: OK（シーン内改行なし）
- シーン間空行: OK（各シーンの間に空行1行）
- シーン本文箇条書きなし: OK（Markdown箇条書き・番号リストなし）
- 各シーン180〜220字: OK（全シーン範囲内）
- 全体3600〜4400字: OK（現在の文字数目安: 3847）
- 50〜60文字説明: NG（現在の説明文字数: 80）
- シーン1統計クイズ: OK（ABC選択肢、調査、締め文を確認してください）
- シーン1禁止表現なし: OK（禁止表現を確認してください）
- シーン2正解発表とテーマ接続: OK（正解発表からテーマへ接続してください）
- シーン3本紹介固定文: OK（固定文を確認してください）
- シーン4著者紹介と3ポイント: OK（著者紹介と3つの重要ポイントを確認してください）
- シーン5冒頭固定: OK（必須開始文: 重要ポイントの1つ目は）
- シーン7研究・データ補強: OK（研究・データ補強を入れてください）
- シーン8チャンネル登録固定文: OK（固定CTAを変えずに入れてください）
- シーン9冒頭固定: OK（必須開始文: 重要ポイントの2つ目は）
- シーン11実話エピソード: NG（確認済み実話を入れてください）
- シーン12コメント促進形式: OK（固定フォーマットを確認してください）
- シーン13冒頭固定: OK（必須開始文: 重要ポイントの3つ目は）
- シーン15名言補強: OK（確認済み名言を入れてください）
- シーン16本書案内固定文: OK（本書案内固定文と概要欄誘導なしを確認してください）
- シーン17おさらい開始: OK（必須開始文: 今回の内容をおさらいすると）
- シーン18実践: OK（仕事や日常への実践に落とし込んでください）
- シーン19関連動画接続: OK（関連動画への自然な接続を入れてください）
- シーン20締め固定文: OK（固定締め文を変えずに入れてください）
- タイトル案A/B/C: OK（3案あるか確認してください）
- タイトル前後の【】: OK（【冒頭フック】メインタイトル【後方フック】形式を確認してください）
- タイトルの【】フック重複: OK（重複なし）
- タイトル弱いフックなし: NG（禁止された弱いフック語を単独使用していないか確認してください）
- タイトル数字検討: OK（数字化できる要素がある場合は数字を入れてください）
- 画像プロンプト20件: OK（検出件数: 20）
- 画像プロンプト必須メタ情報: NG（item1: 前ブロックからの理解の流れ, 入力画像チェック; item2: 入力画像チェック; item5: 使用画像, 入力画像チェック）
- 画像プロンプト所属ブロック: NG（シーン1: 所属ブロック不一致; シーン2: 所属ブロック不一致; シーン3: 所属ブロック不一致; シーン4: 所属ブロック不一致; シーン5: 所属ブロック不一致）
- 重要ポイント画像の理解の流れ: NG（重要ポイント1=土台、2=構造、3=実践の流れを確認してください）

## 修正推奨
- NGの項目が1つでもある場合は、提出前に再生成または手修正してください。
- 事実確認が必要な統計、研究、実話、名言は、Koichiさんの確認対象として扱ってください。
- 自動生成結果は最終稿ではなく、品質担保のための確認前提の下書きです。

## 投稿補助情報チェック

- タイトルA：OK
- タイトルB：OK
- タイトルC：OK
- タイトル前後の【】：OK
- タイトル弱いフックなし：NG
- タイトルフック重複なし：OK
- タイトル数字検討：OK
- 過去タイトル重複：OK
- 過去フック重複：OK
- タイトルの誇張：OK
- タイムスケジュール5項目：OK
- タイムスケジュール時間固定：OK
- 内部シーン表記なし：OK
- 50文字説明 50〜60文字：NG
- 50文字説明 文字数併記：NG
- コメント3行構成：OK
- コメント3行目固定文：OK
- コメント内容と動画テーマの一致：OK

【metadata出力整形チェック】

タイムスケジュール5行出力：OK
タイムスケジュール1行連結なし：OK
コメント3行出力：OK
コメント1行連結なし：OK
コメント3行目固定文：OK

## 【入力ファイル判定】

- 実行日：2026-06-20
- 今日の日付キー：20260620
- 今回の原稿材料：OK
- 今回のブックカバー：OK
- 今回の著者画像：OK
- scene_19用原稿材料：OK
- scene_19用ブックカバー：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_20
生成完了：なし
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：FAILED

- scene_01：NEEDS_REVIEW
- scene_02：NEEDS_REVIEW
- scene_03：NEEDS_REVIEW
- scene_04：NEEDS_REVIEW
- scene_05：NEEDS_REVIEW
- scene_06：NEEDS_REVIEW
- scene_07：NEEDS_REVIEW
- scene_08：NEEDS_REVIEW
- scene_09：NEEDS_REVIEW
- scene_10：NEEDS_REVIEW
- scene_11：NEEDS_REVIEW
- scene_12：NEEDS_REVIEW
- scene_13：NEEDS_REVIEW
- scene_14：NEEDS_REVIEW
- scene_15：NEEDS_REVIEW
- scene_16：NEEDS_REVIEW
- scene_17：NEEDS_REVIEW
- scene_18：NEEDS_REVIEW
- scene_19：NEEDS_REVIEW
- scene_20：NEEDS_REVIEW
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【自動取得情報チェック】

- scene_11_story_person：NEEDS_REVIEW
- scene_11_story_person_source：NEEDS_REVIEW
- scene_15_quote_person：NEEDS_REVIEW
- scene_15_quote_source：NEEDS_REVIEW
- scene_11：人物画像未取得の場合は、シルエットまたは象徴表現で代替。
- scene_15：名言人物画像未取得の場合は、名言カードまたは静物構図で代替。

## 【OpenAI API通信チェック】

対象：ai_assets
API呼び出し：OK
エラー種別：APITimeoutError
retry回数：5
最終結果：recovered
メッセージ：Request timed out.

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：scene_01
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：OK

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：scene_02
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：OK

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：scene_03
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：OK

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：OK
実ブックカバーを使用：OK
AIが表紙を再生成していない：OK
ブックカバーの文字が読める：OK
ブックカバーが歪んでいない：OK
表紙の上に文字を重ねていない：OK
今回の本紹介として機能している：OK
動画全体の結論が短く伝わる：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_02と構図が違う：OK

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：scene_04
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：OK

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OK
scene_04_author_reference：OK
scene_04_visual：stylized_watercolor_author_illustration
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：scene_05
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：OK

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：scene_06
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：OK

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：scene_07
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：OK

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：scene_08
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：OK

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：scene_09
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：OK

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：scene_10
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：OK

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：scene_11
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：OK

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：scene_12
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：OK

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：scene_13
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：OK

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：scene_14
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：OK

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：scene_15
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：OK

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：scene_16
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：OK

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：scene_17
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：OK

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：scene_18
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：OK

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：scene_19
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：OK

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：scene_20
失敗：なし
スキップ：なし
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：OK

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

scene_06固定役割に合っている：OK
現在の原稿内容に沿っている：OK
重要ポイント①の理由・背景・仕組みが見える：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
visual_structure が適切：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

scene_10固定役割に合っている：OK
重要ポイント②の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
generic flowchart image になっていない：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

scene_14固定役割に合っている：OK
重要ポイント③の具体化になっている：OK
現在の原稿内容に沿っている：OK
visual_structure が適切：OK
可変ラベルが原稿から生成されている：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
generic meeting image になっていない：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：なし
失敗：なし
スキップ：scene_06
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：SKIPPED

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
現在の原稿内容に沿っている：NG
直前の重要ポイントを深掘りしている：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：なし
失敗：なし
スキップ：scene_07
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：SKIPPED

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：NG
重要ポイント①の根拠補強になっている：NG
evidence_type が現在の原稿に基づいている：NG
source_confidence を記録している：NG
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：なし
失敗：なし
スキップ：scene_08
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：SKIPPED

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：NG
押し売り感がない：NG
Book Baseらしい学びの雰囲気がある：NG
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：なし
失敗：なし
スキップ：scene_09
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：SKIPPED

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：NG
重要ポイント②の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_2_label が原稿から生成されている：NG
point_2_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：なし
失敗：なし
スキップ：scene_10
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：SKIPPED

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：なし
失敗：なし
スキップ：scene_11
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：SKIPPED

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：NG
重要ポイント②の実話補強になっている：NG
エピソードが現在の原稿に基づいている：NG
verification_status を記録している：NG
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：なし
失敗：なし
スキップ：scene_12
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：SKIPPED

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：NG
本の学び・要点整理が主役：NG
コメントCTAが補助的に小さい：NG
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：NG
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：なし
失敗：なし
スキップ：scene_13
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：SKIPPED

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：NG
重要ポイント③の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_3_label が原稿から生成されている：NG
point_3_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：なし
失敗：なし
スキップ：scene_14
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：SKIPPED

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：なし
失敗：なし
スキップ：scene_15
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：SKIPPED

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：NG
重要ポイント③の引用・一節補強になっている：NG
引用または要約が現在の原稿に基づいている：NG
attribution_status を記録している：NG
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：なし
失敗：なし
スキップ：scene_16
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：SKIPPED

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：NG
本書の残りの価値案内になっている：NG
自然な読書案内になっている：NG
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：なし
失敗：なし
スキップ：scene_17
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：SKIPPED

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：NG
3つの重要ポイントの振り返りになっている：NG
3ポイントが順番のある流れとして見える：NG
point_1_label / point_2_label / point_3_label が原稿から生成されている：NG
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：なし
失敗：なし
スキップ：scene_18
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：SKIPPED

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：NG
本の学びを仕事や日常に落とし込む画像になっている：NG
単なるデスクワーク画像になっていない：NG
practice_theme_label が定義されている：NG
practice_action_label が定義されている：NG
practice_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：なし
失敗：なし
スキップ：scene_19
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：SKIPPED

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：なし
失敗：なし
スキップ：scene_20
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：SKIPPED

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：NG
動画全体を温かく締める画像になっている：NG
読後感・余韻・感謝が伝わる：NG
final_message_label が定義されている：NG
closing_emotion が設定されている：NG
closing_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：なし
失敗：なし
スキップ：scene_06
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：SKIPPED

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
現在の原稿内容に沿っている：NG
直前の重要ポイントを深掘りしている：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：なし
失敗：なし
スキップ：scene_07
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：SKIPPED

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：NG
重要ポイント①の根拠補強になっている：NG
evidence_type が現在の原稿に基づいている：NG
source_confidence を記録している：NG
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：なし
失敗：なし
スキップ：scene_08
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：SKIPPED

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：NG
押し売り感がない：NG
Book Baseらしい学びの雰囲気がある：NG
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：なし
失敗：なし
スキップ：scene_09
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：SKIPPED

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：NG
重要ポイント②の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_2_label が原稿から生成されている：NG
point_2_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：なし
失敗：なし
スキップ：scene_10
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：SKIPPED

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：なし
失敗：なし
スキップ：scene_11
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：SKIPPED

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：NG
重要ポイント②の実話補強になっている：NG
エピソードが現在の原稿に基づいている：NG
verification_status を記録している：NG
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：なし
失敗：なし
スキップ：scene_12
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：SKIPPED

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：NG
本の学び・要点整理が主役：NG
コメントCTAが補助的に小さい：NG
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：NG
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：なし
失敗：なし
スキップ：scene_13
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：SKIPPED

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：NG
重要ポイント③の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_3_label が原稿から生成されている：NG
point_3_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：なし
失敗：なし
スキップ：scene_14
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：SKIPPED

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：なし
失敗：なし
スキップ：scene_15
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：SKIPPED

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：NG
重要ポイント③の引用・一節補強になっている：NG
引用または要約が現在の原稿に基づいている：NG
attribution_status を記録している：NG
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：なし
失敗：なし
スキップ：scene_16
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：SKIPPED

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：NG
本書の残りの価値案内になっている：NG
自然な読書案内になっている：NG
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：なし
失敗：なし
スキップ：scene_17
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：SKIPPED

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：NG
3つの重要ポイントの振り返りになっている：NG
3ポイントが順番のある流れとして見える：NG
point_1_label / point_2_label / point_3_label が原稿から生成されている：NG
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：なし
失敗：なし
スキップ：scene_18
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：SKIPPED

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：NG
本の学びを仕事や日常に落とし込む画像になっている：NG
単なるデスクワーク画像になっていない：NG
practice_theme_label が定義されている：NG
practice_action_label が定義されている：NG
practice_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：なし
失敗：なし
スキップ：scene_19
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：SKIPPED

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：なし
失敗：なし
スキップ：scene_20
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：SKIPPED

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：NG
動画全体を温かく締める画像になっている：NG
読後感・余韻・感謝が伝わる：NG
final_message_label が定義されている：NG
closing_emotion が設定されている：NG
closing_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：なし
失敗：なし
スキップ：scene_06
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：SKIPPED

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
現在の原稿内容に沿っている：NG
直前の重要ポイントを深掘りしている：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：なし
失敗：なし
スキップ：scene_07
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：SKIPPED

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：NG
重要ポイント①の根拠補強になっている：NG
evidence_type が現在の原稿に基づいている：NG
source_confidence を記録している：NG
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：なし
失敗：なし
スキップ：scene_08
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：SKIPPED

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：NG
押し売り感がない：NG
Book Baseらしい学びの雰囲気がある：NG
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：なし
失敗：なし
スキップ：scene_09
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：SKIPPED

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：NG
重要ポイント②の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_2_label が原稿から生成されている：NG
point_2_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：なし
失敗：なし
スキップ：scene_10
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：SKIPPED

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：なし
失敗：なし
スキップ：scene_11
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：SKIPPED

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：NG
重要ポイント②の実話補強になっている：NG
エピソードが現在の原稿に基づいている：NG
verification_status を記録している：NG
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：なし
失敗：なし
スキップ：scene_12
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：SKIPPED

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：NG
本の学び・要点整理が主役：NG
コメントCTAが補助的に小さい：NG
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：NG
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：なし
失敗：なし
スキップ：scene_13
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：SKIPPED

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：NG
重要ポイント③の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_3_label が原稿から生成されている：NG
point_3_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：なし
失敗：なし
スキップ：scene_14
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：SKIPPED

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：なし
失敗：なし
スキップ：scene_15
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：SKIPPED

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：NG
重要ポイント③の引用・一節補強になっている：NG
引用または要約が現在の原稿に基づいている：NG
attribution_status を記録している：NG
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：なし
失敗：なし
スキップ：scene_16
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：SKIPPED

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：NG
本書の残りの価値案内になっている：NG
自然な読書案内になっている：NG
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：なし
失敗：なし
スキップ：scene_17
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：SKIPPED

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：NG
3つの重要ポイントの振り返りになっている：NG
3ポイントが順番のある流れとして見える：NG
point_1_label / point_2_label / point_3_label が原稿から生成されている：NG
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：なし
失敗：なし
スキップ：scene_18
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：SKIPPED

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：NG
本の学びを仕事や日常に落とし込む画像になっている：NG
単なるデスクワーク画像になっていない：NG
practice_theme_label が定義されている：NG
practice_action_label が定義されている：NG
practice_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：なし
失敗：なし
スキップ：scene_19
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：SKIPPED

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：なし
失敗：なし
スキップ：scene_20
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：SKIPPED

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：NG
動画全体を温かく締める画像になっている：NG
読後感・余韻・感謝が伝わる：NG
final_message_label が定義されている：NG
closing_emotion が設定されている：NG
closing_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：なし
失敗：なし
スキップ：scene_06
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：SKIPPED

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
現在の原稿内容に沿っている：NG
直前の重要ポイントを深掘りしている：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：なし
失敗：なし
スキップ：scene_07
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：SKIPPED

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：NG
重要ポイント①の根拠補強になっている：NG
evidence_type が現在の原稿に基づいている：NG
source_confidence を記録している：NG
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：なし
失敗：なし
スキップ：scene_08
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：SKIPPED

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：NG
押し売り感がない：NG
Book Baseらしい学びの雰囲気がある：NG
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：なし
失敗：なし
スキップ：scene_09
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：SKIPPED

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：NG
重要ポイント②の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_2_label が原稿から生成されている：NG
point_2_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：なし
失敗：なし
スキップ：scene_10
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：SKIPPED

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：なし
失敗：なし
スキップ：scene_11
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：SKIPPED

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：NG
重要ポイント②の実話補強になっている：NG
エピソードが現在の原稿に基づいている：NG
verification_status を記録している：NG
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：なし
失敗：なし
スキップ：scene_12
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：SKIPPED

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：NG
本の学び・要点整理が主役：NG
コメントCTAが補助的に小さい：NG
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：NG
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：なし
失敗：なし
スキップ：scene_13
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：SKIPPED

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：NG
重要ポイント③の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_3_label が原稿から生成されている：NG
point_3_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：なし
失敗：なし
スキップ：scene_14
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：SKIPPED

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：なし
失敗：なし
スキップ：scene_15
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：SKIPPED

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：NG
重要ポイント③の引用・一節補強になっている：NG
引用または要約が現在の原稿に基づいている：NG
attribution_status を記録している：NG
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：なし
失敗：なし
スキップ：scene_16
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：SKIPPED

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：NG
本書の残りの価値案内になっている：NG
自然な読書案内になっている：NG
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：なし
失敗：なし
スキップ：scene_17
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：SKIPPED

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：NG
3つの重要ポイントの振り返りになっている：NG
3ポイントが順番のある流れとして見える：NG
point_1_label / point_2_label / point_3_label が原稿から生成されている：NG
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：なし
失敗：なし
スキップ：scene_18
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：SKIPPED

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：NG
本の学びを仕事や日常に落とし込む画像になっている：NG
単なるデスクワーク画像になっていない：NG
practice_theme_label が定義されている：NG
practice_action_label が定義されている：NG
practice_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：なし
失敗：なし
スキップ：scene_19
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：SKIPPED

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：なし
失敗：なし
スキップ：scene_20
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：SKIPPED

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：NG
動画全体を温かく締める画像になっている：NG
読後感・余韻・感謝が伝わる：NG
final_message_label が定義されている：NG
closing_emotion が設定されている：NG
closing_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_06〜scene_06
生成完了：なし
失敗：なし
スキップ：scene_06
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_06：SKIPPED

scene番号：scene_06
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_06.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
現在の原稿内容に沿っている：NG
直前の重要ポイントを深掘りしている：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_07〜scene_07
生成完了：なし
失敗：なし
スキップ：scene_07
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_07：SKIPPED

scene番号：scene_07
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_07.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：NG
重要ポイント①の根拠補強になっている：NG
evidence_type が現在の原稿に基づいている：NG
source_confidence を記録している：NG
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_08〜scene_08
生成完了：なし
失敗：なし
スキップ：scene_08
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_08：SKIPPED

scene番号：scene_08
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_08.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：NG
押し売り感がない：NG
Book Baseらしい学びの雰囲気がある：NG
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_09〜scene_09
生成完了：なし
失敗：なし
スキップ：scene_09
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_09：SKIPPED

scene番号：scene_09
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_09.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：NG
重要ポイント②の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_2_label が原稿から生成されている：NG
point_2_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_10〜scene_10
生成完了：なし
失敗：なし
スキップ：scene_10
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_10：SKIPPED

scene番号：scene_10
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_10.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_11〜scene_11
生成完了：なし
失敗：なし
スキップ：scene_11
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_11：SKIPPED

scene番号：scene_11
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_11.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：NG
重要ポイント②の実話補強になっている：NG
エピソードが現在の原稿に基づいている：NG
verification_status を記録している：NG
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_12〜scene_12
生成完了：なし
失敗：なし
スキップ：scene_12
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_12：SKIPPED

scene番号：scene_12
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_12.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：NG
本の学び・要点整理が主役：NG
コメントCTAが補助的に小さい：NG
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：NG
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_13〜scene_13
生成完了：なし
失敗：なし
スキップ：scene_13
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_13：SKIPPED

scene番号：scene_13
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_13.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：NG
重要ポイント③の導入だと分かる：NG
現在の原稿内容に沿っている：NG
point_3_label が原稿から生成されている：NG
point_3_type が適切：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_14〜scene_14
生成完了：なし
失敗：なし
スキップ：scene_14
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_14：SKIPPED

scene番号：scene_14
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_14.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：NG
直前の重要ポイントを深掘りしている：NG
現在の原稿内容に沿っている：NG
Before/After・フロー・対比・分解図・メタファーのいずれかがある：NG
原稿内容を図解・人物・短文に変換している：NG
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_15〜scene_15
生成完了：なし
失敗：なし
スキップ：scene_15
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_15：SKIPPED

scene番号：scene_15
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_15.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：NG
重要ポイント③の引用・一節補強になっている：NG
引用または要約が現在の原稿に基づいている：NG
attribution_status を記録している：NG
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_16〜scene_16
生成完了：なし
失敗：なし
スキップ：scene_16
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_16：SKIPPED

scene番号：scene_16
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_16.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：NG
本書の残りの価値案内になっている：NG
自然な読書案内になっている：NG
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_17〜scene_17
生成完了：なし
失敗：なし
スキップ：scene_17
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_17：SKIPPED

scene番号：scene_17
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_17.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：NG
3つの重要ポイントの振り返りになっている：NG
3ポイントが順番のある流れとして見える：NG
point_1_label / point_2_label / point_3_label が原稿から生成されている：NG
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_18〜scene_18
生成完了：なし
失敗：なし
スキップ：scene_18
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_18：SKIPPED

scene番号：scene_18
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_18.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：NG
本の学びを仕事や日常に落とし込む画像になっている：NG
単なるデスクワーク画像になっていない：NG
practice_theme_label が定義されている：NG
practice_action_label が定義されている：NG
practice_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_19〜scene_19
生成完了：なし
失敗：なし
スキップ：scene_19
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_19：SKIPPED

scene番号：scene_19
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_19.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_20〜scene_20
生成完了：なし
失敗：なし
スキップ：scene_20
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_20：SKIPPED

scene番号：scene_20
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_20.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：NG
動画全体を温かく締める画像になっている：NG
読後感・余韻・感謝が伝わる：NG
final_message_label が定義されている：NG
closing_emotion が設定されている：NG
closing_type が設定されている：NG
visual_structure が設定されている：NG
supporting_objects が適切：NG
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_01〜scene_01
生成完了：なし
失敗：なし
スキップ：scene_01
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_01：SKIPPED

scene番号：scene_01
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_01.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_02〜scene_02
生成完了：なし
失敗：なし
スキップ：scene_02
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_02：SKIPPED

scene番号：scene_02
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_02.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_03〜scene_03
生成完了：なし
失敗：なし
スキップ：scene_03
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_03：SKIPPED

scene番号：scene_03
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_03.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_04〜scene_04
生成完了：なし
失敗：なし
スキップ：scene_04
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_04：SKIPPED

scene番号：scene_04
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_04.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：OK
否定を避ける心理効果が伝わる：OK
一目でメッセージが分かる：OK
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：MISSING
scene_04_author_reference：MISSING
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：NG
3つの重要ポイントが見える：NG
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

## 【画像生成チェック】

## 【実行完了状況】

原稿生成：OK
画像プロンプト生成：OK
画像生成対象：scene_05〜scene_05
生成完了：なし
失敗：なし
スキップ：scene_05
次回再開推奨：なし
retry回数：0
最終ステータス：COMPLETED

- scene_05：SKIPPED

scene番号：scene_05
API生成：OK
出力パス：/home/runner/work/bookbase-automation/bookbase-automation/output/2026-06-20_否定しない言い換え事典/images/scene_05.png
画像存在確認：OK
画像サイズ：1536 x 864
16:9確認：OK
使用モデル：gpt-image-2
使用サイズ：1536x864
使用品質：high
Book Base共通ルール適用：OK
scene専用ルール適用：OK
画像内テキスト制約：OK
エラー内容：なし
- thumbnail_A_loss_aversion：NEEDS_REVIEW
- thumbnail_B_benefit：NEEDS_REVIEW
- thumbnail_C_curiosity：NEEDS_REVIEW

## 【thumbnail_A_loss_aversion 画像品質チェック】

thumbnail_A_loss_aversion固定役割に合っている：OK
損失回避型サムネになっている：OK
安っぽい煽りサムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「その努力、遠回りです」が主役として大きく見える：OK
comment_text が1要素のみ：OK
loss_trigger_label が定義されている：OK
tension_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK

## 【thumbnail_B_benefit 画像品質チェック】

thumbnail_B_benefit固定役割に合っている：OK
ベネフィット訴求型サムネになっている：OK
安っぽい自己啓発サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「仕事が軽くなる思考法」が主役として大きく見える：OK
comment_text が1要素のみ：OK
benefit_trigger_label が定義されている：OK
benefit_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK

## 【thumbnail_C_curiosity 画像品質チェック】

thumbnail_C_curiosity固定役割に合っている：OK
逆張り・好奇心訴求型サムネになっている：OK
意味のない奇抜サムネになっていない：OK
参照画像が現在の本の表紙として主役化されている：OK
コメント「考える前に整える」が主役として大きく見える：OK
comment_text が1要素のみ：OK
curiosity_trigger_label が定義されている：OK
contrarian_angle_label が定義されている：OK
curiosity_style が設定されている：OK
visual_structure が設定されている：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
Book Baseロゴが小さく自然：OK
クリック性と上品さが両立している：OK
thumbnail_Aと役割が混ざっていない：OK
thumbnail_Bと役割が混ざっていない：OK

## 【scene_02 画像品質チェック】

scene_role反映：OK
正解Bが一目で分かる：OK
テーマへの橋渡しがある：OK
指定外テキストなし：OK
文字量が少ない：OK
Book Baseらしい高級感：OK
scene_01と構図が違う：OK
サムネイルっぽくなりすぎていない：OK

## 【scene_05 画像品質チェック】

重要ポイント①だと分かる：NG
否定を避ける心理効果が伝わる：NG
一目でメッセージが分かる：NG
文字量が少ない：OK
指定外テキストなし：OK
Book Baseらしい高級感：OK
scene_04と構図が違う：OK
ただの雰囲気画像になっていない：OK

## 【scene_06 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
現在の原稿内容に沿っている：OK
直前の重要ポイントを深掘りしている：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
scene_05と構図が違う：OK
見出しだけで終わっていない：OK

## 【scene_07 画像品質チェック】

scene_07固定役割に合っている：OK
重要ポイント①の根拠補強になっている：OK
evidence_type が現在の原稿に基づいている：OK
source_confidence を記録している：OK
過去テーマのハードコードなし：OK
架空の数字・出典なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_06と構図が違う：OK
generic report image になっていない：OK

## 【scene_08 画像品質チェック】

チャンネル登録CTAだと分かる：OK
押し売り感がない：OK
Book Baseらしい学びの雰囲気がある：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
赤い派手な登録ボタンになっていない：OK
scene_07と構図が違う：OK
Book Baseロゴが自然に入っている：OK

## 【scene_16 画像品質チェック】

scene_16固定役割に合っている：OK
本書の残りの価値案内になっている：OK
自然な読書案内になっている：OK
購入誘導が強すぎない：OK
概要欄リンク誘導なし：OK
販売サイト名なし：OK
架空のブックカバーなし：OK
実カバー使用時はAI再生成なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_03と構図が違う：OK

## 【scene_17 画像品質チェック】

scene_17固定役割に合っている：OK
3つの重要ポイントの振り返りになっている：OK
3ポイントが順番のある流れとして見える：OK
point_1_label / point_2_label / point_3_label が原稿から生成されている：OK
summary_heading が適切：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_04と構図が違う：OK
scene_20の締め画像と役割が混ざっていない：OK
generic three-card image になっていない：OK

## 【scene_09 画像品質チェック】

scene_09固定役割に合っている：OK
重要ポイント②の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_2_label が原稿から生成されている：OK
point_2_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
scene_05と構図が違う：OK
generic business image になっていない：OK

## 【scene_10 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
下部にまとめ帯がある：OK

## 【scene_11 画像品質チェック】

scene_11固定役割に合っている：OK
重要ポイント②の実話補強になっている：OK
エピソードが現在の原稿に基づいている：OK
verification_status を記録している：OK
検証が弱い場合に人物名を出していない：OK
検証が弱い場合に顔を描いていない：OK
過去テーマのハードコードなし：OK
Toyota等の固定企業名なし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_10と構図が違う：OK

## 【scene_12 画像品質チェック】

scene_12固定役割に合っている：OK
本の学び・要点整理が主役：OK
コメントCTAが補助的に小さい：OK
コメントCTAが短い1要素まで：OK
現在のテーマに合う経験質問になっている：OK
キーワード型コメント促しになっていない：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_08と構図が違う：OK
押しつけがましくない：OK

## 【scene_13 画像品質チェック】

scene_13固定役割に合っている：OK
重要ポイント③の導入だと分かる：OK
現在の原稿内容に沿っている：OK
point_3_label が原稿から生成されている：OK
point_3_type が適切：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_09と構図が違う：OK
scene_12と構図が違う：OK
scene_18の実践画像と役割が混ざっていない：OK

## 【scene_14 画像品質チェック】

深掘りシーンの固定役割に合っている：OK
直前の重要ポイントを深掘りしている：OK
現在の原稿内容に沿っている：OK
Before/After・フロー・対比・分解図・メタファーのいずれかがある：OK
原稿内容を図解・人物・短文に変換している：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_13と構図が違う：OK
scene_18と役割が混ざっていない：OK
下部にまとめ帯がある：OK

## 【scene_15 画像品質チェック】

scene_15固定役割に合っている：OK
重要ポイント③の引用・一節補強になっている：OK
引用または要約が現在の原稿に基づいている：OK
attribution_status を記録している：OK
attribution が弱い場合に人物名を出していない：OK
attribution が弱い場合に顔を描いていない：OK
長い引用文を入れていない：OK
過去テーマのハードコードなし：OK
指定外テキストなし：OK
文字量が少ない：OK
scene_14と構図が違う：OK

## 【scene_18 画像品質チェック】

scene_18固定役割に合っている：OK
本の学びを仕事や日常に落とし込む画像になっている：OK
単なるデスクワーク画像になっていない：OK
practice_theme_label が定義されている：OK
practice_action_label が定義されている：OK
practice_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_17の総まとめ画像と役割が混ざっていない：OK
scene_20の締め画像と役割が混ざっていない：OK
generic office image になっていない：OK

## 【scene_20 画像品質チェック】

scene_20固定役割に合っている：OK
動画全体を温かく締める画像になっている：OK
読後感・余韻・感謝が伝わる：OK
final_message_label が定義されている：OK
closing_emotion が設定されている：OK
closing_type が設定されている：OK
visual_structure が設定されている：OK
supporting_objects が適切：OK
画像内テキストが1要素以内：OK
英語テキストなし：OK
指定外テキストなし：OK
文字量が多すぎない：OK
scene_18の実践画像と役割が混ざっていない：OK
scene_19の関連動画接続画像と役割が混ざっていない：OK
CTA・広告バナー風になっていない：OK

## 【scene_03 画像品質チェック】

ブックカバー参照画像あり：NG
実ブックカバーを使用：NG
AIが表紙を再生成していない：NG
ブックカバーの文字が読める：NG
ブックカバーが歪んでいない：NG
表紙の上に文字を重ねていない：NG
今回の本紹介として機能している：NG
動画全体の結論が短く伝わる：NG
文字量が少ない：NG
Book Baseらしい高級感：NG
scene_02と構図が違う：NG

## 【scene_04 画像品質チェック】

著者参考画像あり：OPTIONAL
scene_04_author_reference：OPTIONAL
scene_04_visual：silhouette_or_symbolic
著者紹介として機能している：OK
3つの重要ポイントが見える：OK
文字量が少ない：OK
指定外テキストなし：OK
著者写真をそのまま貼っていない：OK
水彩画風の高級感：OK
scene_03と構図が違う：OK
硬いフローチャートになっていない：OK

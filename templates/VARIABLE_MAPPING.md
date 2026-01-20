# VARIABLE_MAPPING.md
BiBi 症例生成：入力（contents/cases/*.md）→ テンプレ（templates/*）差し込み変数 対応表
最初のGold症例：3410 を基準に固定する。

---

## 0. ルール
- 変数表記は {{ var }} を基本とする（テンプレ側で統一）。
- 文字列の結合は生成側で行い、テンプレは「表示」だけに寄せる。
- URLスラッグは推測せず、入力で確定して渡す。
- 「ピラー」という語はユーザー向け出力で使用禁止。必ず「総合ページ」にする。
- 価格表示がある場合は免責文を必ず出す：
  「＊本ページ記載のモニター制度・料金は投稿時点の内容です。今後、内容が変更・終了となる場合があります。」

---

## 1. 入力ファイルの想定
- 入力：contents/cases/3410.md（INPUT_SCHEMA.mdに準拠）
- 主要キー：case_id, age_decade, sex, seo_title, keywords, meta_description, category_url, final_slug,
  images, main_problems, treatment, price, risks, patient_voice, doctor_comment_seed, related_links

---

## 2. 共通：基本項目（全テンプレ共通で使う）
- {{ case_id }}                 ← case_id
- {{ age_decade }}              ← age_decade
- {{ sex }}                     ← sex
- {{ seo_title }}               ← seo_title
- {{ meta_description }}        ← meta_description
- {{ category_url }}            ← category_url
- {{ final_slug }}              ← final_slug

- {{ keywords_joined }}         ← keywords を「、」で結合（例： "A、B、C"）

- {{ main_problems_joined }}    ← main_problems を「、」で結合（例： "目の下のクマ、ほうれい線、..."）

- {{ risks_joined }}            ← risks を「、」で結合
- {{ risks_short }}             ← risks のうち主要3〜5個を短縮（IG用）

---

## 3. 画像（WP/IG共通）
### hero（冒頭2枚）
- {{ images.hero.0.url }}       ← images.hero[0].url
- {{ images.hero.0.alt }}       ← images.hero[0].alt
- {{ images.hero.1.url }}       ← images.hero[1].url
- {{ images.hero.1.alt }}       ← images.hero[1].alt

### profile（プロフィール横の画像）
- {{ images.profile.url }}      ← images.profile.url
- {{ images.profile.alt }}      ← images.profile.alt

### before_after（3枚）
- {{ images.before_after.0.url }} ← images.before_after[0].url
- {{ images.before_after.0.alt }} ← images.before_after[0].alt
- {{ images.before_after.1.url }} ← images.before_after[1].url
- {{ images.before_after.1.alt }} ← images.before_after[1].alt
- {{ images.before_after.2.url }} ← images.before_after[2].url
- {{ images.before_after.2.alt }} ← images.before_after[2].alt

### doctor / procedure（任意だがGoldでは固定）
- {{ images.doctor.url }}       ← images.doctor.url
- {{ images.doctor.alt }}       ← images.doctor.alt
- {{ images.procedure.url }}    ← images.procedure.url
- {{ images.procedure.alt }}    ← images.procedure.alt

---

## 4. 治療情報（WP/IG共通）
- {{ treatment.name }}          ← treatment.name
- {{ treatment.sessions }}      ← treatment.sessions
- {{ treatment.time_minutes }}  ← treatment.time_minutes

- {{ treatment.injection_areas_session1 }} ← treatment.injection_areas_session1
- {{ treatment.injection_areas_session2 }} ← treatment.injection_areas_session2

### 製剤（products）
- {{ products_summary }}        ← treatment.products を「製剤名 数量単位」で結合（例： "ボリューマ 4本、ボラックス 3本、..."）
- {{ products_summary_short }}  ← IG向け短縮（例： "ボリューマ4本＋ボラックス3本＋ボルベラ2本"）
- {{ products_detail }}         ← セッション別の詳細文（入力にセッション分けがない場合は、生成側で「総合まとめ」+「セッション1/2の注入部位」構成で整形）

※本数/単位はOK。cc（注入量の具体値）は出力禁止。

---

## 5. 価格（WP/IG共通）
- {{ price.plan }}              ← price.plan
- {{ price.monitor_yen }}       ← price.monitor_yen（カンマ整形して表示：例 498,000）
- {{ price.regular_yen }}       ← price.regular_yen（カンマ整形して表示）

---

## 6. WP症例ページ専用：文章生成が必要な変数
### ファーストビュー結論
- {{ fv_conclusion }}
  ← age_decade + main_problems から要約して1文化
  例： "50代のたるみを改善し、構造的リフトで若々しい印象を回復"

### プロフィール文
- {{ profile_text }}
  ← 年代・性別を自然文へ（例："59歳女性。"）
  ※年齢が入力にない場合は「{{age_decade}} {{sex}}」で生成してOK

### 年代背景（一般論）
- {{ age_background_text }}
  ← age_decadeに応じた一般論（たるみ/ボリュームロス/複合悩み）を2〜4文

### 製剤選定理由（本文）
- {{ product_rationale_text }}
  ← products + 悩み + 部位設計をもとに2〜6文
  ※「層・役割・光と影」を入れる
- {{ products_compare_url }}
  ← 既定：/column/hyaluronic-acid-products-comparison/（サイトマップ正規スラッグのみ）

### Dr.こだわり3ブロック（見出し/本文/太字まとめ）
- {{ commitment_heading_1 }} ← 既定： "50代のたるみ改善は「線」ではなく「面」で設計する"
- {{ commitment_text_1 }}    ← 構造（骨/脂肪/靭帯）評価 + 面で設計
- {{ commitment_bold_summary }} ← 既定： "BiBiクリニックでは「支える構造」から設計し、表面だけの治療は行いません"
- {{ commitment_heading_2 }} ← 既定： "美的基準"
- {{ commitment_text_2 }}    ← 光と影・ハイライト位置・自然な立体感
- {{ commitment_heading_3 }} ← 既定： "安全性へのこだわり"
- {{ commitment_text_3 }}    ← 塞栓リスク + 対策（カニューレ/吸引確認/承認製剤/体制）

### Before/Afterの見るポイント
- {{ ba_watch_points }}
  ← main_problemsに応じた注目点を列挙（例："ほうれい線の深さ・頬の高さ・フェイスラインの引き締まり・顔全体のボリューム感"）

### 院長コメント（2段落）
- {{ doctor_comment_paragraph_1 }}
  ← Before/Afterで何が改善されたか（面・立体感・フェイスラインなど）を説明 + 患者の言葉を1文引用
- {{ doctor_comment_paragraph_2 }}
  ← “光/構造/自然/表情の動き” を必ず含め、2セッション設計の意義で締める

※口調：一人称「私」。煽り禁止。個人差は別箇所で担保。

### 患者の声
- {{ patient_voice }} ← patient_voice（入力）
- {{ voice_generalization_text }}
  ← 年代の課題 → 当院アプローチ一般化で2〜4文

### 向いている人（3つ）
- {{ fit_1 }} ← 年代 × たるみ老け見え
- {{ fit_2 }} ← 複合悩み（クマ/ほうれい線/フェイスラインなど）
- {{ fit_3 }} ← 自然に若返りたい/ヒアルロン酸リフト希望

### 関連導線メモ（短文）
- {{ related_links.0.label }} ← related_links[0].label
- {{ related_links.0.url }}   ← related_links[0].url
- {{ related_links.1.label }} ← related_links[1].label
- {{ related_links.1.url }}   ← related_links[1].url
- {{ related_links.2.label }} ← related_links[2].label
- {{ related_links.2.url }}   ← related_links[2].url

- {{ related_links_note_1 }}  ← related_links[1] の説明短文（生成）
- {{ related_links_note_2 }}  ← related_links[2] の説明短文（生成）

---

## 7. Instagram専用：生成が必要な変数
### スライド用
- {{ ig_hook_a }}             ← 変化重視の短いキャッチ（20字程度）
- {{ case_title_short }}      ← "59歳女性 ヒアルロン酸リフト" 等（短縮）
- {{ profile_short }}         ← "{{age_decade}} {{sex}}／主訴：{{main_problems_joined_short}}" 等
- {{ products_reason_short }} ← 製剤の役割を1〜2行に圧縮
- {{ result_explain_short }}  ← Before→Afterで見える変化を1〜2行
- {{ treatment_short }}       ← "ヒアルロン酸リフト（2回）" 等

### キャプション用（あなたの最新仕様）
- {{ empathy_catch }}         ← 共感キャッチ（20〜30字）
- {{ doctor_one_line_comment }} ← “ ” で囲う院長コメント1行
- {{ hashtags }}              ← 10〜15個（固定＋症例固有）

---

## 8. 3410の既定値（Gold症例で固定してよいもの）
- products_compare_url：/column/hyaluronic-acid-products-comparison/
- commitment_heading_* / commitment_bold_summary：Gold症例の文言を基本踏襲
- ba_watch_points：Gold症例の注目点を基本踏襲（必要に応じて悩みで調整）
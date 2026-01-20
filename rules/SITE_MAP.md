# SITE_MAP.md
# BiBiクリニック 正規URL・内部リンク定義（唯一のURLソース）
# 症例生成 / note / アメブロ派生で参照する。推測スラッグは禁止。

version: 1.0
last_updated: 2026-01-20

rules:
  - このファイルにないURLは出力禁止（推測スラッグ禁止）
  - 内部リンクは「internal_links.urls」のみ出力可能
  - internal_links が No.参照などURL不明な場合は TODO とし、リンク出力しない
  - “ピラー”表記はユーザー向け文言で使わない（総合ページに統一）
  - 料金・モニター表記は PRICE_SPEC 側が正とする（ここはURL/SEO設計のみ）

schema:
  id: "一意キー（生成でも参照）"
  content_group: "共通｜固定ページ / ヒアルロン酸｜総合ページ / ヒアルロン酸｜カテゴリ / コラム / 症例テンプレ 等"
  page_title: "ページタイトル"
  priority: "S/A/B/C/-"
  main_keyword: "メインKW"
  url: "絶対パス"
  initial_target_rank: "初期目標順位"
  sub_keywords: ["サブKW1", "サブKW2", "サブKW3"]
  internal_links:
    urls: ["内部リンク先URL（この配列のみ出力可）"]
    notes: "No参照等の補足。URLがないものはここに保持"
  deadline: "達成期限（例：3ヶ月/6ヶ月/-）"
  competition: "競合強度"
  seo:
    title_tag: "Title"
    meta_description: "Description"
  notes: "備考"
  status: "existing / to_make / to_update"

pages:

  # =========================
  # 共通｜固定ページ
  # =========================

  - id: COMMON_PRICES_TOP
    content_group: 共通｜固定ページ
    page_title: 料金表TOP｜大阪・心斎橋 BiBiクリニック
    priority: "-"
    main_keyword: 美容クリニック 料金表 大阪
    url: /prices/
    initial_target_rank: 30位以内
    sub_keywords: ["BiBiクリニック 料金", "美容医療 料金 大阪", "美容クリニック 価格"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/
        # 他カテゴリはURL未提示のため、現時点では出力禁止（TODO）
      notes: "各施術カテゴリ（HA/BTX/水光/脂肪溶解/ゼオスキン/アートメイク）→URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(比較検討)
    seo:
      title_tag: 料金表｜BiBiクリニック【BiBi-clinic】｜心斎橋で平日夜7時まで診療、ヒアルロン酸といえばBiBiクリニック
      meta_description: 大阪・心斎橋のBiBiクリニックの料金表。明瞭会計と安心価格設定で、安心して通える美容医療を大阪・心斎橋でご提供しています。全施術の料金を一元管理するハブページです。
    notes: 既存ページ
    status: existing

   - id: COMMON_CASE_TOP   # No.47
    content_group: 共通｜固定ページ
    page_title: 症例一覧TOP｜大阪・心斎橋 BiBiクリニック
    priority: "-"
    main_keyword: 症例一覧 大阪
    url: /case/
    initial_target_rank: 30位以内
    sub_keywords: ["ビフォーアフター 美容クリニック 大阪", "美容医療 症例 大阪", "ヒアルロン酸 症例"]
    internal_links:
      urls:
        - /column/guide-for-40s-women/
      notes: "各症例詳細ページ(No.10等)は /case/ 配下テンプレ（別途定義）。No.39（40代ハブ）はURL確定。"
    deadline: 6ヶ月
    competition: 中(ビジュアルCV)
    seo:
      title_tag: 症例｜BiBiクリニック【BiBi-clinic】｜心斎橋で平日夜7時まで診療、ヒアルロン酸といえばBiBiクリニック
      meta_description: 大阪・心斎橋のBiBiクリニックの症例一覧。自然に、美しく仕上がる美容医療を大阪・心斎橋でご提供。全症例を施術別・悩み別に絞り込めるハブページで最適な症例を探せます。
    notes: 既存ページ
    status: existing

  - id: TRUST_STAFF
    content_group: コラム：医師紹介
    page_title: 院長紹介｜BiBiクリニック 山本幸一郎（大阪・心斎橋）
    priority: "-"
    main_keyword: BiBiクリニック 院長
    url: /staff/
    initial_target_rank: 圏外OK
    sub_keywords: ["山本幸一郎 医師", "注入専門医 大阪", "美容クリニック 医師紹介"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/
        - /case/
      notes: "ピラー(No.1)/症例(No.10系)/40代ハブ(No.39)/クリニック選び(No.40) → URL一部未提示のためTODO"
    deadline: "-"
    competition: 弱(ブランド)
    seo:
      title_tag: 院長紹介｜BiBiクリニック 山本幸一郎（大阪・心斎橋）
      meta_description: 大阪・心斎橋のBiBiクリニック院長、山本幸一郎の紹介。自然な美しさと安全性を追求する注入専門医として、10年後を見据えた注入設計の理念と経歴をご紹介します。
    notes: 信頼構築要素。既存ページ
    status: existing

  - id: TRUST_CLINIC
    content_group: コラム：クリニック紹介
    page_title: BiBiクリニックについて｜大阪・心斎橋
    priority: "-"
    main_keyword: 美容クリニック 大阪 心斎橋
    url: /clinic/
    initial_target_rank: 30位以内
    sub_keywords: ["BiBiクリニック", "美容皮膚科 心斎橋", "美容クリニック 大阪"]
    internal_links:
      urls:
        - /column/first-visit-counseling/
        - /staff/
      notes: "ピラー(No.1) → /service/hyaluronic-acid/ は該当のため上記 staff から誘導、必要ならここにも追加可"
    deadline: 6ヶ月
    competition: 中(間接CV)
    seo:
      title_tag: BiBiクリニックについて｜大阪・心斎橋の美容皮膚科
      meta_description: 大阪・心斎橋のBiBiクリニックの理念・院内紹介・アクセス情報。「医療×アート」の融合を体現し、通うほど好きになるクリニック哲学をご紹介します。
    notes: ブランド信頼訴求。既存ページ
    status: existing

  - id: COMMON_CAMPAIGN
    content_group: 共通｜固定ページ
    page_title: キャンペーン一覧｜大阪・心斎橋 BiBiクリニック
    priority: "-"
    main_keyword: 美容クリニック キャンペーン 大阪
    url: /campaign/
    initial_target_rank: 圏外OK
    sub_keywords: ["BiBiクリニック キャンペーン", "美容医療 お得", "美容クリニック セール"]
    internal_links:
      urls: []
      notes: "各施術カテゴリ → URL未提示のためTODO"
    deadline: "-"
    competition: 弱(プロモーション)
    seo:
      title_tag: キャンペーン｜BiBiクリニック【BiBi-clinic】｜心斎橋で平日夜7時まで診療、ヒアルロン酸といえばBiBiクリニック
      meta_description: 大阪・心斎橋のBiBiクリニックのお得なキャンペーン情報。期間限定の特別プランで、この機会に美容医療を始めてみませんか。お得なキャンペーン一覧ページです。
    notes: 既存ページ
    status: existing

  - id: COMMON_GROUP
    content_group: 共通｜固定ページ
    page_title: BiBiグループ｜大阪・心斎橋 BiBiクリニック
    priority: "-"
    main_keyword: BiBiグループ
    url: /group/
    initial_target_rank: 圏外OK
    sub_keywords: ["BiBiクリニック グループ", "美容医療 グループ 大阪", "BiBiキャリア"]
    internal_links:
      urls:
        - /clinic/
      notes: "アートメイク(No.33) → URL未提示のためTODO"
    deadline: "-"
    competition: 弱(ブランド)
    seo:
      title_tag: BiBiグループ｜BiBiクリニック【BiBi-clinic】｜心斎橋で平日夜7時まで診療、ヒアルロン酸といえばBiBiクリニック
      meta_description: 大阪・心斎橋のBiBiグループの紹介。美容医療クリニックの運営だけでなく、アートメイクスクールやBiBiキャリアによる派遣事業も。多角的な美容医療サービス展開をご紹介します。
    notes: 既存ページ
    status: existing

  - id: COMMON_CANCEL_POLICY
    content_group: 共通｜固定ページ
    page_title: キャンセルポリシー｜大阪・心斎橋 BiBiクリニック
    priority: "-"
    main_keyword: 美容クリニック キャンセルポリシー 大阪
    url: /clinic/policy-cancel/
    initial_target_rank: 圏外OK
    sub_keywords: ["BiBiクリニック キャンセル", "美容クリニック 予約変更", "美容医療 キャンセル料"]
    internal_links:
      urls:
        - /column/first-visit-counseling/
      notes: "カウンセリング(No.42) = /column/first-visit-counseling/"
    deadline: "-"
    competition: 弱(信頼補強)
    seo:
      title_tag: キャンセルポリシー｜BiBiクリニック【BiBi-clinic】｜心斎橋で平日夜7時まで診療、ヒアルロン酸といえばBiBiクリニック
      meta_description: 大阪・心斎橋のBiBiクリニックのキャンセルポリシー。明確なキャンセル規定で安心してご利用いただけます。予約変更・キャンセルの手続き・注意事項についてご案内します。
    notes: 要制作
    status: to_make


  # =========================
  # ヒアルロン酸｜総合ページ（旧ピラー）
  # =========================

  - id: HA_ROOT
    content_group: ヒアルロン酸｜総合ページ
    page_title: 【大阪・心斎橋】ヒアルロン酸注入とは？効果・持続期間・料金・リスク・症例からわかる失敗しない選び方｜BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 大阪
    url: /service/hyaluronic-acid
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 注入", "ヒアルロン酸 効果", "ヒアルロン酸 症例"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/tear-trough/
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/lift/
        - /service/hyaluronic-acid/nose/
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/lowerface-chin/
        - /service/hyaluronic-acid/lips/
        - /service/hyaluronic-acid/neck/
        - /column/hyaluronic-acid-products-comparison/
        - /column/aging-mechanism/
        - /column/hyaluronic-acid-risk-embolism/
      notes: "額/こめかみ/製剤比較/老化/安全対策の導線はURL確定済み。額・こめかみのカテゴリURLは本文で別定義（下記参照）。"
    deadline: 3ヶ月
    competition: 強(S級KW)
    seo:
      title_tag: ヒアルロン酸注入の効果・料金・症例を医師が解説｜大阪 BiBiクリニック
      meta_description: 年間症例6500件。ヒアルロン酸注入の効果・持続期間・料金・リスクを医師が解説。大阪・心斎橋のBiBiクリニックで構造リフト設計に基づく自然な若返りを。症例写真、製剤比較も掲載。*2024年6月〜2025年5月院内集計
    notes: "総合ページハブ。「大阪」のみでNo.39との競合回避。医師が語る構造リフト設計理論。"
    status: to_update


  # =========================
  # ヒアルロン酸｜カテゴリ
  # =========================

  - id: HA_TEAR_TROUGH
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 涙袋注入｜大阪・心斎橋 BiBiクリニック
    priority: A
    main_keyword: 涙袋 ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/tear-trough/
    initial_target_rank: 20位以内
    sub_keywords: ["涙袋 ヒアルロン酸 自然", "涙袋 ヒアルロン酸 ダウンタイム", "涙袋 失敗"]
    internal_links:
      urls:
        - /service/hyaluronic-acid
        - /column/hyaluronic-acid-products-comparison/
        - /column/hyaluronic-acid-risk-embolism/
      notes: "症例(No.10系)は /case/ 配下（テンプレ定義あり）"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: 涙袋ヒアルロン酸｜派手にならない自然な涙袋形成｜大阪 BiBiクリニック
      meta_description: 涙袋がないor小さいとお悩みの方へ。大阪・心斎橋のBiBiクリニックで自然な涙袋ヒアルロン酸注入。派手にならない比率設計で優しい印象を。ボルベラ®使用・持続期間18ヶ月・20-30代症例80件公開中。
    notes: "派手すぎない涙袋デザイン理論。"
    status: to_make

  - id: HA_MIDFACE
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 頬 コケ改善｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 頬こけ 大阪
    url: /service/hyaluronic-acid/midface/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 頬こけ", "ゴルゴライン ヒアルロン酸", ""]
    internal_links:
      urls:
        - /service/hyaluronic-acid/lift/
        - /column/aging-mechanism/
        - /service/hyaluronic-acid
      notes: "40代ハブ(No.39) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: 中顔面ヒアルロン酸｜クマ・ゴルゴ・頬こけを光反射で改善｜大阪 BiBi
      meta_description: 中顔面のクマ・頬こけ・ゴルゴラインでお悩みの方へ。大阪・心斎橋のBiBiクリニックで光反射設計によるヒアルロン酸治療。骨格タイプ別の注入設計で立体感と若々しい印象へ。40代症例120件公開中。
    notes: "光反射理論を前半に配置。"
    status: to_make

  - id: HA_UNDEREYE_DARKCIRCLE
    content_group: ヒアルロン酸｜カテゴリ
    page_title: 目の下のクマ ヒアルロン酸治療｜影・凹み・青クマを見極めて改善｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: 目の下 クマ ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/undereye-darkcircle/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 目の下 クマ", "目の下 クマ 改善 ヒアルロン酸", "青クマ 黒クマ ヒアルロン酸"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/lift/
        - /column/aging-mechanism/
        - /column/hyaluronic-acid-risk-embolism/
        - /service/hyaluronic-acid
      notes: "40代ハブ(No.39) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: 目の下のクマにヒアルロン酸は有効？原因別に医師が解説｜大阪 BiBiクリニック
      meta_description: 影・凹み・青クマなど、目の下のクマの原因を見極めて行うヒアルロン酸治療。大阪・心斎橋BiBiクリニックでは中顔面構造と光反射を考慮した注入設計で、自然な若返りを実現。症例写真多数掲載。
    notes: "クマ特化CV直前KW回収ページ。"
    status: to_make

  - id: HA_LIFT_HUB
    content_group: ヒアルロン酸｜カテゴリ（ハブ）
    page_title: ヒアルロン酸リフト（たるみ・中顔面改善）｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 リフト 大阪
    url: /service/hyaluronic-acid/lift/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 たるみ 改善", "構造リフト", "ヒアルロン酸 リフトアップ"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/lowerface-chin/
        - /service/hyaluronic-acid
        - /column/aging-mechanism/
      notes: "構造的リフト理論の中心ハブ。"
    deadline: 6ヶ月
    competition: 強(S級KW)
    seo:
      title_tag: ヒアルロン酸リフト｜支える構造設計で若返り｜大阪 BiBiクリニック
      meta_description: ヒアルロン酸リフトで自然な若返りを。大阪・心斎橋のBiBiクリニックで「引き上げではなく支える」構造リフト理論。骨格・脂肪・靭帯の3層構造で根本改善。中顔面・ほうれい線・下顔面の治療事例と費用目安を詳しく解説します。
    notes: "構造リフト理論の中心ハブ。"
    status: to_make

  - id: HA_FOREHEAD
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 額 注入｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: 額 ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/forehead
    initial_target_rank: 20位以内
    sub_keywords: ["額 ボリューム", "額 丸み", ""]
    internal_links:
      urls:
        - /service/hyaluronic-acid
        - /column/hyaluronic-acid-products-comparison/
        - /column/aging-mechanism/
      notes: "症例(No.10系)は /case/ 配下"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: ヒアルロン酸 ひたい 注入｜大阪・心斎橋 BiBiクリニック
      meta_description: 額・こめかみのボリューム減少でお悩みの方へ。大阪・心斎橋のBiBiクリニックで額・こめかみヒアルロン酸注入。女性らしい丸み・男性らしい輪郭を性別別デザイン理論で設計。持続期間24ヶ月・症例60件公開中。
    notes: "性別別デザイン理論。"
    status: to_make

  - id: HA_TEMPLE
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 こめかみ注入｜凹み・骨感を自然に改善｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: こめかみ ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/temple
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 こめかみ", "こめかみ 凹み 改善", "こめかみ ボリューム"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/forehead
        - /service/hyaluronic-acid/lift/
        - /column/aging-mechanism/
        - /column/hyaluronic-acid-products-comparison/
        - /service/hyaluronic-acid
      notes: "額とセット評価。送客導線重視。"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: こめかみヒアルロン酸注入で自然な若返り｜大阪 BiBiクリニック
      meta_description: こめかみの凹みや骨感が気になる方へ。大阪・心斎橋のBiBiクリニックでは、側頭部の解剖と顔全体バランスを考慮したヒアルロン酸注入で、痩せ見え・老け感を自然に改善します。症例写真も多数掲載。
    notes: "単独CVより構造リフト/中顔面への導線優先。"
    status: to_make

  - id: HA_NOSE
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 鼻筋・鼻根注入｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: 鼻 ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/nose/
    initial_target_rank: 20位以内
    sub_keywords: ["鼻筋 ヒアルロン酸", "ヒアルロン酸 鼻 安全", "鼻根 ヒアルロン酸"]
    internal_links:
      urls:
        - /column/hyaluronic-acid-risk-embolism/
        - /column/hyaluronic-acid-products-comparison/
        - /service/hyaluronic-acid
      notes: "症例(No.10系)は /case/ 配下"
    deadline: 6ヶ月
    competition: 強(塞栓リスク認知)
    seo:
      title_tag: 鼻筋ヒアルロン酸｜塞栓対策と層構造の安全設計｜大阪 BiBiクリニック
      meta_description: 鼻筋を自然に整えたい方へ。大阪・心斎橋のBiBiクリニックで安全性を最優先した鼻ヒアルロン酸注入。層構造理論と血管走行把握で塞栓リスクを最小化。緊急時対応体制完備。鼻筋・鼻根の症例50件公開中。
    notes: "医療安全訴求。"
    status: to_make

  - id: HA_NASOLABIAL_FOLD
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 ほうれい線注入（マリオネットライン含む）｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 ほうれい線 大阪
    url: /service/hyaluronic-acid/nasolabial-fold/
    initial_target_rank: 10位以内
    sub_keywords: ["ほうれい線 ヒアルロン酸", "ほうれい線 たるみ", "マリオネットライン ヒアルロン酸"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/lift/
        - /column/hyaluronic-acid-products-comparison/
        - /prices/hyaluronic-acid/
        - /column/first-visit-counseling/
        - /service/hyaluronic-acid
      notes: "40代ハブ(No.39) → URL未提示のためTODO"
    deadline: 3ヶ月
    competition: 強(最重要CV-KW)
    seo:
      title_tag: ほうれい線ヒアルロン酸｜骨格支点から根本改善｜大阪 BiBiクリニック
      meta_description: ほうれい線のたるみでお悩みの方へ。大阪・心斎橋のBiBiクリニックで骨格支点リフト設計によるヒアルロン酸注入。表面ではなく骨格・脂肪・靭帯から支える3層構造治療で-5歳の印象変化を。40代症例150件以上公開。今すぐ無料カウンセリングへ。
    notes: "最重要CVページ。CTA強化。"
    status: to_make

  - id: HA_LOWERFACE_CHIN
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 下顔面（あご・フェイスライン）注入｜大阪・心斎橋 BiBiクリニック
    priority: A
    main_keyword: あご ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/lowerface-chin/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 フェイスライン", "Eライン ヒアルロン酸", "あご 形成"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/lift/
        - /column/hyaluronic-acid-products-comparison/
        - /service/hyaluronic-acid
      notes: "ボトックス比較(No.17)/脂肪溶解(No.31) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: 下顔面・あごヒアルロン酸｜Eライン×黄金比の3D設計｜大阪 BiBi
      meta_description: フェイスラインやあごの形でお悩みの方へ。大阪・心斎橋のBiBiクリニックで下顔面・あごヒアルロン酸注入。Eライン×黄金比の3Dバランス理論で横顔美人を実現。骨格タイプ別の輪郭形成・症例90件公開中。
    notes: "Eライン×黄金比を前半配置。"
    status: to_make

  - id: HA_LIPS
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 リップ（唇）注入｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: リップ ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/lips/
    initial_target_rank: 30位以内
    sub_keywords: ["唇 ヒアルロン酸", "リップ ヒアルロン酸 料金", "ヒアルロン酸 リップ 持続"]
    internal_links:
      urls:
        - /column/hyaluronic-acid-products-comparison/
        - /service/hyaluronic-acid
      notes: "症例(No.10系)は /case/ 配下"
    deadline: 6ヶ月
    competition: 中(A級KW)
    seo:
      title_tag: リップヒアルロン酸｜上下比率×スマイルラインの大人設計｜大阪 BiBi
      meta_description: 唇のボリュームやバランスでお悩みの方へ。大阪・心斎橋のBiBiクリニックでリップヒアルロン酸注入。上下比率×スマイルラインの分析で自然なボリュームと笑顔の調和を実現。世代別リップデザイン・症例70件公開中。
    notes: "上下比率×スマイルライン。"
    status: to_make

  - id: HA_NECK
    content_group: ヒアルロン酸｜カテゴリ
    page_title: ヒアルロン酸 首（ネック）注入｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: 首 シワ ヒアルロン酸 大阪
    url: /service/hyaluronic-acid/neck/
    initial_target_rank: 圏外OK
    sub_keywords: ["首 ヒアルロン酸", "ネックライン ヒアルロン酸", "首 たるみ"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/lift/
        - /column/hyaluronic-acid-products-comparison/
        - /service/hyaluronic-acid
      notes: "症例(No.10系)は /case/ 配下"
    deadline: 6ヶ月
    competition: 弱(ニッチKW)
    seo:
      title_tag: 首のシワ改善ヒアルロン酸｜顔との一体デザイン｜大阪 BiBiクリニック
      meta_description: 首のシワやたるみでお悩みの方へ。大阪・心斎橋のBiBiクリニックで首ヒアルロン酸注入。顔との一体デザインで若々しい印象へ。ネックエイジング理論とボライト®使用例・持続期間24ヶ月・症例30件を公開中。
    notes: "ネックデザイン訴求（優先度低）。"
    status: to_make


  # =========================
  # ヒアルロン酸｜症例（テンプレ）
  # =========================

  - id: HA_CASE_TEMPLATE
    content_group: ヒアルロン酸｜症例テンプレ
    page_title: "{年代}女性／{主訴}を{製剤名}で改善【大阪・心斎橋 BiBiクリニック】"
    priority: S
    main_keyword: "{主訴} 症例写真 大阪"
    url: "/case/{年代}-{主訴slug}-{製剤名slug}/"
    initial_target_rank: 30位以内
    sub_keywords: ["{年代} {主訴} ビフォーアフター", "{製剤名} 効果 写真", "{主訴} ヒアルロン酸 費用"]
    internal_links:
      urls:
        - /prices/hyaluronic-acid/
        - /case/
        - /service/hyaluronic-acid
      notes: "症例は該当カテゴリ（涙袋/中顔面/ほうれい線等）へ戻す導線を必須。カテゴリURLは上記定義から選択。"
    deadline: 6ヶ月
    competition: 中(ビジュアルCV)
    seo:
      title_tag: "{年代}{主訴}改善症例｜{製剤名} 費用{金額}｜大阪 BiBiクリニック"
      meta_description: "{年代}女性の{主訴}改善症例。{製剤名}を使用した治療をビフォーアフター写真で公開。施術費用{金額}・ダウンタイム{期間}・{特記事項}。{独自設計理論}による注入設計を医師が詳しく解説。大阪・心斎橋 BiBiクリニック。"
    notes: "E-E-A-T補強。テンプレ。"
    status: to_update


  # =========================
  # 共通コラム（信頼導線）
  # =========================

  - id: TRUST_FIRST_VISIT
    content_group: 共通コラム（信頼導線）
    page_title: 初診カウンセリングの流れ｜無料・無理な勧誘なし｜大阪 BiBiクリニック
    priority: S
    main_keyword: 美容クリニック カウンセリング 大阪
    url: /column/first-visit-counseling/
    initial_target_rank: 20位以内
    sub_keywords: ["初診 流れ 美容クリニック", "無料カウンセリング 大阪", "美容クリニック 初めて"]
    internal_links:
      urls:
        - /staff/
        - /clinic/
        - /prices/
      notes: "FAQ(No.44) → URL未提示のためTODO"
    deadline: 3ヶ月
    competition: 中(CV直前)
    seo:
      title_tag: 初診カウンセリングの流れ｜無料・無理な勧誘なし｜大阪 BiBi
      meta_description: 初めての美容医療も安心。大阪・心斎橋のBiBiクリニックで「納得してから決める」BiBi式カウンセリング哲学。院長が直接診察し丁寧にご提案。当日施術も可能で無理な勧誘は一切ありません。今すぐWEB/LINE予約へ。
    notes: "全ページフッターに予約CTA導線。"
    status: to_make


  # =========================
  # コラム：製剤 / 安全 / 基礎 / 併用
  # =========================

  - id: COLUMN_HA_PRODUCTS_COMPARISON
    content_group: コラム：製剤別解説
    page_title: アラガン社ヒアルロン酸®全シリーズ徹底比較｜ボリューマ®・ボリフト®・ボラックス®・ボルベラ®・ボライト®・ウルトラプラス
    priority: A
    main_keyword: ヒアルロン酸 製剤 比較
    url: /column/hyaluronic-acid-products-comparison/
    initial_target_rank: 30位以内
    sub_keywords: ["アラガン ヒアルロン酸", "ボリューマ ボリフト 違い", "ヒアルロン酸 種類"]
    internal_links:
      urls:
        - /service/hyaluronic-acid
        - /prices/hyaluronic-acid/
        - /case/
      notes: "各部位カテゴリは HA_ROOT/各カテゴリへ誘導"
    deadline: 6ヶ月
    competition: 中(比較検討層)
    seo:
      title_tag: アラガン社ヒアルロン酸®全シリーズ徹底比較｜大阪 BiBiクリニック
      meta_description: アラガン社製剤の違いを医師が徹底比較。ボリューマ・ボリフト・ボラックス・ボルベラ・ボライトの弾性・親水性・層構造を可視化した早見表で最適な選択を。部位別適応マップと費用対効果を詳しく解説。大阪・心斎橋 BiBiクリニック。
    notes: "層構造×適応マップで差別化。"
    status: to_make

  - id: COLUMN_HA_RISK_EMBOLISM
    content_group: コラム：安全対策
    page_title: ヒアルロン酸塞栓・失敗を防ぐために知っておくべきリスクと対処法
    priority: S
    main_keyword: ヒアルロン酸 塞栓
    url: /column/hyaluronic-acid-risk-embolism/
    initial_target_rank: 30位以内
    sub_keywords: ["ヒアルロン酸 失敗", "ヒアルロン酸 血管閉塞", "ヒアルロン酸 失敗例"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/nose/
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/lowerface-chin/
        - /column/hyaluronic-acid-products-comparison/
      notes: "クリニック選び(No.40) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(不安解消CV)
    seo:
      title_tag: ヒアルロン酸注入の塞栓・失敗リスクと対策｜大阪 BiBiクリニック
      meta_description: ヒアルロン酸注入の塞栓・失敗例から学ぶ安全対策。大阪・心斎橋のBiBiクリニックで血管閉塞の緊急時対応から予防まで、医師が実践する安全注入マニュアルとBiBi式リスクゼロ設計を公開。失敗例との違いを詳しく解説します。
    notes: "リスク管理SEO。"
    status: to_make

  - id: COLUMN_AGING_MECHANISM
    content_group: コラム：基礎知識
    page_title: たるみ・老化のメカニズム｜肌の構造からわかる変化と対策
    priority: B
    main_keyword: 顔 老化 メカニズム
    url: /column/aging-mechanism/
    initial_target_rank: 圏外OK
    sub_keywords: ["たるみ 原因", "骨吸収 顔", "脂肪萎縮"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/lowerface-chin/
        - /service/hyaluronic-acid/lift/
      notes: "40代ハブ(No.39) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 弱(教育コンテンツ)
    seo:
      title_tag: たるみ・老化の原因とヒアルロン酸対策｜大阪 BiBiクリニック
      meta_description: たるみ・老化のメカニズムを医師が徹底解説。骨・脂肪・皮膚の変化を分析し、「老化は減る現象」という理論から年代別ヒアルロン酸の予防アプローチへ。大阪・心斎橋のBiBiクリニックで構造リフト設計の理論的背景をご紹介します。
    notes: "理論系SEO。"
    status: existing

  - id: COLUMN_HA_BTX_COMBINATION
    content_group: コラム：比較・併用・順序
    page_title: ボトックスとヒアルロン酸の違い・順番・併用効果を医師が解説
    priority: B
    main_keyword: ボトックス ヒアルロン酸 違い
    url: /column/hyaluronic-acid-botox-combination/
    initial_target_rank: 20位以内
    sub_keywords: ["ボトックス ヒアルロン酸 併用", "ボトックス ヒアルロン酸 順番", "ボトックス ヒアルロン酸 同時"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/lowerface-chin/
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/lift/
      notes: "ボトックス総合ページ(No.18) → URL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(併用検討層)
    seo:
      title_tag: ボトックスとヒアルロン酸の違いを医師が徹底比較｜大阪 BiBi
      meta_description: ボトックスとヒアルロン酸の違いを医師が徹底比較。効果・持続期間・併用順番の早見表で最適な選択を。「動き」と「支え」を両立する家の構造理論に基づく併用設計・間隔・同時施術の可否を詳しく解説。大阪・心斎橋 BiBiクリニック。
    notes: "併用設計理論。"
    status: to_make

  - id: COLUMN_INJECTION_COMPARISON
    content_group: 共通｜コラム
    page_title: ヒアルロン酸・ボトックス・脂肪溶解の違い｜大阪・心斎橋 BiBiクリニック
    priority: C
    main_keyword: ヒアルロン酸 ボトックス 違い
    url: /column/injection-comparison/
    initial_target_rank: 30位以内
    sub_keywords: ["ヒアルロン酸 ボトックス 脂肪溶解", "美容注射 種類", "美容注射 比較"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/
      notes: "BTX/FatXの総合ページURL未提示のためTODO"
    deadline: 6ヶ月
    competition: 中(初診導線)
    seo:
      title_tag: ヒアルロン酸・ボトックス・脂肪溶解の違いを徹底比較｜大阪/ BiBi
      meta_description: 美容注射の違いを医師が徹底比較。「足す(HA)・動かす(BTX)・減らす(FatX)」の効果・ダウンタイム・費用感を早見表で横断比較。大阪・心斎橋のBiBiクリニックで目的別チャートであなたに合う治療を無料診断。
    notes: "初診導線のナビ役。"
    status: to_make

  - id: COLUMN_GUIDE_40S_WOMEN
    content_group: ヒアルロン酸｜コラム（ペルソナ）
    page_title: 40代女性のためのヒアルロン酸注入完全ガイド｜失敗しない選び方｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 40代 大阪
    url: /column/guide-for-40s-women/
    initial_target_rank: 15位以内
    sub_keywords: ["40代 たるみ 改善", "40代 ほうれい線 ヒアルロン酸", "ヒアルロン酸 40代 おすすめ"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/midface/
        - /prices/hyaluronic-acid/
        - /case/
        - /column/first-visit-counseling/
      notes: "クリニック選び(No.40) → URL未提示のためTODO"
    deadline: 3ヶ月
    competition: 強(ペルソナ直撃)
    seo:
      title_tag: 40代女性のためのヒアルロン酸注入完全ガイド｜大阪 BiBi
      meta_description: 40代のたるみ・ほうれい線改善ガイド。大阪・心斎橋のBiBiクリニックで「減る美容→支える美容」設計を。骨格・脂肪・靭帯の優先順位別治療プラン・費用目安15-30万円・40代症例50件を公開。無料カウンセリングで10年後を見据えた設計を。
    notes: "ヒーロー直下CTA/サイド固定バナー。No.1との競合回避（サブKWで差別化）。"
    status: to_make

  - id: COLUMN_HOW_TO_CHOOSE_CLINIC
    content_group: コラム（不安解消）
    page_title: ヒアルロン酸で失敗しないクリニックの選び方｜7チェック｜大阪 心斎橋BiBiクリニック
    priority: A
    main_keyword: ヒアルロン酸 失敗 大阪
    url: /column/how-to-choose-clinic/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 クリニック 選び方", "美容クリニック 選び方", "ヒアルロン酸 安全"]
    internal_links:
      urls:
        - /column/hyaluronic-acid-risk-embolism/
        - /case/
        - /staff/
        - /prices/hyaluronic-acid/
        - /column/first-visit-counseling/
      notes: "相談CTA強め（LINE/WEB）。"
    deadline: 6ヶ月
    competition: 中(CV直前)
    seo:
      title_tag: ヒアルロン酸で失敗しないクリニックの選び方｜7チェック｜大阪 BiBi
      meta_description: ヒアルロン酸クリニックの選び方を医師が解説。失敗例から学ぶ7つのチェックポイントで「後悔しない選択」を。大阪・心斎橋のBiBiクリニックでBiBi式安全体制・症例・医師紹介・料金を詳しくご紹介。今すぐ無料カウンセリングへ。
    notes: "不安解消→CV直前導線。"
    status: to_make

  - id: PRICES_HA
    content_group: コラム（不安解消）※価格ページ
    page_title: ヒアルロン酸の料金・年代別プラン｜モニター情報｜大阪 BiBi
    priority: S
    main_keyword: ヒアルロン酸 料金 大阪
    url: /prices/hyaluronic-acid/
    initial_target_rank: 15位以内
    sub_keywords: ["ヒアルロン酸 相場 大阪", "ヒアルロン酸 モニター 大阪", "ヒアルロン酸 価格"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/tear-trough/
        - /service/hyaluronic-acid/midface/
        - /service/hyaluronic-acid/undereye-darkcircle/
        - /service/hyaluronic-acid/lift/
        - /service/hyaluronic-acid/forehead
        - /service/hyaluronic-acid/temple
        - /service/hyaluronic-acid/nose/
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/lowerface-chin/
        - /service/hyaluronic-acid/lips/
        - /service/hyaluronic-acid/neck/
        - /column/hyaluronic-acid-products-comparison/
        - /case/
        - /column/first-visit-counseling/
      notes: "40代ハブ(No.39) → URL未提示のためTODO"
    deadline: 3ヶ月
    competition: 強(CV直前)
    seo:
      title_tag: ヒアルロン酸の料金・40代プラン・モニター情報｜大阪 BiBiクリニック
      meta_description: ヒアルロン酸の料金を明瞭公開。大阪・心斎橋のBiBiクリニックで製剤別料金と40代向けプランの費用対効果を医師が解説。「本数より設計」の考え方でモニター情報もご案内。15-30万円プラン例も詳しくご紹介します。
    notes: "価格表下に注意書き定型文固定（別Spec）。"
    status: to_update

  # =========================
  # コラム：ガイド（年代ハブ）
  # =========================

  - id: HA_GUIDE_40S_WOMEN   # No.39
    content_group: ヒアルロン酸｜カテゴリ（年代ハブ）
    page_title: 40代女性のためのヒアルロン酸注入完全ガイド｜失敗しない選び方｜大阪・心斎橋 BiBiクリニック
    priority: S
    main_keyword: ヒアルロン酸 40代 大阪
    url: /column/guide-for-40s-women/
    initial_target_rank: 15位以内
    sub_keywords: ["40代 たるみ 改善", "40代 ほうれい線 ヒアルロン酸", "ヒアルロン酸 40代 おすすめ"]
    internal_links:
      urls:
        - /service/hyaluronic-acid/nasolabial-fold/
        - /service/hyaluronic-acid/midface/
        - /prices/hyaluronic-acid/
        - /column/how-to-choose-clinic/
        - /case/
        - /column/first-visit-counseling/
      notes: "No.6=ほうれい線 / No.3=中顔面 / No.41=HA料金 / No.40=クリニック選び / No.47=症例一覧TOP / No.42=初診カウンセリング"
    deadline: 40
    competition: "-"
    seo:
      title_tag: 40代女性のためのヒアルロン酸注入完全ガイド｜失敗しない選び方｜大阪・心斎橋 BiBiクリニック
      meta_description: "※未入力（元表にDescriptionがないため）。入れたい場合は追記する。"
    notes: "No.39 URL確定。年代特化ハブ。"
    status: to_make


  # =========================
  # コラム：不安解消（クリニック選び）
  # =========================

  - id: HA_HOW_TO_CHOOSE_CLINIC  # No.40
    content_group: コラム（不安解消）
    page_title: ヒアルロン酸で失敗しないクリニックの選び方｜7チェック｜大阪 心斎橋BiBiクリニック
    priority: A
    main_keyword: ヒアルロン酸 失敗 大阪
    url: /column/how-to-choose-clinic/
    initial_target_rank: 20位以内
    sub_keywords: ["ヒアルロン酸 クリニック 選び方", "美容クリニック 選び方", "ヒアルロン酸 安全"]
    internal_links:
      urls:
        - /column/hyaluronic-acid-risk-embolism/
        - /case/
        - /staff/
        - /prices/hyaluronic-acid/
        - /column/first-visit-counseling/
      notes: "No.14=塞栓/安全対策 / No.47=症例一覧TOP / No.12=医師紹介 / No.41=HA料金 / No.42=初診カウンセリング"
    deadline: "-"
    competition: "-"
    seo:
      title_tag: ヒアルロン酸で失敗しないクリニックの選び方｜7チェック｜大阪 心斎橋BiBiクリニック
      meta_description: "※未入力（元表にDescriptionがないため）。入れたい場合は追記する。"
    notes: "No.40 URL確定。不安解消CV導線。"
    status: to_make
  # =========================
- id: BTX_PILLAR   # No.18
  content_group: ボトックス｜ピラー
  page_title: 【大阪・心斎橋】ボトックス注入とは？効果・持続期間・料金・副作用・症例からわかる失敗しない選び方｜BiBiクリニック
  priority: B
  main_keyword: ボトックス 大阪
  url: /service/botox/
  initial_target_rank: 30位以内
  sub_keywords: ["ボトックス 表情じわ", "ボトックス 効果", "ボトックス 料金"]
  internal_links:
    urls:
      - /service/botox/facial-expression/
      - /service/botox/masseter/
      - /service/botox/body/
      - /column/injection-comparison/
  deadline: 6ヶ月
  competition: 中(A級KW)
  seo:
    title_tag: ボトックス注入で表情じわを整える｜大阪 BiBiクリニック
    meta_description: 大阪・心斎橋のBiBiクリニックでは、ボトックス注入の効果・持続期間・料金・副作用・症例を医師が詳しく解説。表情じわ改善から小顔・肩こり・多汗症まで、部位別の考え方と失敗しない選び方がわかります。
  notes: 既存ページ。CTA直下に「カテゴリへ戻る」導線を必ず配置
  status: existing
  
  
  - id: BTX_FACIAL_EXPRESSION   # No.19
  content_group: ボトックス｜カテゴリ
  page_title: 【大阪・心斎橋】表情筋ボトックス（額・眉間・目尻・口角・顎・人中ボトックス）｜自然な表情を保つ注入設計｜BiBiクリニック
  priority: B
  main_keyword: ボトックス 額 大阪
  url: /service/botox/facial-expression/
  initial_target_rank: 30位以内
  sub_keywords: ["ボトックス 眉間", "ボトックス 目尻", "表情じわ ボトックス"]
  internal_links:
    urls:
      - /service/botox/
      - /column/injection-comparison/
  deadline: 6ヶ月
  competition: 中(A級KW)
  seo:
    title_tag: 額・眉間・目尻の表情じわボトックス｜自然な表情設計｜大阪 BiBi
    meta_description: 額・眉間・目尻の表情じわでお悩みの方へ。大阪・心斎橋のBiBiクリニックで表情筋ボトックス。部位別単位・持続期間・副作用を医師が丁寧に解説。
  notes: 表情時／安静時の2枚組写真を標準仕様
  status: planned

- id: BTX_MASSETER   # No.20
  content_group: ボトックス｜カテゴリ
  page_title: 【大阪・心斎橋】エラボトックス（咬筋ボトックス）｜小顔・左右差補正でフェイスラインを整える｜BiBiクリニック
  priority: B
  main_keyword: エラ ボトックス 大阪
  url: /service/botox/masseter/
  initial_target_rank: 20位以内
  sub_keywords: ["エラボトックス 小顔", "咬筋ボトックス", "ボトックス 小顔"]
  internal_links:
    urls:
      - /service/botox/
      - /service/hyaluronic-acid/lowerface-chin/
      - /column/injection-comparison/
  deadline: 6ヶ月
  competition: 中(A級KW)
  seo:
    title_tag: エラボトックスでフェイスライン小顔｜左右差補正設計｜大阪 BiBi
    meta_description: エラ張りや食いしばりでお悩みの方へ。咬筋の発達を見極め、左右差補正を行うエラボトックスを医師が解説。
  notes: 食いしばり問診票をDL可能に
  status: planned
  
- id: BTX_BODY   # No.21
  content_group: ボトックス｜カテゴリ
  page_title: 【大阪・心斎橋】肩こり・ふくらはぎ・太もも・二の腕ボトックス｜筋肉由来の張りを整える｜BiBiクリニック
  priority: B
  main_keyword: ボトックス 肩 大阪
  url: /service/botox/body/
  initial_target_rank: 圏外OK
  sub_keywords: ["肩ボトックス 美容", "ふくらはぎ ボトックス", "太もも ボトックス"]
  internal_links:
    urls:
      - /service/botox/
      - /column/injection-comparison/
  deadline: 6ヶ月
  competition: 弱〜中
  seo:
    title_tag: 肩・脚・腕ボトックス｜用量漸増法で副作用最小化｜大阪 BiBi
    meta_description: 肩こり・脚痩せ・腕ライン改善に対応したボディボトックス。筋活動を残す設計で日常動作への影響を最小化。
  notes: 各部位のPHILOSOPHY_{AREA}.mdを症例生成時に必ず参照
  status: planned  
  
- id: BTX_BODY   # No.21
  content_group: ボトックス｜カテゴリ
  page_title: 【大阪・心斎橋】肩こり・ふくらはぎ・太もも・二の腕ボトックス｜筋肉由来の張りを整える｜BiBiクリニック
  priority: B
  main_keyword: ボトックス 肩 大阪
  url: /service/botox/body/
  initial_target_rank: 圏外OK
  sub_keywords: ["肩ボトックス 美容", "ふくらはぎ ボトックス", "太もも ボトックス"]
  internal_links:
    urls:
      - /service/botox/
      - /column/injection-comparison/
  deadline: 6ヶ月
  competition: 弱〜中
  seo:
    title_tag: 肩・脚・腕ボトックス｜用量漸増法で副作用最小化｜大阪 BiBi
    meta_description: 肩こり・脚痩せ・腕ライン改善に対応したボディボトックス。筋活動を残す設計で日常動作への影響を最小化。
  notes: 各部位のPHILOSOPHY_{AREA}.mdを症例生成時に必ず参照
  status: planned
  
- id: ARTMAKE_PILLAR   # No.33
  content_group: アートメイク｜ピラー
  page_title: 【大阪・心斎橋】医療アートメイク（眉・リップ）｜デザイン・持続期間・ダウンタイム・料金・リスクまで｜BiBiクリニック
  priority: C
  main_keyword: アートメイク 大阪
  url: /service/artmake/
  initial_target_rank: 30位以内
  sub_keywords: ["医療アートメイク 大阪", "アートメイク 心斎橋", "アートメイク 眉"]
  internal_links:
    urls:
      - /service/artmake/eyebrow/
      - /service/artmake/lip/
      - /column/artmake-safety-design/
  deadline: 6ヶ月
  competition: 中(A級KW)
  seo:
    title_tag: 医療アートメイク（眉・リップ）｜大阪・心斎橋 BiBiクリニック
    meta_description: 医師監修の医療アートメイク総論。眉・リップのデザイン、持続期間、ダウンタイム、料金、リスクまで詳しく解説。
  notes: 施術者紹介・衛生基準を必須掲載
  status: existing  
    
- id: ARTMAKE_EYEBROW   # No.34
  content_group: アートメイク｜カテゴリ
  page_title: 眉アートメイク｜自然な黄金比デザインと毛流れ設計｜大阪・心斎橋 BiBiクリニック
  url: /service/artmake/eyebrow/

- id: ARTMAKE_LIP   # No.35
  content_group: アートメイク｜カテゴリ
  page_title: リップアートメイク｜血色と輪郭を自然に整える｜大阪・心斎橋 BiBiクリニック
  url: /service/artmake/lip/
    
- id: ARTMAKE_SAFETY   # No.37
  content_group: 共通コラム
  page_title: 医療アートメイクの安全性とデザイン理論｜大阪・心斎橋 BiBiクリニック
  url: /column/artmake-safety-design/  
  
- id: FATMELT_PILLAR   # No.30
  content_group: 脂肪溶解｜ピラー
  page_title: 脂肪溶解注射（FatX・カベリン）｜大阪・心斎橋 BiBiクリニック
  url: /service/fat-melt/
  
 - id: SKINBOOSTER_PILLAR   # No.24
  content_group: 水光注射｜ピラー
  page_title: 水光注射（スキンブースター）｜大阪・心斎橋 BiBiクリニック
  url: /skin-booster/   
  # =========================

  # - id: COLUMN_FACIAL_GOLDEN_RATIO
  #   content_group: コラム
  #   page_title: 黄金比で整えるヒアルロン酸デザイン｜Eライン・顔バランスを医師が解説｜大阪・心斎橋BiBiクリニック
  #   priority: A
  #   main_keyword: ヒアルロン酸 黄金比
  #   url: /column/facial-golden-ratio
  #   initial_target_rank: 15位以内（3ヶ月以内）
  #   sub_keywords: ["Eライン ヒアルロン酸", "唇 黄金比 形成", "顔 黄金比 バランス"]
  #   internal_links:
  #     urls:
  #       - /service/hyaluronic-acid/lift/
  #       - /column/aging-mechanism/
  #       - /service/hyaluronic-acid/lowerface-chin/
  #       - /service/hyaluronic-acid/midface/
  #     notes: ""
  #   deadline: 3ヶ月
  #   competition: ""
  #   seo:
  #     title_tag: ""
  #     meta_description: ""
  #   notes: ""
  #   status: to_make
  
    - FAQ(No.44)はURL未提示のため現時点では未定義扱い（生成物にリンクを出力しない）
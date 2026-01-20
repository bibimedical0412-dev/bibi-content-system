# INPUT_SCHEMA.md（案）

## 必須（これがないと生成不可）
case_id: "3410"
age_decade: "50代"        # 例：20代/30代/40代/50代/60代
sex: "女性"
main_problems: ["目の下のクマ","ほうれい線","フェイスラインのたるみ","顎/顎先"]
seo_title: "50代女性 ヒアルロン酸リフト 症例..."    # 症例タイトル
keywords: ["ヒアルロン酸リフト","50代","たるみ改善","大阪"]   # 2〜4
meta_description: "..."   # 80〜120字目安
category_url: "/service/hyaluronic-acid/lift/"        # 総合ページURL（正規）
final_slug: "/hyaluronic-acid/lift/50s-ha-lift-aging" # 完成URL（正規）

images:
  hero:
    - url: "..." # 正面BA
      alt: "..."
    - url: "..." # 斜めBA
      alt: "..."
  profile: { url: "...", alt: "..." }
  before_after:
    - { url: "...", alt: "...", angle: "正面" }
    - { url: "...", alt: "...", angle: "右斜め" }
    - { url: "...", alt: "...", angle: "左斜め" }
  doctor: { url: "...", alt: "..." }  # 任意（なければ固定素材）
  procedure: { url: "...", alt: "..." } # 任意

treatment:
  name: "ヒアルロン酸注入術"
  sessions: 2
  time_minutes: "10〜30分"
  products:
    - { name: "ボリューマ", count: 4, unit: "本" }
    - { name: "ボラックス", count: 3, unit: "本" }
    - { name: "ボルベラ", count: 2, unit: "本" }
    - { name: "ボツラックス", count: 50, unit: "単位" }
  injection_areas_session1: "..."  # 表示用テキスト
  injection_areas_session2: "..."

price:
  plan: "部分モニター"  # 全顔/部分の判定はPRICE_SPECに従う
  monitor_yen: 498000
  regular_yen: 553200

risks: ["内出血","腫れ","痛み","左右差","感染","アレルギー反応","塞栓"]

doctor_comment_seed: >
  # 任意：カルテや所見から「狙い」を数行で入れておくと精度が上がる

patient_voice: >
  全然違いますね。顔が引き締まっていて嬉しいです。ありがとうございました。

related_links:
  - { label: "ヒアルロン酸リフト総合ページ", url: "/service/hyaluronic-acid/lift/" }
  - { label: "顎・フェイスラインのヒアルロン酸", url: "/service/hyaluronic-acid/lowerface-chin/" }
  - { label: "ボトックス注射", url: "/service/botox/" }

publish_targets:
  - wordpress
  - note
  - ameblo 
  - 

- 主対象は title / category_url / wp_path から判定する
- botox/ が含まれる場合、treatment_type = BOTX
- BOTX症例ページでは、ヒアルロン酸・アートメイク等の他施術ログは無視する
- 併用症例として扱う場合のみ、入力に「併用：◯◯＋◯◯」の明示がある場合に限る
- 明示がない限り、主対象以外の施術は生成・言及しない 
- 
## ARTMAKE fields（追加）
- target.area: brow|lip|eyeline|other
- target.technique: 例）4D（毛並み+パウダー）/ パウダー / 毛並み など
- target.pigment_note: 例）ブラウン系、医療用色素 等（不明なら空欄）
- target.sessions: 例）1回目/2回予定、1回のみ、2回目 など
- time_required: 例）約120分
- monitor_type: 全顔|部分|不明（部分が基本になりやすいが、入力優先）
- risks: 入力がある場合はそれをそのまま優先 
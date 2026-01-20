# STEP_A_PHILOSOPHY_SPEC.md
# 症例生成 Step A-Philosophy 仕様書（PHILOSOPHY_MAP.md 準拠）

purpose:
  症例文章に BiBi の部位別思想（PHILOSOPHY）を必ず反映させ、
  思想の抜け・誤用・一般論化を防ぐ。

inputs:
  - INPUT_SCHEMA（症例入力）
  - PHILOSOPHY_MAP.md
  - 該当する PHILOSOPHY ファイル（例：botox/calf.md 等）

outputs:
  - philosophy_digest（抽出・構造化された要点）
  - generation_constraints（must/avoid の制約）
  - section_injection_plan（どのセクションに何を入れるか）

hard_rules:
  - 該当PHILOSOPHYは必ず参照する（未参照での生成は禁止）
  - MAPにない area は philosophy=NONE と扱い、一般論補完は禁止
  - “推測”で思想を補完しない（不足は TODO で返す）

---

## Step A-Philosophy：処理フロー

1) INPUT_SCHEMA から取得
   - treatment.area
   - treatment.type（例：botox / ha / artmake 等）
   - treatment.category（任意）

2) PHILOSOPHY_MAP.md を参照し、参照ファイルを一意決定
   - area -> file
   - file == NONE の場合：
       - philosophy_digest = {}
       - generation_constraints = { forbid_generic_fill: true }
       - 以降の生成では philosophy 由来の一般論挿入は禁止

3) file を全文読み込み（例：botox/calf.md）

4) 抽出（Digest）
   以下の A〜E を抽出し、構造化して保持する

   A. goal_definition（ゴール定義）
      - 何を目指すか（例：細さより後ろ姿、血色設計 等）
      - NGゴール（例：効かせすぎ、濃くする 等）が明記されていれば取得

   B. design_principles（設計原則）
      - 効かせすぎない
      - 日常動作を壊さない
      - 左右差前提
      - 初回控えめ -> 調整、など

   C. risk_and_avoid（リスク・避ける設計）
      - 効きすぎ時の困りごと
      - 避けるべき表現・設計
      - 禁忌/注意（妊娠/ヘルペス等、記載がある範囲のみ）

   D. kinetics（効果の出方）
      - 効果発現 / 最大 / 持続
      - “ゆっくり変化”などの時間軸

   E. indication_and_combo（適応/併用）
      - 適応外の判断軸
      - 併用提案の条件

5) 反映計画（Section Injection Plan）
   CASE_PAGE_SPEC の各セクション（例：仕上がりポイント / 工夫ポイント / Drコメント / 注意点）に
   どのDigest要素を入れるかを決める。

---

## 文章生成時の強制ルール

must_apply:
  - A（goal_definition）は必ず本文に反映
  - B（design_principles）は必ず本文に反映
  - D（kinetics）は誇張せず、記載がある範囲で反映

prohibitions:
  - philosophy と矛盾するゴール設定は禁止
  - file == NONE の場合、一般論・別部位思想の流用は禁止
  - 単位数・回数・持続を断定しない（記載があっても“目安＋個別設計”を優先）
  - philosophy に書かれていない効果/リスクを追加推測しない

---

## 反映チェック（自動/人レビュー）

checklist:
  - goal_definition が文中に現れているか
  - 「効かせすぎない」「自然」「日常動作」等の設計原則が消えていないか
  - 時間軸（効果が出るまで）が誇張されていないか
  - 適応外・併用の判断がねじれていないか

if_failed:
  - 再生成（差し戻し）
  - philosophy_digest を再抽出してから再生成
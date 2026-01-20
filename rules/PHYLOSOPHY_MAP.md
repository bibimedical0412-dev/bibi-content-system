# PHILOSOPHY_MAP.md
# 症例生成時に必ず参照する思想ファイルの対応表（実ファイル名準拠）
# 推測禁止：該当がない場合は philosophy: NONE とし、一般論補完は禁止。

version: 1.0
last_updated: 2026-01-20

base_dir_policy:
  - 本MAPの file は「PHILOSOPHYルートからの相対パス」を書く
  - 大小文字・ハイフン・アンダースコア・スペルは実ファイル名に完全一致させる
  - mapに存在しないareaは philosophyを適用しない（流用禁止）

rules:
  - area は INPUT_SCHEMA の treatment.area を唯一の参照元とする
  - area → file は必ず 1:1 で確定させる（複数候補禁止）
  - file が NONE の場合：
      - philosophy 適用なし
      - 一般論での補完は禁止
      - 該当箇所は TODO/保留で返す（推測しない）

map:

  ## =========================
  ## ARTMAKE（アートメイク）
  ## =========================
  eyebrow_artmake:
    file: artmake/eyeblow.md

  lip_artmake:
    file: artmake/lip.md


  ## =========================
  ## BOTOX（ボトックス）
  ## =========================
  # ※スクショのファイル名に完全一致
  upperarm_botox:
    file: botox/appeararm.md

  axillary_botox:
    file: botox/Axillary.md

  calf_botox:
    file: botox/calf.md

  facial_expression_botox:
    file: botox/FACIAL_EXPRESSION.md

  masseter_botox:
    file: botox/masseter.md

  mouth_design_botox:
    file: botox/mouth_design.md

  shoulder_botox:
    file: botox/shoulder.md

  thigh_botox:
    file: botox/Thigh.md


  ## =========================
  ## HA（ヒアルロン酸）
  ## =========================
  # ※スクショのファイル名に完全一致
  chin_jawline_ha:
    file: ha/chin_jawline.md

  forehead_ha:
    file: ha/FOREHEHEAD.md
    # ↑注意：スクショは「FOREHEAD.md」なので、実ファイル名に合わせてください
    # もし実際が FOREHEAD.md なら、上を FOREHEAD.md に直してください

  lips_ha:
    file: ha/LIPS.md

  midface_hollow_ha:
    file: ha/midface_hollow.md

  nasolabial_fold_ha:
    file: ha/nasolabial-fold.md

  neck_ha:
    file: ha/neck.md

  nose_ha:
    file: ha/NOSE.md

  tear_trough_ha:
    file: ha/TEAR_TROUGH.md

  temple_ha:
    file: ha/TEMPLE.md


  ## =========================
  ## 該当なし
  ## =========================
  none:
    file: NONE
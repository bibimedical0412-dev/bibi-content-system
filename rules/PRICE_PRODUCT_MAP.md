# PRICE_PRODUCT_MAP.md
# 入力（caseの treatment.products[].name）→ PRICE_SPEC の product_code への対応表

## Hyaluronic Acid（ヒアルロン酸）
# 価格帯A：ボリューマ/ボリフト/ボルベラ（同一価格）
- aliases: ["ボリューマ", "Voluma", "VOLUMA"]
  code: "HA_VOLUMA"

- aliases: ["ボリフト", "Volift", "VOLIFT"]
  code: "HA_VOLIFT"

- aliases: ["ボルベラ", "Volbella", "VOLBELLA"]
  code: "HA_VOLBELLA"

# 価格帯B：ボラックス
- aliases: ["ボラックス", "Volux", "VOLUX"]
  code: "HA_VOLUX"

# 価格帯C：ボライト
- aliases: ["ボライト", "Volite", "VOLITE", "ボライトXC", "ボライトXC"]
  code: "HA_VOLITE"

# 価格帯D：ウルトラプラス
- aliases: ["ウルトラプラス", "Ultra Plus", "ULTRA PLUS", "ウルトラプラスXC", "ウルトラプラスXC"]
  code: "HA_ULTRA_PLUS"

## Botox / Toxin（表情筋 50単位系）
- aliases: ["ボツラックス", "Botulax", "BOTULAX"]
  code: "BTX_BOTULAX_50"

- aliases: ["ボトックス", "BOTOX", "アラガン", "ボトックス(アラガン社製)"]
  code: "BTX_ALLERGAN_50"

## Options（オプション）
- aliases: ["カニューレ"]
  code: "OPT_CANNULA"

- aliases: ["麻酔"]
  code: "OPT_ANESTHESIA"
  
## ARTMAKE mapping（確定）

# eyebrow
- "アイブロウ 4D" -> ARTMAKE_BROW_4D
- "アイブロウ4D" -> ARTMAKE_BROW_4D
- "眉アートメイク 4D" -> ARTMAKE_BROW_4D
- "眉アートメイク4D" -> ARTMAKE_BROW_4D
- "4D（毛並み+パウダー）" -> ARTMAKE_BROW_4D
- "4D" -> ARTMAKE_BROW_4D  # ※area=brow のときのみ有効にする（prompt側制約）

- "アイブロウ 3D" -> ARTMAKE_BROW_3D
- "アイブロウ3D" -> ARTMAKE_BROW_3D
- "眉アートメイク 3D" -> ARTMAKE_BROW_3D
- "眉アートメイク3D" -> ARTMAKE_BROW_3D
- "3D" -> ARTMAKE_BROW_3D  # ※area=brow のときのみ

- "アイブロウ 2D" -> ARTMAKE_BROW_2D
- "アイブロウ2D" -> ARTMAKE_BROW_2D
- "眉アートメイク 2D" -> ARTMAKE_BROW_2D
- "眉アートメイク2D" -> ARTMAKE_BROW_2D
- "2D" -> ARTMAKE_BROW_2D  # ※area=brow のときのみ

# lip
- "リップ" -> ARTMAKE_LIP
- "リップアートメイク" -> ARTMAKE_LIP
- "lip" -> ARTMAKE_LIP
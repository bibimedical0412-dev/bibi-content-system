# PRICE_SPEC.md
**作成日**: 2025-11-26  
**更新日**: 2025-12-23  
**バージョン**: v2.4（②準拠）

---

## 0. このファイルの目的
症例ページ・CMS・Instagram等の自動生成において、価格の**特定・合算・表示**を一貫させるための正規仕様。
- 価格は必ず本ファイルの定義に基づき決定する
- 価格の推測は禁止
- 不確定の場合は価格行を出力しない（または「要確認」）

---

## 1. 料金表示ルール（最重要）

### 1-1. 症例ページ（Web）
- **必ず「モニター料金＋通常料金」を併記**する
- **表示するモニター料金は「全顔モニター料金」**を用いる  
  ※部分施術であっても、表示上は全顔モニター料金を適用する（②準拠）
- 表示例
  - `モニター価格：¥XX,XXX（税込）`
  - `通常価格：¥XX,XXX（税込）`

### 1-2. Instagram
- `¥XX,XXX〜` のような **from 表記は可**
- ただし **推測で最安値を作らない**
  - 製剤が確定できる場合：該当製剤の全顔モニター単価を from として可
  - 製剤が不明な場合：`要確認` または価格行なし

### 1-3. 単位表記
- **cc表記は禁止**（本文・料金行ともに）
- 使用可：**本数 / 単位（U）/ 回数**

---

## 2. 自動生成 優先順位ルール
1. 症例入力に `price.plan` がある → **それを最優先**
2. `price.plan` が無い場合：
   - `case.price.rule = "AUTO"` なら本ファイルで単価を確定し合算
3. 製剤名が曖昧／コード未確定：
   - 原則：価格行を出力しない（または「要確認」）
   - Instagram用途のみ、許容される場合：`「ヒアルロン酸1本 ¥XX,XXX〜」` にフォールバック  
     ※ただし **XX,XXX を確定できる場合のみ**

---

## 3. 自動価格計算（Step A-Price）

### 3-1. 入力前提（推奨データ構造）
- `case.price.rule`: "AUTO" | "MANUAL"
- `case.price.plan`: string（任意、最優先で表示）
- `case.price.category`: "全顔" | "部分"（あっても表示価格は全顔モニターへ寄せる）
- `treatment.products[]`:
  - `code`（product_code or set_code）
  - `qty`（本数・回数・セット数・単位）
- `treatment.options[]`:
  - `code`（OPT_CANNULA / OPT_ANESTHESIA 等）
  - `qty`（任意、通常は 1）

> 注意：入力にないオプションや本数を推測して加算してはいけない。

### 3-2. 計算ルール
1) `case.price.plan` が存在する  
   → 価格は計算せず、表示は `price.plan` をそのまま採用（最優先）

2) `case.price.rule = "AUTO"` の場合  
   - `treatment.products` の各 item を、下記の **価格マスタ**から単価特定
   - **monitor 単価は常に full_face_monitor を使用**
   - regular は `regular` を使用
   - `monitor_yen` = Σ(単価_monitor × qty)
   - `regular_yen` = Σ(単価_regular × qty)

3) オプション加算
   - `treatment.options` に入力がある場合のみ加算
   - `monitor_yen += option.price × qty`
   - `regular_yen += option.price × qty`
   - ※オプションは通常「同一価格」前提（モニター/通常で変動しない）

4) 不確定の場合
   - 単価を特定できない product / option が1つでも含まれる場合：
     - `monitor_yen` / `regular_yen` を空にする
     - 料金行は「非表示」または「要確認」

### 3-3. 表示用整形（推奨）
- `price_plan_label = "全顔モニター"`
- `price_monitor_yen` = 3桁カンマ + `¥` + `(税込)` 表記
- `price_regular_yen` = 同上

---

## 4. 価格マスタ（医師施術）

### 4-1. ヒアルロン酸（1本）
> 価格は **全顔モニター / 通常** のみを使用する（②準拠）

| product_code | name | unit_label | full_face_monitor | regular |
|---|---|---:|---:|---:|
| HA_ULTRA_PLUS | ウルトラプラス | 1本 | 26800 | 33500 |
| HA_VOLUMA | ボリューマ | 1本 | 44800 | 56000 |
| HA_VOLIFT | ボリフト | 1本 | 44800 | 56000 |
| HA_VOLBELLA | ボルベラ | 1本 | 44800 | 56000 |
| HA_VOLITE | ボライト | 1本 | 44800 | 62300 |
| HA_VOLUX | ボラックス | 1本 | 49800 | 62300 |

#### 3本セット
| set_code | description | unit_label | full_face_monitor | regular |
|---|---|---:|---:|---:|
| HA_3SET_STD | ボリューマ/ボリフト/ボルベラ 3本セット（1本あたり価格） | 1本 | 40400 | 50400 |
| HA_3SET_VOLUX | 上記＋ボラックス変更（1本あたり価格） | 1本 | 45400 | 56650 |

> 注意：セットは「1本あたり価格」で登録しているため、計算時は `qty = 本数` を基本とする。  
> 例）3本セットの表記で「3本」なら `HA_3SET_STD × 3` として合算する。

#### ヒアルロン酸 共通注意文（表示用）
- 1本1ccの購入を基本とし、少量使用でも1本分の料金となります
- 残量は破棄となります
- 1本分(1cc)を複数の部位に振り分けることは可能です

---

### 4-2. ヒアルロン酸 オプション
| option_code | name | unit_label | price |
|---|---|---:|---:|
| OPT_CANNULA | カニューレ | 1回 | 5500 |
| OPT_ANESTHESIA | 麻酔 | 1回 | 3300 |

---

### 4-3. ボツリヌストキシン（ボツラックス：韓国製）
#### 50単位プラン（3部位以上の表情筋に適用）
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| BTX_BOTULAX_50 | ボツラックス（50単位） | 50単位 | 14800 | 18500 |

#### 単位別（ボツラックス）
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| BTX_BOTULAX_50 | ボツラックス（50単位） | 50単位 | 14800 | 18500 |
| BTX_BOTULAX_100 | ボツラックス（100単位） | 100単位 | 17800 | 22300 |
| BTX_BOTULAX_200 | ボツラックス（200単位） | 200単位 | 26800 | 37300 |
| BTX_BOTULAX_300 | ボツラックス（300単位） | 300単位 | 36800 | 49800 |
| BTX_BOTULAX_400 | ボツラックス（400単位） | 400単位 | 46800 | 62300 |
| BTX_BOTULAX_500 | ボツラックス（500単位） | 500単位 | 56800 | 74800 |
| BTX_BOTULAX_600 | ボツラックス（600単位） | 600単位 | 66800 | 87300 |
| BTX_BOTULAX_700 | ボツラックス（700単位） | 700単位 | 76800 | 99800 |

---

### 4-4. ボツリヌストキシン（ボトックス：アラガン社製）
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| BTX_ALLERGAN_50 | ボトックス（50単位） | 50単位 | 31700 | 39800 |
| BTX_ALLERGAN_100 | ボトックス（100単位） | 100単位 | 63400 | 79800 |
| BTX_ALLERGAN_200 | ボトックス（200単位） | 200単位 | 126800 | 158500 |

#### アラガン：表情筋1部位（必要時のみ）
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| BTX_ALLERGAN_1PART | ボトックス（表情筋1部位） | 1部位 | 13200 | 16500 |

---

### 4-5. 特殊施術（ボトックス）
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| BTX_MICRO_OR_NECK_50 | マイクロボトックス or ネックボトックス | 50単位 | 44000 |  |

> regular が未定義の場合は空欄とし、症例ページでは「要確認」または価格行を出力しない。

---

### 4-6. 脂肪溶解注射
| product_code | name | unit_label | monitor | regular |
|---|---|---:|---:|---:|
| LIPO_FATX_5 | Fat X Core | 5cc | 22000 | 27500 |
| LIPO_FATX_10 | Fat X Core | 10cc | 33000 | 41500 |
| LIPO_FATX_20 | Fat X Core | 20cc | 60000 | 75000 |
| LIPO_CABELLIN_10 | カベリン | 10cc | 19800 | 25000 |
| LIPO_CABELLIN_20 | カベリン | 20cc | 36000 | 45000 |

> 注意：本文では cc 表記禁止だが、施術名としての「10cc」などはマスタの unit_label として保持可。  
> 料金表示行では「施術名 + 料金」で出す（本文での量説明は避ける）。

---

## 5. 価格マスタ（看護師施術：アートメイク）
> ②準拠：**部分モニターも全顔モニター料金を適用**（表示上）

| product_code | display_name | unit_label | full_face_monitor | regular |
|---|---|---:|---:|---:|
| ARTMAKE_BROW_4D | アイブロウ 4D | 1回 | 33000 | 41000 |
| ARTMAKE_BROW_3D | アイブロウ 3D | 1回 | 28000 | 35000 |
| ARTMAKE_BROW_2D | アイブロウ 2D | 1回 | 28000 | 35000 |
| ARTMAKE_LIP | リップ | 1回 | 28000 | 35000 |

#### アートメイク 注意文（表示用）
- 2回目は1〜2ヶ月後を推奨（個人差あり）
- モニター条件：Before/After写真の撮影・使用許可、HP・Instagram・広告での使用許可

---

## 6. 免責文（固定・削除禁止）
＊本ページ記載のモニター制度・料金は投稿時点の内容です。
今後、内容が変更・終了となる場合があります。

---

## 7. NG事項（自動生成の禁止行為）
- 価格の推測（最安値生成・相場当て・未入力オプション加算）
- 製剤の推測（名前が曖昧な場合に勝手にコード割当）
- cc表記（本文・料金表示行）
- regular 未定義のメニューを通常価格として出力すること

---

## 8. フォールバック方針
- 製剤/コードが確定できない：
  - **症例ページ**：価格行を出さない（または「要確認」）
  - **Instagram**：確定できる場合のみ `¥XX,XXX〜`。確定できない場合は出さない

---

## 9. Product Codes（運用で使用）
### Hyaluronic Acid
HA_ULTRA_PLUS
HA_VOLUMA
HA_VOLIFT
HA_VOLBELLA
HA_VOLUX
HA_VOLITE
HA_3SET_STD
HA_3SET_VOLUX

### Options
OPT_CANNULA
OPT_ANESTHESIA

### Botulinum (Botulax)
BTX_BOTULAX_50
BTX_BOTULAX_100
BTX_BOTULAX_200
BTX_BOTULAX_300
BTX_BOTULAX_400
BTX_BOTULAX_500
BTX_BOTULAX_600
BTX_BOTULAX_700

### Botulinum (Allergan)
BTX_ALLERGAN_1PART
BTX_ALLERGAN_50
BTX_ALLERGAN_100
BTX_ALLERGAN_200

### Special
BTX_MICRO_OR_NECK_50

### Lipolysis
LIPO_FATX_5
LIPO_FATX_10
LIPO_FATX_20
LIPO_CABELLIN_10
LIPO_CABELLIN_20

### Artmake
ARTMAKE_BROW_4D
ARTMAKE_BROW_3D
ARTMAKE_BROW_2D
ARTMAKE_LIP
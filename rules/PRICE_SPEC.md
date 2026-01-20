⸻

1. 価格表示の基本原則（最重要）


表示ルール
	•	症例ページでは 必ずモニター料金＋通常料金を併記
	•	Instagramでは 「¥XX,XXX〜」表記可
	•	cc表記は禁止（本数・単位のみ可）

⸻

2. ヒアルロン酸（医師施術）

製剤別 価格テーブル（1本＝1cc）

product_code	name	full_face_monitor	partial_monitor	regular
HA_ULTRA_PLUS	ウルトラプラス	¥26,800	¥30,200	¥33,500
HA_VOLUX	ボラックス	¥49,800	¥56,100	¥62,300
HA_VOLUMA	ボリューマ	¥44,800	¥50,400	¥56,000
HA_VOLIFT	ボリフト	¥44,800	¥50,400	¥56,000
HA_VOLBELLA	ボルベラ	¥44,800	¥50,400	¥56,000
HA_VOLITE	ボライト	¥44,800	¥56,100	¥62,300

セット価格（3本）

set_code	description	full_face_monitor	partial_monitor	regular
HA_3SET_STD	ボリューマ/ボリフト/ボルベラ	¥40,400	¥45,400	¥50,400
HA_3SET_VOLUX	上記＋ボラックス1本	¥45,400	¥51,000	¥56,650

共通注意事項（必ず表示）

・1cc未満でも1本分の料金
・1本を複数部位へ分配可能

オプション

option	price
カニューレ	¥5,500
麻酔	¥3,300


⸻

3. ボツリヌストキシン（医師施術）

表情筋（通常）

product	unit	full_face_monitor	partial_monitor	regular
ボツラックス	50単位	¥24,200	¥27,300	¥30,300
ボトックス(アラガン)	50単位	¥31,700	¥35,800	¥39,800

ボツラックス キャンペーン

unit	monitor	regular
100	¥16,500	¥22,300
200	¥21,800	¥37,300
300	¥29,800	¥49,800
400	¥39,800	¥62,300
500	¥49,800	¥74,800
600	¥59,800	¥87,300
700	¥69,800	¥99,800

特殊
	•	マイクロボトックス / ネックボトックス 50単位
→ ¥44,000（モニター）

⸻

4. その他 医師施術（要参照）

脂肪溶解注射

product	volume	monitor	regular
Fat X Core	5cc	¥22,000	¥27,500
Fat X Core	10cc	¥33,000	¥41,500
Fat X Core	20cc	¥60,000	¥75,000
カベリン	10cc	¥19,800	¥25,000
カベリン	20cc	¥36,000	¥45,000


⸻

5. 看護師施術（アートメイク）

### ARTMAKE_BROW_4D
- display_name: "アイブロウ 4D"
- unit_label: "1回"
- pricing:
  - monitor_type: "全顔"
    monitor_price: 33000
    regular_price: 41000
  - monitor_type: "部分"
    monitor_price: 38000
    regular_price: 41000
- notes:
  - "2回目は1〜2ヶ月後を推奨（個人差あり）"
  - "モニター条件：Before/After写真の撮影・使用許可、HP・Instagram・広告での使用許可"
  - "顔出しNG、部分のみOKなど条件により料金変動あり"

### ARTMAKE_BROW_3D
- display_name: "アイブロウ 3D"
- unit_label: "1回"
- pricing:
  - monitor_type: "全顔"
    monitor_price: 28000
    regular_price: 35000
  - monitor_type: "部分"
    monitor_price: 32000
    regular_price: 35000
- notes:
  - "2回目は1〜2ヶ月後を推奨（個人差あり）"
  - "モニター条件：Before/After写真の撮影・使用許可、HP・Instagram・広告での使用許可"
  - "顔出しNG、部分のみOKなど条件により料金変動あり"

### ARTMAKE_BROW_2D
- display_name: "アイブロウ 2D"
- unit_label: "1回"
- pricing:
  - monitor_type: "全顔"
    monitor_price: 28000
    regular_price: 35000
  - monitor_type: "部分"
    monitor_price: 32000
    regular_price: 35000
- notes:
  - "2回目は1〜2ヶ月後を推奨（個人差あり）"
  - "モニター条件：Before/After写真の撮影・使用許可、HP・Instagram・広告での使用許可"
  - "顔出しNG、部分のみOKなど条件により料金変動あり"

### ARTMAKE_LIP
- display_name: "リップ"
- unit_label: "1回"
- pricing:
  - monitor_type: "全顔"
    monitor_price: 28000
    regular_price: 35000
  - monitor_type: "部分"
    monitor_price: 32000
    regular_price: 35000
- notes:
  - "2回目は1〜2ヶ月後を推奨（個人差あり）"
  - "モニター条件：Before/After写真の撮影・使用許可、HP・Instagram・広告での使用許可"
  - "顔出しNG、部分のみOKなど条件により料金変動あり"
⸻

6. モニター免責文（固定・削除禁止）

＊本ページ記載のモニター制度・料金は投稿時点の内容です。
今後、内容が変更・終了となる場合があります。


⸻

7. 自動生成時の優先順位ルール
	1.	症例入力に「price.plan」がある → それを最優先
	2.	なければ
	•	部位数から 全顔 / 部分 を自動判定
	3.	製剤名が曖昧な場合
	•	「ヒアルロン酸1本 ¥XX,XXX〜」表記にフォールバック
	4.	価格の推測は禁止
	
### Step A-Price：価格を確定する（PRICE_SPEC参照）
1) case.price.rule が "AUTO" の場合：
   - PRICE_SPEC.md を参照し、treatment.products の製剤名から単価を特定する
   - case.price.category が "全顔" なら full_face_monitor を使う
   - case.price.category が "部分" なら partial_monitor を使う
   - 通常料金は regular を使う
2) 複数本・複数製剤がある場合：
   - 各製剤の（該当カテゴリの）モニター単価を合算して monitor_yen を作る
   - 各製剤の通常単価を合算して regular_yen を作る
3) オプション（カニューレ・麻酔）が入力にある場合のみ加算する（推測禁止）
4) 価格が確定できない場合：
   - price.plan / monitor_yen / regular_yen は空にして、テンプレ上の価格行を出力しない（または「要確認」表記にする）
5) 表示用整形：
   - price_plan_label = "{category}モニター"
   - price_monitor_yen = 3桁カンマ整形
   - price_regular_yen = 3桁カンマ整形
   

## Product codes (for automation)
HA_ULTRA_PLUS
HA_VOLUMA
HA_VOLIFT
HA_VOLBELLA
HA_VOLUX
HA_VOLITE
OPT_CANNULA
OPT_ANESTHESIA
BTX_BOTULAX_50
BTX_ALLERGAN_50 
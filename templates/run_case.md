# 実行テンプレ（run_case.md）
目的：1症例を「毎回同じ手順・同じ品質」で生成する

---

## ✅ 実行手順（人間がやること）

1. `contents/cases/{症例ページスラッグ}/input.md` を開く
2. その中身をこのチャットに貼る（input全文）
3. 次に `templates/case_generate.md` の全文を貼る
4. そのまま生成させる（追加の質問が来ても、原則は input の追記のみ）

---

## ✅ チャットへ貼る順番（固定）

### ① 入力（この症例の材料）
【ここに `contents/cases/{slug}/input.md` を全文貼る】

### ② 命令書（生成の型）
【ここに `templates/case_generate.md` を全文貼る】

---

## ✅ 出力の保存先（Git上の置き場所）

生成が終わったら以下に貼り戻して保存する：

- WordPress：`contents/cases/{slug}/outputs/wp.html`
- note：`contents/cases/{slug}/outputs/note.md`
- アメブロ：`contents/cases/{slug}/outputs/ameblo.html`

（必要なら）
- インスタ：`contents/cases/{slug}/outputs/instagram.txt`

---

## ✅ 命名規則（推奨）

- slug は「完成スラッグ（URLパス）」の末尾に合わせる
  例：`10s-chin-eline`

- フォルダ構造（1症例 = 1フォルダ）
  contents/cases/10s-chin-eline/
    ├─ input.md
    └─ outputs/
        ├─ wp.html
        ├─ note.md
        └─ ameblo.html

---

## ✅ 注意
- input.md は「事実（入力）」だけ。文章の完成をここでやらない
- 出力が崩れたときは、まず `case_generate.md` を直す（入力をいじらない）
- 価格・注意文などの固定表記は rules 側のルールを優先
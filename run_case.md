# run_case.md
# 症例生成 実行手順書（MVP版）

このファイルは  
**「1症例を input → 生成 → 保存 → push まで回すための人間用手順書」**です。

⚠️ **AIには読ませません**  
⚠️ **作業者（miki）が毎回この順番で実行します**

---

## 🎯 ゴール
- 1症例 = 1フォルダ
- 同じ手順で何度でも再現できる
- **最低限「回る」ことを最優先**（完成度は後回し）

---

## 📁 フォルダ構成（前提）

contents/
└─ cases/
└─ {case-slug}/
├─ input.md
└─ outputs/

### 例

contents/cases/10s-chin-eline/
├─ input.md
└─ outputs/

---

## ① 症例フォルダを作る

場所：

contents/cases/

フォルダ名：

完成スラッグと同じ名前
例：10s-chin-eline

---

## ② input.md を作る

場所：

contents/cases/{case-slug}/

ファイル名：

input.md

中身：
- `templates/case_input.md` を **全文コピー**
- 最初は以下だけ埋まっていればOK
  - A. 管理情報（部位・年代・性別・症例タイトル・主な悩み・モニタープラン）
  - C. カルテ原文（そのまま貼る）

※ 他は空欄でも可  
※ **まずは「回す」ことが最優先**

---

## ③ ChatGPTで症例生成を実行

1. ChatGPTを開く
2. 以下を順番に渡す

### ① ルール宣言
- rules 配下の該当ルール
- templates の生成テンプレ
（※ これは後で整理。MVPでは最低限でOK）

### ② input.md の中身をそのまま貼る

---

## ④ 生成結果を保存する

保存場所：

contents/cases/{case-slug}/outputs/

保存ファイル例：

case_wordpress.html
case_note.md
case_ameblo.html
case_instagram.txt

※ ファイル名は厳密でなくてOK  
※ 後で命名ルールを固める

---

## ⑤ commit → push

- 変更内容を commit
- main ブランチに push

🎉 **これで1症例完了**

---

## ✅ チェックリスト（毎回）

- [ ] cases/{case-slug}/ フォルダがある
- [ ] input.md がある
- [ ] outputs/ に生成物が入っている
- [ ] push されている

---
## Done定義（今回の勝利条件）
- WordPressに「下書き」が1件存在する
- 下書きURLをブラウザで確認できる

※ この run_case.md は  
「迷ったらここに戻る」ための **作業者用アンカー**。


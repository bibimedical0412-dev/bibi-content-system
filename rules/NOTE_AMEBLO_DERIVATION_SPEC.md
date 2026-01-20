# NOTE_AMBLO_DERIVATION_SPEC.md
# note / アメブロ 派生生成 仕様書
# WP症例ページからの「流用」ではなく、同一思想を通した別媒体生成を行う

version: 1.0
last_updated: 2026-01-20

purpose:
  note / アメブロ記事においても、
  BiBiクリニックの PHILOSOPHY（部位別思想）を破壊せずに反映する。
  文章量を減らしても、思想・ゴール・注意点は必ず残す。

basic_principle:
  - WP症例は「マスター」だが、コピペ元にはしない
  - 派生生成も Step A-Philosophy を必ず通す
  - 要約はするが、思想の削除は禁止

---

## 派生生成フロー（全体）

1. INPUT_SCHEMA を読み込む
2. Step A-Philosophy を実行
   - PHILOSOPHY_MAP.md 参照
   - 該当 PHILOSOPHY を読み込み
   - philosophy_digest を生成
3. CASE_PAGE_SPEC に基づき
   - WP用フル症例文章を「生成」する（※省略しない）
4. WP文章を直接使わず、
   philosophy_digest + 症例要点から
   note / アメブロ用文章を再構築する

※ WP生成をスキップして直接派生させてもよいが、
   思想抽出（Step A-Philosophy）は必須

---

## note / アメブロ共通の必須反映要素

以下は **必ず含める（短くてもOK）**

must_include:
  - philosophy.goal_definition
  - philosophy.design_principles（最低1つ）
  - philosophy.kinetics（効果の出方・時間軸）
  - 「当院の考え方」「当院では〜」と分かる一文

must_not:
  - 一般論だけの記事
  - 施術のメリットだけを並べる構成
  - philosophy と矛盾するゴール設定
  - 単位数・回数の断定

---

## 媒体別の構成ルール

### ◆ note 用構成（推奨）

sections:
  1. 導入（共感・悩み）
  2. 施術の考え方（PHILOSOPHY要約）
  3. なぜ当院ではこの設計をするのか
  4. 効果の出方・注意点
  5. まとめ（当院らしさ）

rules:
  - 見出し数は 4〜6 に抑える
  - 医療広告的に煽らない
  - 思想説明を1ブロック必ず入れる

### ◆ アメブロ 用構成（推奨）

sections:
  1. 導入（短め・日常トーン）
  2. 施術のポイント（PHILOSOPHY簡略）
  3. 注意点・誤解されやすい点
  4. 締め（安心感）

rules:
  - note よりさらに短く
  - 専門用語は減らすが、思想は消さない
  - 「当院では〜」を必ず入れる

---

## PHILOSOPHY反映の具体例（ふくらはぎ）

example:
  philosophy.goal_definition:
    "細さではなく後ろ姿の美しさを重視"

  note_reflection:
    "当院では、単に脚を細くするのではなく、
     後ろ姿が軽やかに見えるライン作りを大切にしています。"

  ameblo_reflection:
    "ふくらはぎは、細さよりも
     後ろ姿のバランスがとても大切な部位です。"

---

## 禁止事項（派生時）

- WP本文の単純要約
- PHILOSOPHYを読まずに生成
- 「一般的には〜」で逃げる構成
- 他部位思想の流用

---

## 品質チェック（最低限）

checklist:
  - 当院独自の考え方が1文以上あるか
  - 効果時期が誇張されていないか
  - 読者に誤解を与える断定表現がないか
  - WPと思想的に矛盾していないか

fail_action:
  - 再生成
  - philosophy_digest 再抽出
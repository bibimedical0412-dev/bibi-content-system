---
id: design_dna_bibi_hp
version: 2.0
last_updated: 2025-12-09
scope:
  - wordpress_pages
  - case_pages
  - service_pages
  - columns
rules:
  - no_global_css
  - bem_with_bibi_prefix
  - no_tag_selector
  - component_scoped_js
---

# 08. デザインDNA - BiBiクリニックHP統一規格

**最終更新**: 2025年12月9日  
**バージョン**: v2.0  
**目的**: 全ページで統一されたビジュアルアイデンティティを維持し、プロフェッショナルで信頼性の高い印象を構築する

---

## 📋 目次

1. [カラーパレット](#カラーパレット)
2. [タイポグラフィ](#タイポグラフィ)
3. [HTML/CSS/JavaScript実装ルール](#htmlcssjavascript実装ルール)
4. [レイアウト原則](#レイアウト原則)
5. [画像ガイドライン](#画像ガイドライン)
6. [アイコン・グラフィック要素](#アイコングラフィック要素)
7. [レスポンシブデザイン](#レスポンシブデザイン)

---

## 🎨 カラーパレット

BiBiクリニックのWEBサイトで使用されている色を「色コード → 用途」形式でまとめました。
色を変えたい場合は、このガイド内の近い色から選ぶことで、サイト全体の統一感を維持できます。

### メインカラー - アクション・強調系

#### #615d69
```
用途:
• 「Read more」等ページ進むボタン
• 「一覧に戻る」等ページ戻るボタン  
• 「ご予約はこちら」等ボタン
役割: 主要なアクションボタンの背景色
```

#### #745e9d
```
用途:
• コラム記事カードのNEWバッジ背景
• ページ下部CTAボタンホバー（マウスオーバー時）
• 操作中の状態表現
役割: 強調表示用のディープパープル。サイト内で"新着・注目"を示す色
```

#### #a49ab6
```
用途:
• ページ下部CTAボタン
• リンク色・アクション可能色
• h3見出しのリードマーク（▪️）などのアクセントカラー
役割: セカンダリアクション・インタラクティブ要素
```

### アクセントカラー - グラフィック要素系

#### #8f83a5
```
用途:
• h2見出しの下ライン（左側の濃い色）
• グラフィカルな要素として使用するアクセントカラー
役割: 見出し装飾・グラデーション用の濃色
```

#### #bab3c6
```
用途:
• 診察フローの番号ラベル
• 検索用タグのボタンホバー（マウスオーバー時）
• タブ表現などのアクセントカラー
役割: UI要素の状態変化表現
```

#### #d2ced9
```
用途:
• h2見出しの下ライン（右側の薄い色）
• 本文用罫線
• 料金表の項目ヘッダー行
• 記事用タグの背景色
役割: 区切り線・背景色（薄）
```

### ニュートラルカラー

#### #ffffff（白）
```
用途:
• 濃色背景時の文字色（ボタン文字、バッジ文字など）
• 料金表・各項目等の背景色
役割: 基本背景色・反転時の文字色
```

#### #f5f6f9（オフホワイト）
```
用途:
• 全てのページで共通に使用している背景色
役割: ページ全体の基本背景色
```

#### #cfcfcf（グレー）
```
用途:
• 料金表用罫線
役割: 表組みの区切り線
```

### テキストカラー

#### #545454（ダークグレー）
```
用途:
• 本文文字色
• h1見出し文字色
• h2見出し文字色
• キャプションなど文字色
役割: メインテキストカラー
```

#### #81749A（ミディアムパープル）
```
用途:
• h3見出し文字色
• h4見出し文字色
役割: サブ見出し用テキストカラー
```

### カラー使用原則

- **統一性**: 全ページで同じカラーコードを使用
- **視認性**: テキストと背景のコントラスト比は4.5:1以上を維持（WCAG 2.1 AA基準）
- **薬機法対応**: 効果を過度に強調する色使いは避ける
- **年齢層配慮**: 40代女性が落ち着きと信頼を感じる配色

---

## 📝 タイポグラフィ

### フォントファミリー

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", 
             "Noto Sans JP", "Hiragino Kaku Gothic ProN", 
             "Yu Gothic", Meiryo, sans-serif;
```

### フォントサイズ階層

```
H1: 32px / 2rem (ページメインタイトル)
H2: 28px / 1.75rem (セクション見出し)
H3: 24px / 1.5rem (サブセクション見出し)
H4: 20px / 1.25rem (小見出し)
H5: 18px / 1.125rem (リスト内見出し)
H6: 16px / 1rem (補足見出し)

本文: 16px / 1rem (基本テキスト)
小文字: 14px / 0.875rem (キャプション、注釈)
極小文字: 12px / 0.75rem (免責事項、法的表記)
```

### 行間・文字間

```css
/* 本文 */
line-height: 1.8;
letter-spacing: 0.05em;

/* 見出し */
line-height: 1.4;
letter-spacing: 0.02em;
```

### フォントウェイト

```
見出し: 700 (Bold)
強調: 600 (Semi-Bold)
本文: 400 (Regular)
軽量テキスト: 300 (Light)
```

### 見出しスタイリング

#### H2見出し
```css
/* 見出しテキスト */
color: #545454;
font-size: 28px;
font-weight: 700;

/* 下線装飾 */
/* グラデーション: #8f83a5（左）→ #d2ced9（右） */
border-bottom: 2px solid;
border-image: linear-gradient(to right, #8f83a5, #d2ced9) 1;
```

#### H3見出し
```css
color: #81749A;
font-size: 24px;
font-weight: 700;

/* リードマーク装飾（オプション） */
/* ▪️ マークを #a49ab6 で表示 */
```

#### H4見出し
```css
color: #81749A;
font-size: 20px;
font-weight: 700;
```

### タイポグラフィ原則

- **可読性優先**: 40代女性が読みやすい16px以上を基本
- **適切な行間**: 1.8以上で目の疲れを軽減
- **階層の明確化**: H1→H6の順序を守り、飛ばさない
- **強調の節度**: 太字・色付きは本当に重要な箇所のみ

---

## 🔧 HTML/CSS/JavaScript実装ルール

### 重要原則

**すべてのコードは固有のクラス名を使用し、グローバルスコープへの影響を完全に防ぐこと。**

### 1. HTML について

#### ✅ DO（必須事項）

```html
<!-- すべての主要タグに固有のクラス名を付与 -->
<section class="bibi-case-study">
  <div class="bibi-case-study__inner">
    <h2 class="bibi-case-study__title">症例紹介</h2>
    <div class="bibi-case-study__content">
      <p class="bibi-case-study__text">テキスト内容</p>
    </div>
  </div>
</section>
```

#### ❌ DON'T（禁止事項）

```html
<!-- 汎用的すぎるクラス名 -->
<section class="section">
  <div class="inner">
    <div class="wrap">
      <button class="btn">ボタン</button>
    </div>
  </div>
</section>
```

#### クラス命名規則

- **BEM記法推奨**: `block__element--modifier`
- **プレフィックス使用**: `bibi-` を推奨（例: `bibi-header`, `bibi-nav`）
- **意味のある名前**: 用途が明確な命名（`custom-section` ではなく `bibi-price-table`）

```html
<!-- 良い例 -->
<div class="bibi-price-table">
  <div class="bibi-price-table__header">
    <h3 class="bibi-price-table__title">料金表</h3>
  </div>
  <ul class="bibi-price-table__list">
    <li class="bibi-price-table__item">
      <span class="bibi-price-table__name">施術名</span>
      <span class="bibi-price-table__price">¥00,000</span>
    </li>
  </ul>
</div>
```

### 2. CSS について

#### ✅ DO（必須事項）

```css
/* 固有クラス内でスコープを限定 */
.bibi-case-study a {
  color: #a49ab6;
  text-decoration: none;
}

.bibi-case-study a:hover {
  color: #745e9d;
}

.bibi-case-study p {
  color: #545454;
  line-height: 1.8;
  margin-bottom: 16px;
}

.bibi-case-study ul {
  list-style: none;
  padding-left: 0;
}
```

#### ❌ DON'T（禁止事項）

```css
/* タグ単体への直接スタイル指定 - 絶対禁止 */
a {
  color: #a49ab6;
}

p {
  line-height: 1.8;
}

/* グローバルセレクタの使用 - 絶対禁止 */
* {
  box-sizing: border-box;
}

body {
  font-family: sans-serif;
}

html {
  font-size: 16px;
}
```

#### セレクタ使用ルール

```css
/* ✅ 正しい: 固有クラス + タグでスコープ限定 */
.bibi-article h2 {
  color: #545454;
  border-bottom: 2px solid;
  border-image: linear-gradient(to right, #8f83a5, #d2ced9) 1;
}

.bibi-article h3 {
  color: #81749A;
}

/* ✅ 正しい: 固有クラスのみ */
.bibi-article__button {
  background-color: #615d69;
  color: #ffffff;
}

/* ❌ 間違い: タグ単体 */
button {
  background-color: #615d69;
}
```

#### レイアウト系プロパティの制限

```css
/* ✅ 正しい: 固有クラス内でのみ使用 */
.bibi-container {
  display: flex;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.bibi-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

/* ❌ 間違い: グローバルに影響 */
div {
  display: block;
}

section {
  margin: 40px 0;
}
```

### 3. JavaScript について

#### ✅ DO（必須事項）

```javascript
// 固有クラスを起点に要素を取得
const caseStudySection = document.querySelector('.bibi-case-study');
const buttons = caseStudySection.querySelectorAll('.bibi-case-study__button');

buttons.forEach(button => {
  button.addEventListener('click', function() {
    // 処理内容
  });
});

// または、コンテナ内のみで操作
document.querySelectorAll('.bibi-case-study').forEach(section => {
  const toggleBtn = section.querySelector('.bibi-case-study__toggle');
  const content = section.querySelector('.bibi-case-study__content');
  
  toggleBtn.addEventListener('click', () => {
    content.classList.toggle('bibi-case-study__content--open');
  });
});
```

#### ❌ DON'T（禁止事項）

```javascript
// 汎用クラス名や既存クラス名を前提とした処理
const buttons = document.querySelectorAll('.btn'); // NG
const sections = document.querySelectorAll('section'); // NG

// グローバルな要素への直接アクセス
document.body.style.overflow = 'hidden'; // NG
```

### 4. スタイルの完全カプセル化

#### コンポーネント単位での完結

```html
<!-- HTML -->
<div class="bibi-cta-banner">
  <div class="bibi-cta-banner__inner">
    <h2 class="bibi-cta-banner__title">ご予約はこちら</h2>
    <p class="bibi-cta-banner__text">お気軽にお問い合わせください</p>
    <a href="/contact" class="bibi-cta-banner__button">予約する</a>
  </div>
</div>
```

```css
/* CSS - このコンポーネント専用のスタイル */
.bibi-cta-banner {
  background-color: #f5f6f9;
  padding: 60px 20px;
  text-align: center;
}

.bibi-cta-banner__inner {
  max-width: 800px;
  margin: 0 auto;
}

.bibi-cta-banner__title {
  color: #545454;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 16px;
}

.bibi-cta-banner__text {
  color: #545454;
  font-size: 16px;
  line-height: 1.8;
  margin-bottom: 32px;
}

.bibi-cta-banner__button {
  display: inline-block;
  background-color: #a49ab6;
  color: #ffffff;
  padding: 16px 48px;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.bibi-cta-banner__button:hover {
  background-color: #745e9d;
}
```

### 5. 実装チェックリスト

新規コンポーネント作成時、以下を確認：

- [ ] すべての主要タグに固有クラス名が付与されているか
- [ ] タグ単体（a, p, ul等）への直接スタイル指定をしていないか
- [ ] グローバルセレクタ（*, body, html）を使用していないか
- [ ] レイアウト系プロパティが固有クラス内に限定されているか
- [ ] JavaScriptが固有クラスを起点に要素を取得しているか
- [ ] 他のページ・コンポーネントに影響を与えないか

---

## 📐 レイアウト原則

### グリッドシステム

```
最大コンテンツ幅: 1200px
左右パディング: 20px (モバイル) / 40px (タブレット以上)
セクション間マージン: 80px (PC) / 60px (タブレット) / 40px (モバイル)
```

### スペーシングスケール

```
xs: 8px   (アイコンとテキストの間隔)
sm: 16px  (段落間、リスト項目間)
md: 24px  (サブセクション間)
lg: 40px  (セクション内の大きな区切り)
xl: 60px  (メジャーセクション間)
xxl: 80px (ページセクション間)
```

### カードデザイン

```css
.bibi-card {
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 24px;
  background: #ffffff;
}
```

### ボタンデザイン

#### プライマリボタン

```css
.bibi-button--primary {
  background-color: #615d69;
  color: #ffffff;
  padding: 12px 32px;
  border-radius: 4px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.bibi-button--primary:hover {
  background-color: #745e9d;
  box-shadow: 0 4px 12px rgba(97, 93, 105, 0.3);
}
```

#### セカンダリボタン

```css
.bibi-button--secondary {
  background-color: #a49ab6;
  color: #ffffff;
  padding: 12px 32px;
  border-radius: 4px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.bibi-button--secondary:hover {
  background-color: #745e9d;
}
```

#### アウトラインボタン

```css
.bibi-button--outline {
  background-color: transparent;
  color: #615d69;
  border: 2px solid #615d69;
  padding: 10px 30px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.bibi-button--outline:hover {
  background-color: #615d69;
  color: #ffffff;
}
```

### レイアウト原則

1. **F字型視線導線**: 重要情報は左上から右下へ配置
2. **ホワイトスペース**: 詰め込みすぎず、余白を十分に確保
3. **視覚階層**: サイズ・色・配置で重要度を明確化
4. **一貫性**: 同じ種類の要素は同じスタイルを適用

---

## 📷 画像ガイドライン

### 症例写真

```
推奨サイズ: 800x600px以上
アスペクト比: 4:3 または 3:4
フォーマット: JPEG (品質85-90) / WebP推奨
ファイルサイズ: 200KB以下
```

#### 写真要件

- **解像度**: 鮮明で顔のディテールが分かる
- **照明**: 均一で影が少ない
- **角度**: 正面・左右45度・真横の統一
- **プライバシー**: 目線モザイク処理（薄く、顔の印象を損なわない）
- **色調**: 自然な肌色、過度な加工なし

### サムネイル画像

```
サイズ: 400x300px
フォーマット: JPEG / WebP
ファイルサイズ: 50KB以下
```

### アイキャッチ画像

```
サイズ: 1200x630px (OGP推奨サイズ)
用途: SNSシェア、一覧ページ
```

### 画像最適化

```html
<!-- 遅延読み込み -->
<img src="image.jpg" loading="lazy" alt="顎ヒアルロン酸（ボラックス2本）施術前の左45度写真">

<!-- レスポンシブ画像 -->
<img 
  src="image-800.jpg" 
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="説明文"
  loading="lazy">
```

---

## 🎯 アイコン・グラフィック要素

### アイコンセット

推奨ライブラリ: Font Awesome 6.x / Material Icons

```
チェックマーク: ✓ (成功、メリット)
注意マーク: ⚠ (注意事項)
情報マーク: ℹ (補足情報)
電話: ☎ (連絡先)
時計: 🕐 (営業時間、施術時間)
星: ★ (評価、ポイント)
```

### グラフィック要素

#### 区切り線

```css
.bibi-divider {
  border-top: 1px solid #d2ced9;
  margin: 40px 0;
}
```

#### 引用ボックス

```css
.bibi-quote {
  border-left: 4px solid #8f83a5;
  background-color: #f5f6f9;
  padding: 16px 20px;
  margin: 24px 0;
}

.bibi-quote p {
  color: #545454;
  font-size: 16px;
  line-height: 1.8;
  margin: 0;
}
```

#### 情報ボックス

```css
.bibi-info-box {
  background-color: #f5f6f9;
  border: 1px solid #d2ced9;
  border-radius: 8px;
  padding: 20px;
  margin: 24px 0;
}

.bibi-info-box__title {
  color: #81749A;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
}

.bibi-info-box__content {
  color: #545454;
  font-size: 16px;
  line-height: 1.8;
}
```

### 装飾原則

- **シンプル**: 過度な装飾は避け、情報を優先
- **統一性**: 同じアイコンは同じ意味で使用
- **視認性**: アイコンサイズは16px以上

---

## 📱 レスポンシブデザイン

### ブレークポイント

```css
/* モバイル（デフォルト） */
/* 〜767px */

/* タブレット */
@media (min-width: 768px) { 
  /* タブレット用スタイル */
}

/* デスクトップ */
@media (min-width: 1024px) { 
  /* デスクトップ用スタイル */
}

/* 大型ディスプレイ */
@media (min-width: 1440px) { 
  /* 大型ディスプレイ用スタイル */
}
```

### モバイルファースト原則

1. **タップ領域**: ボタンは最低44x44px
2. **読みやすさ**: フォントサイズは16px以上
3. **スクロール**: 縦スクロールを基本、横スクロールは避ける
4. **画像**: モバイルでは軽量版を配信
5. **フォーム**: 入力しやすい大きさ、適切なキーボードタイプ

### 画面サイズ別調整

**モバイル（〜767px）**
- 1カラムレイアウト
- フォントサイズ: 基本16px
- 余白: スペーシングの0.7倍

**タブレット（768px〜1023px）**
- 2カラムレイアウト可能
- フォントサイズ: 基本16px
- 余白: スペーシングの0.85倍

**デスクトップ（1024px〜）**
- 2〜3カラムレイアウト
- フォントサイズ: 基本16px
- 余白: スペーシング通り

### レスポンシブ実装例

```css
/* モバイルファースト */
.bibi-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  padding: 20px;
}

/* タブレット */
@media (min-width: 768px) {
  .bibi-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    padding: 40px;
  }
}

/* デスクトップ */
@media (min-width: 1024px) {
  .bibi-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
  }
}
```

---

## 🔍 実装時の注意事項

### DO（推奨）

✅ 全ページで同じカラーコードを使用  
✅ 見出し階層を守る（H1→H2→H3...）  
✅ すべての主要タグに固有クラス名を付与  
✅ タグ単体へのスタイル指定を避け、固有クラスでスコープを限定  
✅ alt属性を必ず記載  
✅ モバイルで実際に確認する  
✅ ページ読み込み速度を意識（画像最適化、不要なCSSを削除）  
✅ コントラスト比を確認（テキストの可読性）

### DON'T（禁止）

❌ 勝手にカラーコードを変更しない  
❌ 汎用クラス名（btn、inner、wrap等）を使用しない  
❌ タグ単体（a、p、ul等）に直接スタイルを当てない  
❌ グローバルセレクタ（*、body、html）を使用しない  
❌ フォントサイズを14px未満にしない（本文）  
❌ 見出しタグを装飾目的で使用しない  
❌ 画像を過度に加工しない（症例写真は特に）  
❌ 1ページに複数のH1を使用しない  
❌ インラインCSSを乱用しない（保守性低下）

---

## 📊 デザインチェックリスト

新規ページ作成時、以下を確認：

### カラー・タイポグラフィ
- [ ] カラーパレットに従っているか
- [ ] フォントサイズ・行間が適切か
- [ ] コントラスト比は4.5:1以上か
- [ ] 見出し階層が正しいか（H1→H2→H3...）

### HTML/CSS実装
- [ ] すべての主要タグに固有クラス名が付与されているか
- [ ] タグ単体へのスタイル指定をしていないか
- [ ] グローバルセレクタを使用していないか
- [ ] 固有クラス内でスコープが限定されているか

### アクセシビリティ・パフォーマンス
- [ ] 画像にalt属性があるか
- [ ] ボタンのタップ領域は十分か（44x44px以上）
- [ ] ページ読み込み速度は3秒以内か

### レスポンシブ
- [ ] モバイルで表示が崩れていないか
- [ ] 全ブラウザで表示確認したか（Chrome, Safari, Edge, Firefox）

---

## 🎨 ブランドの一貫性

### トーン&マナー

**ビジュアルトーン**
- 清潔感: オフホワイト（#f5f6f9）をベースに、パープル系でアクセント
- 信頼感: プロフェッショナルなレイアウト、過度な装飾は避ける
- 親しみやすさ: 柔らかい色合い、適度な余白

**対象ユーザー配慮（40代女性）**
- 文字は大きめ、行間は広め
- 派手すぎない、落ち着いた配色
- 分かりやすい導線、迷わせない設計

---

## 🔄 更新履歴

| バージョン | 日付 | 変更内容 | 担当者 |
|----------|------|---------|--------|
| v2.0 | 2025-12-09 | カラーパレット全面更新、HTML/CSS/JavaScript実装ルール追加 | システム更新 |
| v1.1 | 2025-11-26 | v90詳細版への参照追加 | システム構築チーム |
| v1.0 | 2025-11-26 | 初版作成、全セクション定義 | システム構築チーム |

---

**このファイルは全ページ作成時に必ず参照すること。**

**関連ファイル**: 01_HP運営原則_why.md, 04_ドクター・クリニック情報.md

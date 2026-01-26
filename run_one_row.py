import os, json, base64, uuid, datetime
import requests
from dotenv import load_dotenv

from googleapiclient.discovery import build
import google.auth

load_dotenv(".env")

# ====== Required ENV ======
SHEET_ID  = os.getenv("SHEET_ID")
SHEET_TAB = os.getenv("SHEET_TAB")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL   = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # export OPENAI_MODEL=... で上書き可

WP_BASE_URL = os.getenv("WP_BASE_URL", "").rstrip("/")
WP_USER     = os.getenv("WP_USER")
WP_APP_PASS = os.getenv("WP_APP_PASS")

if not SHEET_ID or not SHEET_TAB:
    raise RuntimeError("SHEET_ID / SHEET_TAB が未設定です。先に export してください。")

def now_jst_iso():
    jst = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")

def auth_header_basic(user: str, app_pass: str) -> dict:
    token = base64.b64encode(f"{user}:{app_pass}".encode("utf-8")).decode("utf-8")
    return {"Authorization": f"Basic {token}"}

def sheets_service():
    creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return build("sheets", "v4", credentials=creds)

def get_values(svc, range_a1: str):
    res = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=range_a1
    ).execute()
    return res.get("values", [])

def update_values(svc, range_a1: str, values):
    svc.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=range_a1,
        valueInputOption="RAW",
        body={"values": values}
    ).execute()

def norm(s):
    return (s or "").strip().lower().replace("　", " ")

def find_header_map(headers):
    """
    STEP1対応:
    - 日本語列名をalias登録
    - 同名列（モニタープラン×2）に備える
      1) もし「モニタープラン（判定）」「モニタープラン（表示）」があるならそれを優先
      2) もし「モニタープラン」が2つあるなら、出現順で judge / display に割り当て
    """
    aliases = {
        "status": ["status", "ステータス"],
        "raw_input": ["raw_input", "raw input", "該当のカルテ情報", "該当カルテ情報", "raw"],
        "title": ["title", "症例タイトル案", "症例タイトル", "WPタイトル", "wp_title", "タイトル"],
        "blog_title": ["note/アメブロ タイトル", "アメブロタイトル", "noteタイトル"],

        "wp_draft_url": ["wp_draft_url", "wp下書きurl", "wp下書き url", "wp下書き", "wp draft url"],
        "wp_post_id": ["wp_post_id", "wp_postid", "post_id", "wp_post_id"],
        "flags": ["flags", "要確認点", "要確認", "flag"],
        "error_message": ["error_message", "error", "エラー", "エラーメッセージ"],
        "generated_at": ["generated_at", "生成日時", "generated at"],
        "started_at": ["started_at", "開始", "started at"],
        "finished_at": ["finished_at", "終了", "finished at"],
        "row_lock": ["row_lock", "ロック", "lock"],

        # ====== 追加：構造化入力に必要な列（STEP2） ======
        "final_slug": ["final_slug", "完成スラッグ(url)", "完成スラッグ", "完成slug", "完成スラッグ（url）", "完成slug(url)"],
        "main_worry": ["主な悩み", "主訴", "悩み"],
        "intent_kw": ["検索意図キーワード", "検索意図kw", "検索kw", "intent_kw", "kw"],
        "meta_desc": ["メタディスクリプション", "meta", "description", "meta_desc"],
        "category_url": ["カテゴリーページurl", "カテゴリページurl", "カテゴリurl", "category_url", "category"],
        "wp_slug": ["wpコピペ用スラッグ", "wp_slug", "slug_wp", "wpスラッグ", "wp slug", "slug"],

        "thumb": ["サムネ", "サムネイル", "thumbnail", "thumb"],
        "sub1": ["サブ1", "sub1"],
        "sub2": ["サブ2", "sub2"],
        "sub3": ["サブ3", "sub3"],
        "sub4": ["サブ4", "sub4"],
        "karte_url": ["karte_url", "カルテurl", "カルテ url"],
        "case_id": ["cass/id", "cassid", "case_id", "カルテ番号", "id"],

        # モニタープラン（分割済みがあればそれを優先）
        "monitor_plan_judge": ["モニタープラン（判定）", "モニター判定", "monitor_plan_judge"],
        "monitor_plan_display": ["モニタープラン（表示）", "モニター表示", "monitor_plan_display"],
        # 旧：同名列
        "monitor_plan": ["モニタープラン", "モニター", "plan"],
    }

    headers_n = [norm(h) for h in headers]
    idx = {}

    # まず通常のキーを拾う（monitor_plan系以外）
    for key, cand_list in aliases.items():
        if key in ("monitor_plan", "monitor_plan_judge", "monitor_plan_display"):
            continue
        cand_n = [norm(x) for x in cand_list]
        for i, h in enumerate(headers_n):
            if h in cand_n or any(c in h for c in cand_n if c):
                idx[key] = i
                break

    # monitor_plan_judge / display を優先して探す
    def find_all_indices(candidates):
        cand_n = [norm(x) for x in candidates]
        hits = []
        for i, h in enumerate(headers_n):
            if h in cand_n or any(c in h for c in cand_n if c):
                hits.append(i)
        return hits

    judge_hits = find_all_indices(aliases["monitor_plan_judge"])
    display_hits = find_all_indices(aliases["monitor_plan_display"])

    if judge_hits:
        idx["monitor_plan_judge"] = judge_hits[0]
    if display_hits:
        idx["monitor_plan_display"] = display_hits[0]

    # 分割列が無い場合、旧「モニタープラン」が2つある想定で出現順に割り当て
    if "monitor_plan_judge" not in idx or "monitor_plan_display" not in idx:
        legacy_hits = find_all_indices(aliases["monitor_plan"])
        if len(legacy_hits) >= 1 and "monitor_plan_judge" not in idx:
            idx["monitor_plan_judge"] = legacy_hits[0]
        if len(legacy_hits) >= 2 and "monitor_plan_display" not in idx:
            idx["monitor_plan_display"] = legacy_hits[1]
        # 旧列が1つしか無い場合はそれを両方で使う（最終フォールバック）
        if len(legacy_hits) == 1:
            idx.setdefault("monitor_plan_display", legacy_hits[0])

    return idx

def safe_cell(row, headers_len, i):
    if i is None:
        return ""
    if i < 0:
        return ""
    if i >= headers_len:
        return ""
    if i >= len(row):
        return ""
    return row[i] or ""

def build_structured_input(row, headers_len, idx) -> str:
    """
    STEP2対応:
    raw_input単体 → 全列の構造化ブロック入力へ
    """
    def g(key):
        return str(safe_cell(row, headers_len, idx.get(key))).strip()

    title = g("title")
    structured = f"""あなたは美容クリニックの医師です。
以下の入力（構造化データ）を元に、美容医療の症例ページ用「HTML本文」だけを生成してください。

【重要】
- titleは固定（本文中の見出しに使ってOKだが、別案生成はしない）
- 推測でcc/本数/金額/適応/経過などを作らない（未記載は「記載なし」扱い）
- 医療広告として断定・誇張・No.1/最安などの表現は避ける
- 出力はHTMLのみ（本文だけ）。```や説明文は不要

【固定情報】
title: {title}
主な悩み: {g("main_worry")}
検索意図KW: {g("intent_kw")}
メタディスクリプション: {g("meta_desc")}
カテゴリーページURL: {g("category_url")}
WPスラッグ: {g("wp_slug")}
完成スラッグ(URL): {g("final_slug")}

【画像】
サムネ: {g("thumb")}
サブ1: {g("sub1")}
サブ2: {g("sub2")}
サブ3: {g("sub3")}
サブ4: {g("sub4")}

【カルテ情報】
karte_url: {g("karte_url")}
カルテ番号: {g("case_id")}
raw_input:
{g("raw_input")}

【制約】
モニタープラン（判定）: {g("monitor_plan_judge")}
モニタープラン（表示）: {g("monitor_plan_display")}

【出力要件】
- <h2>〜などを使い、症例ページとして読みやすい構成にする
- 内部リンクを貼れる箇所があれば、カテゴリーページURLや完成スラッグ(URL)を自然に挿入してよい（押し売り禁止）
- 価格は入力に無ければ書かない（推測禁止）
"""
    return structured

def openai_generate_html(structured_input: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }f

    payload = {
        "model": OPENAI_MODEL,
        "input": structured_input,
        "max_output_tokens": 2200,
    }

    r = requests.post("https://api.openai.com/v1/responses", headers=headers, json=payload, timeout=120)
    if r.status_code >= 300:
        raise RuntimeError(f"OpenAI error {r.status_code}: {r.text}")

    data = r.json()

    text = None
    if "output_text" in data and data["output_text"]:
        text = data["output_text"]
    else:
        try:
            chunks = []
            for o in data.get("output", []):
                for c in o.get("content", []):
                    if c.get("type") in ("output_text", "text"):
                        chunks.append(c.get("text", ""))
            text = "\n".join(chunks).strip()
        except Exception:
            text = None

    if not text:
        raise RuntimeError("No HTML generated")
    return text

def wp_create_draft(title: str, html: str, slug: str = ""):
    url = f"{WP_BASE_URL}/wp-json/wp/v2/posts"
    headers = {"Content-Type": "application/json"}
    headers.update(auth_header_basic(WP_USER, WP_APP_PASS))

    body = {"title": title, "content": html, "status": "draft"}
    if slug:
        # STEP3のWP反映ルール：post_name(slug)にWPコピペ用スラッグを使う
        body["slug"] = slug

    r = requests.post(url, headers=headers, json=body, timeout=120)
    if r.status_code >= 300:
        raise RuntimeError(f"WP error {r.status_code}: {r.text}")

    post = r.json()
    return post.get("id"), post.get("link")

def main():
    svc = sheets_service()

    # A:AZくらい広めに取る
    values = get_values(svc, f"{SHEET_TAB}!A1:AZ2000")
    if not values or len(values) < 2:
        raise RuntimeError("シートにデータがない or 範囲が取れていません。SHEET_TAB（タブ名）を確認してください。")

    # 既存運用どおり「2行目がヘッダー」
    headers = values[1]
    idx = find_header_map(headers)
    headers_len = len(headers)

    # 必須列チェック（STEP1/2に必要）
    required = ["status", "raw_input", "title", "wp_slug"]
    missing = [k for k in required if k not in idx]
    if missing:
        raise RuntimeError(f"必須列が見つかりません: {', '.join(missing)}（ヘッダー名/aliasを確認）")

    # Status=New の最初の1行を探す
    target_row = None
    for r_i in range(2, len(values)):  # 2 = 3行目（実データ開始）
        row = values[r_i] + [""] * (headers_len - len(values[r_i]))
        status = (row[idx["status"]] or "").strip().lower()
        if status == "new":
            target_row = (r_i, row)
            break

    if not target_row:
        print("No target row: Status=New が見つかりませんでした。")
        return

    r_i, row = target_row
    rownum = r_i + 1  # A1の行番号

    title = (safe_cell(row, headers_len, idx["title"]) or "").strip()
    if not title:
        raise RuntimeError("title が空です（シートの title 列を確認）")

    wp_slug = (safe_cell(row, headers_len, idx["wp_slug"]) or "").strip()
    if not wp_slug:
        raise RuntimeError("WPコピペ用スラッグ（wp_slug）が空です")

    # Runningにしてロック
    lock = str(uuid.uuid4())[:8]
    started = now_jst_iso()

    def set_cell(col_key, value):
        if col_key in idx:
            col = idx[col_key]
            row[col] = value

    set_cell("row_lock", lock)
    set_cell("started_at", started)
    set_cell("status", "Running")
    update_values(svc, f"{SHEET_TAB}!A{rownum}:AZ{rownum}", [row])

    try:
        raw_text = (safe_cell(row, headers_len, idx["raw_input"]) or "").strip()
        if not raw_text:
            raise RuntimeError("raw_input が空です")

        structured_input = build_structured_input(row, headers_len, idx)
        html = openai_generate_html(structured_input)

        post_id, link = wp_create_draft(title=title, html=html, slug=wp_slug)

        finished = now_jst_iso()
        set_cell("wp_post_id", str(post_id))
        set_cell("wp_draft_url", link or "")
        set_cell("generated_at", finished)
        set_cell("finished_at", finished)
        set_cell("error_message", "")
        if "flags" in idx:
            set_cell("flags", "")

        set_cell("status", "Done")
        update_values(svc, f"{SHEET_TAB}!A{rownum}:AZ{rownum}", [row])

        print("DONE")
        print("row:", rownum)
        print("post_id:", post_id)
        print("link:", link)

    except Exception as e:
        finished = now_jst_iso()
        set_cell("finished_at", finished)
        set_cell("generated_at", finished)
        set_cell("error_message", str(e)[:500])
        set_cell("status", "Error")
        update_values(svc, f"{SHEET_TAB}!A{rownum}:AZ{rownum}", [row])
        raise

if __name__ == "__main__":
    main()
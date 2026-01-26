import os
import json
import base64
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WP_BASE_URL = os.getenv("WP_BASE_URL", "").rstrip("/")
WP_USER = os.getenv("WP_USER")
WP_APP_PASS = os.getenv("WP_APP_PASS")

def openai_generate_html(normalized):
    prompt = "Generate simple HTML for a cosmetic clinic case page based on the JSON below.\n\nJSON:\n"
    prompt += json.dumps(normalized, ensure_ascii=False)

    r = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": "Bearer " + OPENAI_API_KEY,
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4.1-mini",
            "input": prompt,
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()

    # Primary: output_text (if available)
    if isinstance(data, dict) and data.get("output_text"):
        return data["output_text"].strip()

    # Fallback: structured output
    try:
        return data["output"][0]["content"][0]["text"].strip()
    except Exception:
        print("DEBUG response:", json.dumps(data, ensure_ascii=False, indent=2))
        raise RuntimeError("No HTML generated")

def wp_create_draft(title, html):
    token = base64.b64encode((WP_USER + ":" + WP_APP_PASS).encode()).decode()
    r = requests.post(
        WP_BASE_URL + "/wp-json/wp/v2/posts",
        headers={
            "Authorization": "Basic " + token,
            "Content-Type": "application/json",
        },
        json={
            "title": title,
            "content": html,
            "status": "draft",
        },
        timeout=60,
    )
    r.raise_for_status()
    return r.json()

def main():
    with open("input_case.json", "r", encoding="utf-8") as f:
        normalized = json.load(f)

    html = openai_generate_html(normalized)
    post = wp_create_draft("Test Case", html)

    print("DONE")
    print("post_id:", post.get("id"))
    print("link:", post.get("link"))

if __name__ == "__main__":
    main()

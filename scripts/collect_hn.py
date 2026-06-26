#!/usr/bin/env python3
"""
Hacker News Auto-Collector for LLM Wiki
매일 HN Top Stories 중 관심 분야 기사를 자동 수집
"""
import urllib.request
import json
import re
import time
import os
import subprocess
from pathlib import Path
from datetime import date

WIKI_PATH = Path.home() / "wiki"
HN_LOG = WIKI_PATH / ".hn_last_ingest.json"

# ── LLM Translation ─────────────────────────────────

def translate_to_korean(text: str, max_chars: int = 2000) -> str:
    """LLM으로 영문 → 한글 번역"""
    if not text or len(text.strip()) < 20:
        return text
    korean_chars = len(re.findall(r'[가-힣]', text))
    if korean_chars > len(text) * 0.3:
        return text
    text_short = text[:max_chars]
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        try:
            result = subprocess.run(["zsh", "-lc", "echo $OPENROUTER_API_KEY"], capture_output=True, text=True, timeout=5)
            api_key = result.stdout.strip()
        except Exception:
            pass
    if not api_key:
        zshrc = Path.home() / ".zshrc"
        if zshrc.exists():
            content = zshrc.read_text()
            match = re.search(r'OPENROUTER_API_KEY\s*=\s*["\']?(sk-or-v1-\w+)["\']?', content)
            if match:
                api_key = match.group(1)
    if not api_key:
        return text
    payload = {
        "model": "openrouter/owl-alpha",
        "messages": [
            {"role": "system", "content": "다음 텍스트를 자연스러운 한국어로 번역하세요. 기술 용어는 원문을 병기해도 됩니다. 번역만 출력하세요."},
            {"role": "user", "content": text_short},
        ],
        "max_tokens": 1024, "temperature": 0.3,
    }
    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=data, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
        resp = urllib.request.urlopen(req, timeout=30)
        result = json.loads(resp.read())
        translated = result["choices"][0]["message"]["content"].strip()
        if len(text) > max_chars:
            translated += "\n\n(이하 생략...)"
        return translated
    except Exception:
        return text

# 관심 키워드 (제목/URL에 포함되면 수집)
INTEREST_KEYWORDS = [
    "ai", "llm", "gpt", "claude", "machine learning",
    "python", "rust", "open source", "startup",
    "security", "programming", "developer", "api",
    "cloud", "linux", "database", "web3", "crypto",
    "apple", "google", "meta", "microsoft", "nvidia",
    "chip", "gpu", "neural", "diffusion", "agent",
    "automation", "robot", "safety", "alignment",
]

# 제외 키워드
EXCLUDE_KEYWORDS = [
    "crypto scam", "nft", "celebrity", "political",
]

MAX_STORIES_PER_RUN = 5  # 한 번에 최대 수집 기사 수
HN_API_BASE = "https://hacker-news.firebaseio.com/v0"


def load_log() -> dict:
    if HN_LOG.exists():
        return json.loads(HN_LOG.read_text())
    return {"last_run": "", "ingested_ids": []}


def save_log(log: dict):
    HN_LOG.write_text(json.dumps(log, indent=2))


def hn_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "LLM-Wiki/1.0"})
    resp = urllib.request.urlopen(req, timeout=15)
    return json.loads(resp.read())


def fetch_top_stories(limit: int = 30) -> list:
    """Top Stories ID 목록 → 상세 정보"""
    ids = hn_get(f"{HN_API_BASE}/topstories.json")[:limit]
    stories = []
    for story_id in ids:
        try:
            data = hn_get(f"{HN_API_BASE}/item/{story_id}.json")
            if data and data.get("title"):
                stories.append({
                    "id": str(data["id"]),
                    "title": data["title"],
                    "url": data.get("url", f"https://news.ycombinator.com/item?id={data['id']}"),
                    "score": data.get("score", 0),
                    "by": data.get("by", ""),
                    "time": data.get("time", 0),
                    "descendants": data.get("descendants", 0),
                })
            time.sleep(0.1)  # Rate limit
        except Exception:
            pass
    return stories


def fetch_article_content(url: str) -> str:
    """기사 원문 가져오기"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; LLM-Wiki/1.0)"})
        resp = urllib.request.urlopen(req, timeout=15)
        content = resp.read().decode("utf-8", errors="ignore")

        # 간단한 텍스트 추출 (script/style 제거)
        content = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.DOTALL)
        content = re.sub(r"<style[^>]*>.*?</style>", "", content, flags=re.DOTALL)
        content = re.sub(r"<[^>]+>", " ", content)
        content = re.sub(r"\s+", " ", content).strip()

        return content[:5000]  # 앞 5000자만
    except Exception:
        return ""


def should_include(story: dict) -> bool:
    text = (story["title"] + " " + story.get("url", "")).lower()
    # 제외 키워드
    for kw in EXCLUDE_KEYWORDS:
        if kw in text:
            return False
    # 관심 키워드 매치
    for kw in INTEREST_KEYWORDS:
        if kw in text:
            return True
    return False


def create_wiki_page(story: dict, content: str):
    """HN 기사 → 위키 페이지 생성 (한글 번역 포함)"""
    date_str = date.today().isoformat()
    slug = re.sub(r"[^\w\-]", "-", story["title"].lower())[:60].strip("-")
    slug = re.sub(r"-+", "-", slug)

    # 🔄 한글 번역
    print(f"     🔄 번역 중...", end=" ", flush=True)
    title_kr = translate_to_korean(story["title"], max_chars=200)
    content_kr = translate_to_korean(content[:1000], max_chars=1000) if content else ""
    print("✅")

    # 원본 저장 (영문)
    raw_dir = WIKI_PATH / "raw" / "articles"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"hn-{slug}-{date_str}.md"

    raw_content = f"""---
source_url: {story['url']}
ingested: {date_str}
type: hn_article
hn_id: {story['id']}
hn_score: {story['score']}
hn_author: {story['by']}
---

# {story['title']}

**Score:** {story['score']} | **By:** {story['by']} | **Comments:** {story.get('descendants', 0)}
**URL:** {story['url']}
**HN:** https://news.ycombinator.com/item?id={story['id']}

## Content

{content if content else '(Could not fetch article content)'}
"""
    raw_path.write_text(raw_content, encoding="utf-8")

    # 컨셉 페이지 (한글 번역본)
    concept_dir = WIKI_PATH / "concepts"
    concept_dir.mkdir(parents=True, exist_ok=True)
    concept_path = concept_dir / f"hn-{slug}.md"

    tags = ["news"]
    text = story["title"].lower()
    tag_map = {
        "ai-ml": ["ai", "llm", "gpt", "claude", "machine learning", "neural", "diffusion", "agent"],
        "programming": ["python", "rust", "code", "developer", "api", "programming"],
        "security": ["security", "hack", "vulnerability", "exploit", "crypto"],
        "business": ["startup", "company", "funding", "layoff", "revenue"],
        "science": ["research", "paper", "study", "discovery"],
        "tech": ["apple", "google", "meta", "microsoft", "nvidia", "linux", "open source"],
    }
    for tag, keywords in tag_map.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)

    preview_kr = content_kr[:400] if content_kr else "원문 참조"

    concept_content = f"""---
title: {title_kr}
created: {date_str}
updated: {date_str}
type: concept
tags: [{', '.join(tags)}]
sources: [raw/articles/{raw_path.name}]
confidence: medium
source_type: hn
---

# {title_kr}

> 📰 원문: [{story['title']}]({story['url']})
> 🔥 HN Score: {story['score']} | By: {story['by']} | 💬 Comments: {story.get('descendants', 0)}
> 🔗 HN Discussion: https://news.ycombinator.com/item?id={story['id']}

## 요약

{preview_kr}

## 원문 영어

<details>
<summary>원문 보기</summary>

{content[:500] if content else '(원문을 가져올 수 없습니다)'}

</details>

## HN 토론

- [HN 댓글 보기](https://news.ycombinator.com/item?id={story['id']})
- [원문 기사 읽기]({story['url']})
"""
    concept_path.write_text(concept_content, encoding="utf-8")

    return str(raw_path), str(concept_path)


def main():
    print(f"🔥 Hacker News Auto-Collector — {date.today().isoformat()}")
    print()

    log = load_log()
    today = date.today().isoformat()

    if log.get("last_run") == today:
        print("⏭️ Already ran today. Skip.")
        return

    ingested_ids = set(log.get("ingested_ids", []))

    print("  Fetching top stories...")
    stories = fetch_top_stories(limit=50)
    print(f"  Got {len(stories)} stories.\n")

    # 관심 키워드 필터
    matched = [s for s in stories if should_include(s)]
    new_stories = [s for s in matched if s["id"] not in ingested_ids][:MAX_STORIES_PER_RUN]

    if not new_stories:
        print("  No new matching stories.")
        log["last_run"] = today
        save_log(log)
        return

    print(f"  Found {len(new_stories)} new matching stories:\n")
    for i, story in enumerate(new_stories, 1):
        print(f"  {i}. {story['title'][:70]}")
        print(f"     Score: {story['score']} | {story['url'][:80]}")

        content = fetch_article_content(story["url"])
        try:
            raw_path, concept_path = create_wiki_page(story, content)
            ingested_ids.add(story["id"])
            print(f"     ✅ Saved")
        except Exception as e:
            print(f"     ❌ Error: {e}")

        time.sleep(0.5)  # Rate limit

    log["last_run"] = today
    log["ingested_ids"] = list(ingested_ids)[-500:]
    save_log(log)

    print(f"\n✅ Done! {len(new_stories)} stories ingested.")


if __name__ == "__main__":
    main()

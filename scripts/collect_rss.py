#!/usr/bin/env python3
"""
LLM Wiki — RSS/Feed collector
기술 블로그, 뉴스레터, RSS 피드를 구독하여 raw/articles/에 저장
"""
import os
import re
import json
import time
import hashlib
import urllib.request
from pathlib import Path
from datetime import datetime
from email.utils import parsedate_to_datetime

WIKI_PATH = Path.home() / "wiki"
RAW_DIR = WIKI_PATH / "raw" / "articles"
FEED_FILE = WIKI_PATH / "scripts" / "feeds.json"

# 구독할 RSS 피드 목록
DEFAULT_FEEDS = [
    # 한국 기술 블로그
    {"url": "https://tech.kakao.com/feed/", "name": "Kakao Tech", "lang": "ko"},
    {"url": "https://techblog.woowahan.com/feed/", "name": "우아한형제들 Tech", "lang": "ko"},
    {"url": "https://blog.naver.com/Res/atom.naver?blogId=naver_search", "name": "Naver Search Blog", "lang": "ko"},
    {"url": "https://engineering.linecorp.com/ko/feed", "name": "LINE Engineering", "lang": "ko"},
    {"url": "https://toss.tech/feed.xml", "name": "Toss Tech", "lang": "ko"},
    # 해외 기술 블로그
    {"url": "https://openai.com/blog/rss/", "name": "OpenAI Blog", "lang": "en"},
    {"url": "https://ai.googleblog.com/feeds/posts/default", "name": "Google AI Blog", "lang": "en"},
    {"url": "https://research.facebook.com/blog/rss/", "name": "Meta AI Research", "lang": "en"},
    {"url": "https://news.ycombinator.com/rss", "name": "Hacker News", "lang": "en"},
    {"url": "https://arxiv.org/rss/cs.AI", "name": "arXiv AI", "lang": "en"},
    {"url": "https://simonwillison.net/atom/everything/", "name": "Simon Willison", "lang": "en"},
    {"url": "https://lilianweng.github.io/atom.xml", "name": "Lilian Weng", "lang": "en"},
]


def load_feeds():
    if FEED_FILE.exists():
        with open(FEED_FILE) as f:
            return json.load(f)
    return DEFAULT_FEEDS


def save_feeds(feeds):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    with open(FEED_FILE, "w") as f:
        json.dump(feeds, f, ensure_ascii=False, indent=2)


def fetch_rss(url, timeout=15):
    """RSS 피드 가져오기"""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "LLM-Wiki/1.0 (bearj)"}
    )
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [ERROR] {url}: {e}", flush=True)
        return None


SEEN_FILE = WIKI_PATH / ".seen_feeds.json"


def load_seen():
    if SEEN_FILE.exists():
        with open(SEEN_FILE) as f:
            return set(json.load(f))
    return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def parse_rss_simple(content, feed_name, lang):
    """간단한 RSS/Atom 파서 (정규식 기반)"""
    items = []

    # Atom
    entries = re.findall(
        r'<entry>.*?<title.*?>(.*?)</title>.*?'
        r'<link.*?href="(.*?)".*?/>.*?'
        r'<published>(.*?)</published>.*?'
        r'<summary.*?>(.*?)</summary>',
        content, re.DOTALL
    )
    if not entries:
        # RSS 2.0
        entries = re.findall(
            r'<item>.*?<title.*?>(.*?)</title>.*?'
            r'<link.*?>(.*?)</link>.*?'
            r'<pubDate>(.*?)</pubDate>.*?'
            r'<description.*?>(.*?)</description>',
            content, re.DOTALL
        )

    for title, link, pub_date, description in entries:
        title = re.sub(r'<[^>]+>', '', title).strip()
        description = re.sub(r'<[^>]+>', '', description).strip()[:500]

        try:
            dt = parsedate_to_datetime(pub_date)
        except Exception:
            dt = datetime.now()

        items.append({
            "title": title,
            "url": link.strip(),
            "date": dt.strftime("%Y-%m-%d"),
            "summary": description[:300],
            "feed": feed_name,
            "lang": lang,
        })

    return items


def collect_all():
    """모든 피드 수집"""
    feeds = load_feeds()
    seen = load_seen()
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    total_collected = 0
    for feed in feeds:
        print(f"Fetching: {feed['name']} ({feed['url']})", flush=True)
        content = fetch_rss(feed["url"])
        if not content:
            continue

        items = parse_rss_simple(content, feed["name"], feed.get("lang", "en"))
        new_count = 0
        for item in items:
            item_id = hashlib.md5(item["url"].encode()).hexdigest()
            if item_id in seen:
                continue

            seen.add(item_id)
            slug = re.sub(r'[^\w\-]', '-', item["title"].lower())[:60]
            slug = re.sub(r'-+', '-', slug).strip('-')

            file_path = RAW_DIR / f"{slug}.md"
            if file_path.exists():
                continue

            frontmatter = (
                f"---\n"
                f"title: \"{item['title']}\"\n"
                f"source: {item['feed']}\n"
                f"url: {item['url']}\n"
                f"date: {item['date']}\n"
                f"lang: {item['lang']}\n"
                f"type: reference\n"
                f"tags: [feed, {item['feed'].lower().replace(' ', '-')}]\n"
                f"---\n\n"
            )
            content = frontmatter + f"# {item['title']}\n\n"
            content += f"> Source: [{item['feed']}]({item['url']})  \n"
            content += f"> Date: {item['date']}\n\n"
            content += f"{item['summary']}\n\n"
            content += f"---\n*전문 보기: [{item['title']}]({item['url']})*"

            try:
                file_path.write_text(content, encoding="utf-8")
                new_count += 1
                total_collected += 1
            except Exception as e:
                print(f"  [WRITE ERROR] {e}", flush=True)

        print(f"  → {new_count} new items from {feed['name']}", flush=True)

    save_seen(seen)
    print(f"\n✅ Collected {total_collected} new items total", flush=True)
    return total_collected


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "add":
        save_feeds(DEFAULT_FEEDS + [{"url": sys.argv[2], "name": sys.argv[3] if len(sys.argv) > 3 else sys.argv[2], "lang": "en"}])
        print(f"Added feed: {sys.argv[2]}", flush=True)
    elif len(sys.argv) > 1 and sys.argv[1] == "list":
        feeds = load_feeds()
        for i, f in enumerate(feeds):
            print(f"  [{i}] {f['name']} ({f['lang']}) - {f['url']}")
    else:
        collect_all()

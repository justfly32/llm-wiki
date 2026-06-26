#!/usr/bin/env python3
"""
arXiv Auto-Collector for LLM Wiki
매일 관심 키워드로 arXiv를 검색해서 새 논문을 자동 수집
"""
import urllib.request
import urllib.parse
import json
import re
import os
import sys
import subprocess
from pathlib import Path
from datetime import date, datetime, timedelta

WIKI_PATH = Path.home() / "wiki"
ARXIV_LOG = WIKI_PATH / ".arxiv_last_ingest.json"

# ── LLM Translation ─────────────────────────────────

def translate_to_korean(text: str, max_chars: int = 2000) -> str:
    """LLM으로 영문 → 한글 번역. 짧은 텍스트만 번역 (비용 절감)."""
    if not text or len(text.strip()) < 20:
        return text
    
    # 이미 한글이 많으면 번역 건너뜀
    korean_chars = len(re.findall(r'[가-힣]', text))
    if korean_chars > len(text) * 0.3:
        return text
    
    text_short = text[:max_chars]
    
    # OpenRouter API 키 가져오기
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        try:
            result = subprocess.run(
                ["zsh", "-lc", "echo $OPENROUTER_API_KEY"],
                capture_output=True, text=True, timeout=5
            )
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
        return text  # API 키 없으면 원문 반환
    
    system_prompt = "다음 텍스트를 자연스러운 한국어로 번역하세요. 기술 용어는 원문을 병기해도 됩니다. 번역만 출력하세요."
    
    payload = {
        "model": "openrouter/owl-alpha",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_short},
        ],
        "max_tokens": 1024,
        "temperature": 0.3,
    }
    
    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=data,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        resp = urllib.request.urlopen(req, timeout=30)
        result = json.loads(resp.read())
        translated = result["choices"][0]["message"]["content"].strip()
        if len(text) > max_chars:
            translated += "\n\n(이하 생략...)"
        return translated
    except Exception:
        return text  # 실패 시 원문 반환


def translate_paper(title: str, summary: str) -> tuple:
    """논문 제목 + 요약을 한글로 번역"""
    title_kr = translate_to_korean(title, max_chars=200)
    summary_kr = translate_to_korean(summary, max_chars=1500)
    return title_kr, summary_kr

# 관심 키워드 (여기 추가/수정하면 됨)
INTEREST_KEYWORDS = [
    "large language model",
    "transformer",
    "reinforcement learning",
    "diffusion model",
    "multimodal",
    "agent",
    "alignment",
    "inference optimization",
    "fine-tuning",
    "retrieval augmented",
]

# 제외 키워드 (스팍/관련 없는 것)
EXCLUDE_KEYWORDS = [
    "cryptocurrency", "blockchain", "quantum gravity",
    "dark matter", "supersymmetry",
]

MAX_PAPERS_PER_RUN = 5  # 한 번에 최대 수집 논문 수


def load_log() -> dict:
    if ARXIV_LOG.exists():
        return json.loads(ARXIV_LOG.read_text())
    return {"last_run": "", "ingested_ids": []}


def save_log(log: dict):
    ARXIV_LOG.write_text(json.dumps(log, indent=2))


def search_arxiv(query: str, max_results: int = 10) -> list:
    """arXiv API로 검색"""
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"https://export.arxiv.org/api/query?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "LLM-Wiki/1.0"})
        resp = urllib.request.urlopen(req, timeout=30)
        data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ⚠️ arXiv API error: {e}")
        return []

    # 간단한 XML 파싱 (regex 기반)
    entries = []
    for entry_match in re.finditer(r"<entry>(.*?)</entry>", data, re.DOTALL):
        entry_text = entry_match.group(1)

        title = re.search(r"<title>(.*?)</title>", entry_text, re.DOTALL)
        title = title.group(1).strip().replace("\n", " ").strip() if title else "Unknown"

        summary = re.search(r"<summary>(.*?)</summary>", entry_text, re.DOTALL)
        summary = summary.group(1).strip().replace("\n", " ").strip() if summary else ""

        arxiv_id = re.search(r"<id>http://arxiv.org/abs/(.*?)</id>", entry_text)
        arxiv_id = arxiv_id.group(1) if arxiv_id else ""

        published = re.search(r"<published>(.*?)</published>", entry_text)
        published = published.group(1)[:10] if published else ""

        authors = re.findall(r"<name>(.*?)</name>", entry_text)
        authors = [a.strip() for a in authors[:3]]

        categories = re.findall(r"<category term=\"(.*?)\"", entry_text)

        if arxiv_id and title:
            entries.append({
                "id": arxiv_id,
                "title": title,
                "summary": summary[:2000],
                "published": published,
                "authors": authors,
                "categories": categories[:3],
            })

    return entries


def should_include(paper: dict) -> bool:
    """포함 여부 판단"""
    text = (paper["title"] + " " + paper["summary"]).lower()
    # 제외 키워드 체크
    for kw in EXCLUDE_KEYWORDS:
        if kw in text:
            return False
    return True


def create_wiki_page(paper: dict):
    """논문 → 위키 페이지 생성 (한글 번역 포함)"""
    date_str = date.today().isoformat()
    slug = re.sub(r"[^\w\-]", "-", paper["title"].lower())[:60].strip("-")
    slug = re.sub(r"-+", "-", slug)

    # 🔄 한글 번역
    print(f"     🔄 번역 중...", end=" ", flush=True)
    title_kr, summary_kr = translate_paper(paper["title"], paper["summary"])
    print("✅")

    # 원본 저장 (영문 원본)
    raw_dir = WIKI_PATH / "raw" / "papers"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"{slug}-{date_str}.md"

    raw_content = f"""---
source_url: https://arxiv.org/abs/{paper['id']}
ingested: {date_str}
type: paper
arxiv_id: {paper['id']}
authors: {', '.join(paper['authors'])}
published: {paper['published']}
categories: {', '.join(paper['categories'])}
---

# {paper['title']}

**Authors:** {', '.join(paper['authors'])}
**Published:** {paper['published']}
**arXiv:** https://arxiv.org/abs/{paper['id']}
**Categories:** {', '.join(paper['categories'])}

## Abstract

{paper['summary']}
"""
    raw_path.write_text(raw_content, encoding="utf-8")

    # 컨셉 페이지 생성 (한글 번역본)
    concept_dir = WIKI_PATH / "concepts"
    concept_dir.mkdir(parents=True, exist_ok=True)
    concept_path = concept_dir / f"{slug}.md"

    tags = ["research"]
    text = (paper["title"] + " " + paper["summary"]).lower()
    tag_map = {
        "ai-ml": ["language model", "neural", "deep learning", "machine learning", "llm"],
        "programming": ["code", "software", "programming", "api"],
        "alignment": ["alignment", "rlhf", "safety", "constitutional"],
        "optimization": ["optimization", "quantization", "pruning", "efficiency", "inference"],
        "multimodal": ["multimodal", "vision", "image", "video", "audio"],
        "agent": ["agent", "tool use", "planning", "reasoning"],
        "diffusion": ["diffusion", "generative", "image generation"],
    }
    for tag, keywords in tag_map.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)

    concept_content = f"""---
title: {title_kr}
created: {date_str}
updated: {date_str}
type: concept
tags: [{', '.join(tags)}]
sources: [raw/papers/{raw_path.name}]
confidence: medium
---

# {title_kr}

> 📄 원문: [{paper['title']}](https://arxiv.org/abs/{paper['id']})
> ✍️ 저자: {', '.join(paper['authors'])}
> 📅 발행: {paper['published']}
> 🏷️ 카테고리: {', '.join(paper['categories'])}

## 요약

{summary_kr}

## 원문 영어

<details>
<summary>원문 보기</summary>

{paper['summary'][:500]}

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/{paper['id']})
"""
    concept_path.write_text(concept_content, encoding="utf-8")

    return str(raw_path), str(concept_path)


def main():
    print(f"📚 arXiv Auto-Collector — {date.today().isoformat()}")
    print(f"   Keywords: {', '.join(INTEREST_KEYWORDS[:5])}...")
    print()

    log = load_log()
    today = date.today().isoformat()

    if log.get("last_run") == today:
        print("⏭️ Already ran today. Skip.")
        return

    ingested_ids = set(log.get("ingested_ids", []))
    new_papers = []
    seen_ids = set()

    for keyword in INTEREST_KEYWORDS:
        if len(new_papers) >= MAX_PAPERS_PER_RUN:
            break

        print(f"  Searching: '{keyword}'...")
        papers = search_arxiv(keyword, max_results=5)

        for paper in papers:
            if paper["id"] in ingested_ids or paper["id"] in seen_ids:
                continue
            if not should_include(paper):
                continue
            seen_ids.add(paper["id"])
            new_papers.append(paper)

            if len(new_papers) >= MAX_PAPERS_PER_RUN:
                break

    if not new_papers:
        print("  No new papers found.")
        log["last_run"] = today
        save_log(log)
        return

    print(f"\n  Found {len(new_papers)} new papers:\n")
    for i, paper in enumerate(new_papers, 1):
        print(f"  {i}. {paper['title'][:70]}")
        print(f"     {paper['published']} | {', '.join(paper['authors'][:2])}")

        try:
            raw_path, concept_path = create_wiki_page(paper)
            ingested_ids.add(paper["id"])
            print(f"     ✅ Saved: {Path(concept_path).name}")
        except Exception as e:
            print(f"     ❌ Error: {e}")

    log["last_run"] = today
    log["ingested_ids"] = list(ingested_ids)[-500:]  # 최근 500개만 유지
    save_log(log)

    print(f"\n✅ Done! {len(new_papers)} papers ingested.")


if __name__ == "__main__":
    main()

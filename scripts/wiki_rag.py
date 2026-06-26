#!/usr/bin/env python3
"""
LLM Wiki — Hybrid RAG Query Engine (BM25 + Vector)
위키 페이지 기반 질의응답 + 의미 검색

동작 방식:
1. 질문 → BM25 키워드 검색 + SentenceTransformer 벡터 검색 조합
2. 상위 N개 페이지 본문을 컨텍스트로 구성
3. LLM에 컨텍스트 + 질문을 보내서 답변 생성
"""
import os
import re
import json
import math
import pickle
import hashlib
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path
from collections import Counter
from typing import Optional

WIKI_PATH = Path.home() / "wiki"
ENTITIES_DIR = WIKI_PATH / "entities"
CONCEPTS_DIR = WIKI_PATH / "concepts"
COMPARISONS_DIR = WIKI_PATH / "comparisons"
QUERIES_DIR = WIKI_PATH / "queries"
CONCEPT_SUBDIRS = [CONCEPTS_DIR / d for d in ["daily", "knowledge", "learnings", "projects"] if (CONCEPTS_DIR / d).exists()]
ALL_DIRS = [ENTITIES_DIR, COMPARISONS_DIR, QUERIES_DIR] + CONCEPT_SUBDIRS
CACHE_FILE = WIKI_PATH / ".vector_cache.pkl"

# OpenRouter
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openrouter/owl-alpha"

# ── SentenceTransformer ──────────────────────────
_model = None
def get_encoder():
    global _model
    if _model is not None:
        return _model
    try:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("[wiki_rag] SentenceTransformer loaded", flush=True)
    except Exception as e:
        print(f"[wiki_rag] WARNING: SentenceTransformer failed: {e}", flush=True)
        _model = None
    return _model

# ── Page Loading ─────────────────────────────────

def get_all_page_texts() -> list:
    """모든 위키 페이지 텍스트 로드"""
    pages = []
    for d in ALL_DIRS:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
            title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else f.stem
            pages.append({
                "slug": f.stem,
                "title": title,
                "body": body[:3000],
                "path": str(f),
                "full_body": body[:8000],
            })
    return pages

# ── Tokenizer ────────────────────────────────────

def tokenize(text: str) -> list:
    return re.findall(r"[가-힣a-zA-Z0-9]+", text.lower())

# ── BM25 ─────────────────────────────────────────

def compute_bm25_score(query_tokens: list, doc_tokens: list, idf: dict, avg_dl: float, k1: float = 1.5, b: float = 0.75) -> float:
    if not doc_tokens:
        return 0.0
    dl = len(doc_tokens)
    tf = Counter(doc_tokens)
    score = 0.0
    for term in query_tokens:
        if term in idf:
            term_freq = tf.get(term, 0)
            numerator = term_freq * (k1 + 1)
            denominator = term_freq + k1 * (1 - b + b * dl / avg_dl) if avg_dl > 0 else term_freq + k1
            score += idf[term] * numerator / denominator
    return score

def build_idf(pages: list) -> tuple:
    N = len(pages)
    df = Counter()
    all_tokens = []
    for p in pages:
        tokens = tokenize(p["body"])
        all_tokens.append(tokens)
        for term in set(tokens):
            df[term] += 1
    idf = {}
    for term, count in df.items():
        idf[term] = math.log((N - count + 0.5) / (count + 0.5) + 1)
    avg_dl = sum(len(t) for t in all_tokens) / N if N > 0 else 0
    return idf, avg_dl

# ── Vector Search ────────────────────────────────

def compute_embeddings(pages: list) -> list:
    """페이지 임베딩 계산 (캐싱)"""
    encoder = get_encoder()
    if encoder is None:
        return None

    # 캐시 확인
    page_hash = hashlib.md5(
        json.dumps([p["slug"] + p["body"][:200] for p in pages], sort_keys=True).encode()
    ).hexdigest()

    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "rb") as f:
                cached = pickle.load(f)
            if cached.get("hash") == page_hash:
                return cached["embeddings"]
        except Exception:
            pass

    # 임베딩 계산
    texts = [f"{p['title']}: {p['body'][:1000]}" for p in pages]
    try:
        embeddings = encoder.encode(texts, show_progress_bar=False).tolist()
    except Exception as e:
        print(f"[wiki_rag] Embedding failed: {e}", flush=True)
        return None

    # 캐시 저장
    try:
        with open(CACHE_FILE, "wb") as f:
            pickle.dump({"hash": page_hash, "embeddings": embeddings}, f)
    except Exception:
        pass

    return embeddings

def cosine_similarity(a: list, b: list) -> float:
    dot = sum(ai * bi for ai, bi in zip(a, b))
    na = math.sqrt(sum(ai * ai for ai in a))
    nb = math.sqrt(sum(bi * bi for bi in b))
    return dot / (na * nb + 1e-10)

# ── Hybrid Search ────────────────────────────────

def hybrid_search(query: str, top_k: int = 5, bm25_weight: float = 0.4, vec_weight: float = 0.6) -> list:
    """
    BM25 + Vector 하이브리드 검색
    - bm25_weight: BM25 점수 가중치 (0~1)
    - vec_weight: 벡터 유사도 가중치 (0~1)
    """
    pages = get_all_page_texts()
    if not pages:
        return []

    # BM25 점수 계산
    idf, avg_dl = build_idf(pages)
    query_tokens = tokenize(query)
    bm25_scores = []
    for p in pages:
        doc_tokens = tokenize(p["body"])
        score = compute_bm25_score(query_tokens, doc_tokens, idf, avg_dl)
        bm25_scores.append(score)

    # BM25 정규화
    max_bm25 = max(bm25_scores) if max(bm25_scores) > 0 else 1.0
    bm25_scores = [s / max_bm25 for s in bm25_scores]

    # 벡터 유사도 계산
    vec_scores = [0.0] * len(pages)
    embeddings = compute_embeddings(pages)
    if embeddings:
        query_emb = compute_embeddings([{"slug": "_query", "title": query, "body": query}])
        if query_emb:
            for i in range(len(pages)):
                vec_scores[i] = cosine_similarity(query_emb[0], embeddings[i])

    # 하이브리드 점수
    combined = []
    for i, p in enumerate(pages):
        score = bm25_weight * bm25_scores[i] + vec_weight * vec_scores[i]
        if score > 0:
            combined.append((score, p))

    combined.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in combined[:top_k]]

# ── Search (backward compat) ─────────────────────

def search_relevant_pages(query: str, top_k: int = 5) -> list:
    """BM25 검색 (기존 호환성)"""
    return hybrid_search(query, top_k, bm25_weight=1.0, vec_weight=0.0)

def semantic_search(query: str, top_k: int = 5) -> list:
    """벡터 검색 전용"""
    return hybrid_search(query, top_k, bm25_weight=0.0, vec_weight=1.0)

# ── LLM Call ─────────────────────────────────────

def call_llm(system_prompt: str, user_message: str, model: str = None) -> str:
    """OpenRouter LLM 호출"""
    api_key = OPENROUTER_API_KEY
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
        config_path = Path.home() / ".hermes" / "config.yaml"
        if config_path.exists():
            import yaml
            with open(config_path) as f:
                config = yaml.safe_load(f)
            providers = config.get("providers", {})
            for name, p in providers.items():
                if "openrouter" in name.lower():
                    api_key = p.get("api_key", "")

    if not api_key:
        raise ValueError("OpenRouter API key not found")

    model_name = model or DEFAULT_MODEL
    if not model_name.startswith("openrouter/"):
        model_name = f"openrouter/{model_name}"

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "max_tokens": 1024,
        "temperature": 0.3,
    }

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/bearj/llm-wiki",
            "X-Title": "LLM Wiki",
        },
        method="POST",
    )

    resp = urllib.request.urlopen(req, timeout=60)
    result = json.loads(resp.read())
    return result["choices"][0]["message"]["content"].strip()

# ── RAG Query ────────────────────────────────────

def query_wiki(question: str, model: str = None, use_hybrid: bool = True) -> dict:
    """위키 기반 질의응답 (하이브리드 RAG)"""
    result = {
        "question": question,
        "answer": "",
        "sources": [],
        "status": "error",
    }

    if use_hybrid:
        relevant = hybrid_search(question, top_k=5)
    else:
        relevant = search_relevant_pages(question, top_k=5)

    if not relevant:
        result["answer"] = "위키에서 관련 정보를 찾을 수 없습니다."
        result["status"] = "no_data"
        return result

    context_parts = []
    for i, p in enumerate(relevant, 1):
        context_parts.append(f"[출처 {i}] {p['title']}\n{p['body'][:1500]}")
        result["sources"].append({
            "slug": p["slug"],
            "title": p["title"],
        })

    context = "\n\n---\n\n".join(context_parts)

    system_prompt = f"""당신은 개인 위키 기반 질의응답 어시스턴트입니다.
아래 위키 내용을 기반으로 질문에 정확하게 답하세요.

규칙:
- 위키에 없는 내용은 "위키에 없는 정보입니다"라고 말하세요
- 답변은 한국어로 하세요
- 출처를 명시하세요 (출처: [페이지 제목])
- 간결하고 명확하게 답하세요
- 코드 예제는 ``` ``` 로 감싸세요

=== 위키 내용 ===
{context}
=== 위키 내용 끝 ==="""

    try:
        answer = call_llm(system_prompt, question, model)
        result["answer"] = answer
        result["status"] = "ok"
    except Exception as e:
        result["answer"] = f"LLM 호출 실패: {e}"
        result["status"] = "llm_error"

    return result

# ── Summarize ────────────────────────────────────

def summarize_content(content: str, title: str = "", model: str = None) -> dict:
    """LLM 콘텐츠 요약"""
    result = {"title": title, "summary": "", "key_points": [], "tags": [], "status": "error"}

    if not content or len(content) < 50:
        result["summary"] = "요약할 콘텐츠가 너무 짧습니다."
        result["status"] = "too_short"
        return result

    system_prompt = """당신은 텍스트 요약 전문가입니다.
주어진 콘텐츠를 요약하고 핵심 포인트와 태그를 추출하세요.

출력 형식 (JSON):
{
  "summary": "2-3문장 요약",
  "key_points": ["핵심1", "핵심2", "핵심3"],
  "tags": ["태그1", "태그2"]
}

규칙:
- 요약은 2-3문장으로 간결하게
- 핵심 포인트는 3-5개
- 태그는 3-5개 (ai-ml, programming, research, business, science, history, personal 등)
- 반드시 JSON 형식으로 출력"""

    try:
        raw = call_llm(system_prompt, f"제목: {title}\n\n{content[:4000]}", model)
        json_match = re.search(r"\{.*\}", raw, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
            result["summary"] = parsed.get("summary", raw[:500])
            result["key_points"] = parsed.get("key_points", [])
            result["tags"] = parsed.get("tags", [])
        else:
            result["summary"] = raw[:500]
        result["status"] = "ok"
    except Exception as e:
        result["summary"] = f"요약 실패: {e}"
        result["status"] = "error"

    return result

# ── Related Pages (Graph-based + Vector) ─────────

def get_related_pages(slug: str, top_k: int = 5) -> list:
    """그래프 + 벡터 기반 연관 페이지 추천"""
    target_page = None
    for d in ALL_DIRS:
        p = d / f"{slug}.md"
        if p.exists():
            target_page = p
            break

    if not target_page:
        return []

    target_content = target_page.read_text(encoding="utf-8")
    target_body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", target_content, flags=re.DOTALL)
    target_links = set(re.findall(r'\[\[([\w\- ]+)\]\]', target_content))
    target_title = target_page.stem

    candidates = []
    for d in ALL_DIRS:
        for f in d.glob("*.md"):
            if f.stem == slug:
                continue

            content = f.read_text(encoding="utf-8")
            body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
            links = set(re.findall(r'\[\[([\w\- ]+)\]\]', content))

            score = 0.0
            common_links = target_links & links
            score += len(common_links) * 3.0

            f_slug_norm = re.sub(r"[^\w\-]", "-", f.stem.lower())
            if f_slug_norm in [re.sub(r"[^\w\-]", "-", l.lower()) for l in target_links]:
                score += 5.0
            if target_title in links:
                score += 5.0

            target_tags = set(re.findall(r"tags:\s*\[([^\]]+)\]", target_content))
            f_tags = set(re.findall(r"tags:\s*\[([^\]]+)\]", content))
            if target_tags and f_tags:
                score += len(target_tags & f_tags) * 2.0

            target_tokens = set(tokenize(target_body))
            f_tokens = set(tokenize(body))
            if target_tokens and f_tokens:
                jaccard = len(target_tokens & f_tokens) / len(target_tokens | f_tokens)
                score += jaccard * 4.0

            if f.parent == target_page.parent:
                score += 1.0

            if score > 0:
                title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else f.stem
                candidates.append({
                    "slug": f.stem,
                    "title": title,
                    "score": round(score, 2),
                    "common_links": list(common_links)[:3],
                })

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:top_k]

# ── CLI ──────────────────────────────────────────

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "query":
        q = " ".join(sys.argv[2:])
        r = query_wiki(q)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "hybrid":
        q = " ".join(sys.argv[2:])
        r = hybrid_search(q)
        print("=== Hybrid Search Results ===")
        for p in r:
            print(f"  - {p['title']} ({p['slug']})")
    elif len(sys.argv) > 1 and sys.argv[1] == "semantic":
        q = " ".join(sys.argv[2:])
        r = semantic_search(q)
        print("=== Semantic Search Results ===")
        for p in r:
            print(f"  - {p['title']} ({p['slug']})")
    elif len(sys.argv) > 1 and sys.argv[1] == "related":
        slug = sys.argv[2] if len(sys.argv) > 2 else ""
        r = get_related_pages(slug)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "summarize":
        content = " ".join(sys.argv[2:])
        r = summarize_content(content)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print("Usage:")
        print("  wiki_rag.py query <question>        # RAG 질의")
        print("  wiki_rag.py hybrid <query>           # 하이브리드 검색")
        print("  wiki_rag.py semantic <query>         # 의미 검색")
        print("  wiki_rag.py related <slug>           # 연관 페이지")
        print("  wiki_rag.py summarize <text>         # 요약")

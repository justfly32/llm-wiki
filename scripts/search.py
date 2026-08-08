#!/usr/bin/env python3
"""
LLM Wiki — Search (v2, Glean 형태)
====================================
Hermes 작업 결과물 인덱스 검색 + LLM RAG 답변.

사용법:
  python3 search.py "로또 필터 재조정"          # FTS5 검색 + RAG 답변
  python3 search.py --raw "카드뉴스 SEO"        # 원본 검색 결과만 (LLM 없이)
  python3 search.py --top 10 "..."             # 결과 수 지정
  python3 search.py --root projects "..."      # 루트 필터
  python3 search.py --type doc "..."           # 유형 필터
"""
import os
import sys
import json
import sqlite3
import argparse
import urllib.request
from pathlib import Path

INDEX_DB = Path.home() / "wiki" / "index.db"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = os.environ.get("LLM_WIKI_MODEL", "deepseek/deepseek-chat-v3-0324")

def search_fts(query: str, top_k: int = 5, root: str = None, ftype: str = None):
    """FTS5 검색"""
    conn = sqlite3.connect(INDEX_DB)
    # FTS5 MATCH 쿼리 구성
    terms = [t for t in query.split() if t]
    match_q = " OR ".join(f'"{t}"*' for t in terms) if terms else '"*"'
    sql = """
        SELECT f.path, f.rel, f.root, f.type, f.size, f.mtime,
               snippet(files_fts, 4, '⟪', '⟫', '…', 12) AS snip
        FROM files_fts
        JOIN files f ON f.path = files_fts.path
        WHERE files_fts MATCH ?
    """
    params = [match_q]
    if root:
        sql += " AND f.root = ?"
        params.append(root)
    if ftype:
        sql += " AND f.type = ?"
        params.append(ftype)
    sql += " ORDER BY bm25(files_fts) LIMIT ?"
    params.append(top_k)
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return rows

def format_results(rows):
    """검색 결과 포맷팅"""
    lines = []
    for i, (path, rel, root, ftype, size, mtime, snip) in enumerate(rows, 1):
        mtime_s = __import__("datetime").datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
        lines.append(f"[{i}] ({root}/{ftype}) {rel}")
        lines.append(f"    📍 {path}")
        lines.append(f"    🕐 {mtime_s} | {size/1024:.0f}KB")
        if snip:
            lines.append(f"    ⟪ {snip} ⟫")
        lines.append("")
    return "\n".join(lines)

def build_context(rows):
    """RAG용 컨텍스트 구성"""
    parts = []
    for i, (path, rel, root, ftype, size, mtime, snip) in enumerate(rows, 1):
        # 상위 3개 파일은 전체 내용 일부 포함
        if i <= 3:
            conn = sqlite3.connect(INDEX_DB)
            row = conn.execute("SELECT content FROM files WHERE path=?", (path,)).fetchone()
            conn.close()
            content = (row[0] if row else "")[:4000]
            parts.append(f"### [{i}] {rel} ({root}/{ftype})\n경로: {path}\n{content}")
        else:
            parts.append(f"### [{i}] {rel} ({root}/{ftype})\n경로: {path}")
    return "\n\n---\n\n".join(parts)

def call_llm(system_prompt: str, user_message: str) -> str:
    """OpenRouter LLM 호출"""
    if not OPENROUTER_API_KEY:
        return "(OpenRouter API 키 없음 — --raw 모드로 검색 결과만 확인하세요)"
    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"(LLM 호출 실패: {e})"

def main():
    parser = argparse.ArgumentParser(description="LLM Wiki 검색")
    parser.add_argument("query", nargs="+", help="검색어")
    parser.add_argument("--raw", action="store_true", help="원본 검색 결과만 (RAG 없이)")
    parser.add_argument("--top", type=int, default=5, help="결과 수 (기본 5)")
    parser.add_argument("--root", choices=["projects", "hermes", "documents"], help="루트 필터")
    parser.add_argument("--type", choices=["code", "doc", "config", "web", "pdf", "data", "image"], help="유형 필터")
    args = parser.parse_args()

    query = " ".join(args.query)
    rows = search_fts(query, top_k=args.top, root=args.root, ftype=args.type)

    if not rows:
        print(f"🔍 '{query}' 검색 결과 없음")
        return

    if args.raw:
        print(f"🔍 '{query}' — {len(rows)}개 결과")
        print(format_results(rows))
        return

    # RAG 답변
    context = build_context(rows)
    system = (
        "당신은 Hermes Agent의 작업 결과물 인덱스에서 검색된 자료를 바탕으로 답변하는 "
        "내부 지식 비서입니다. 검색된 파일 내용에서 근거를 찾아 답변하고, 출처 파일 경로를 "
        "함께 제시하세요. 검색 결과에 없는 내용은 추측하지 말고 '인덱스에서 찾지 못했습니다'라고 "
        "명시하세요. 답변은 한국어로."
    )
    user = f"질문: {query}\n\n--- 검색된 자료 ---\n{context}"

    print(f"🔍 '{query}' — {len(rows)}개 결과 기반 답변\n")
    print("=" * 60)
    print(call_llm(system, user))
    print("=" * 60)
    print("\n📄 검색 결과:")
    print(format_results(rows))

if __name__ == "__main__":
    main()

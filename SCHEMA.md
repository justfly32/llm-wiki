# LLM Wiki — Schema (v2, 2026-08-09)

> **목적:** Hermes Agent가 만들어낸 모든 작업 결과물을 인덱싱하고 검색 가능하게 하는
> 내부 검색 시스템 (Glean 형태). "LLM이 한 모든 작업을 쉽게 검색하고 찾아갈 수 있게"가 핵심 목표.

## 도메인 정의

이 위키는 **외부 콘텐츠 수집(뉴스/RSS/arXiv)이 아니라, Hermes가 생성한 작업 산출물의 인덱스**다.

- ❌ 외부 기사, 뉴스, 논문 요약 → 저장 금지
- ✅ ~/projects, ~/.hermes, ~/documents 내 작업 파일 → 인덱싱 대상
- ✅ 작업 변경 내역 (daily) → concepts/daily/

## 인덱싱 대상

| 루트 | 포함 | 제외 |
|------|------|------|
| `~/projects/` | 모든 프로젝트 (코드, 문서, 설정) | node_modules, .git, .venv, dist, build, .next, __pycache__ |
| `~/.hermes/` | scripts, skills, memories, cron, sessions, kanban 등 | cache, logs, node, lsp, pastes, sandboxes, state.db 등 |
| `~/documents/` | 작업 문서 | — |

## 인덱스 구조

- **DB:** `~/wiki/index.db` (SQLite FTS5)
- **테이블:** `files(path TEXT, rel TEXT, root TEXT, type TEXT, size INT, mtime REAL, content TEXT)` + FTS5 인덱스
- **갱신:** mtime 기반 증분 — `build_index.py`가 마지막 인덱스 시각 이후 변경 파일만 재인덱싱
- **검색:** `search.py` — FTS5 키워드 검색 + LLM RAG 답변

## 위키 페이지 규칙

- `concepts/daily/YYYY-MM-DD.md` — 매일 작업 요약 (크론이 자동 생성)
- `concepts/knowledge/` — 장기 보관 가치 있는 지식/가이드
- `concepts/projects/` — 프로젝트 계획/스펙
- `concepts/learnings/` — 실패 패턴, 개선점
- `entities/` — 사람/조직/제품 (필요시)
- 프론트매터 필수: `title, created, updated, type, tags, links`
- 최소 1개 이상 outbound wikilink (`[[index]]` 포함 가능)

## 검색 사용법

```bash
python3 ~/wiki/scripts/search.py "질문"          # FTS5 + RAG 답변
python3 ~/wiki/scripts/search.py --raw "키워드"  # 원본 검색 결과만
python3 ~/wiki/scripts/build_index.py             # 전체 인덱싱 (증분)
```

## 보안 원칙 (Phase 3 확장 대비)

- 인덱스는 로컬 SQLite에만 저장 (클라우드 경유 금지)
- 사내 확장 시: 사용자/그룹 → ACL → 검색 결과 필터링 (Glean Permission Mirroring)

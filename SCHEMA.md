# Wiki Schema

## Domain
Personal knowledge base for Bear J + Agent. Covers project records, research results, learnings, and daily work logs.

## Structure

```
wiki/
├── SCHEMA.md           # This file
├── index.md            # Content catalog
├── log.md              # Change history
├── concepts/           # Categorized knowledge
│   ├── projects/       # Project plans, specs, drafts
│   ├── knowledge/      # Research, docs, guides, reports
│   ├── learnings/      # Failure patterns, feedback, improvements
│   └── daily/          # Daily work logs (chronological)
├── raw/
│   ├── articles/       # Original ingested articles
│   └── archive/        # Deprecated papers, news, external content
├── entities/           # Entity pages (people, orgs, tools)
├── comparisons/        # Side-by-side analyses
└── queries/            # Filed query results
```

## Conventions
- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Frontmatter `links:` field required — list of `[[slug|description]]`
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: project | knowledge | learning | daily | entity | concept | comparison | query
tags: [from taxonomy below]
links: [[other-page-slug|description]]
# Optional:
confidence: high | medium | low
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy
- **Domains:** ai-ml, programming, research, business, tools, agent, tax, investment
- **Types:** project, report, guide, analysis, workflow, command
- **Methods:** automation, orchestration, research, documentation
- **Meta:** comparison, timeline, learning, how-to

## Page Rules
- **Create a page** when: project completed, research conducted, learning captured
- **Link every page** to at least 2 related pages via `links:` frontmatter
- **Daily pages** link to previous/next day (chronological chain)
- **Project pages** link to related knowledge docs and learnings
- **Archive** superseded content to `raw/archive/`

## Update Policy
When new information conflicts:
1. Check dates — newer generally supersedes older
2. If genuinely contradictory, note both with dates and sources
3. Mark in frontmatter: `contradictions: [page-name]`

## 추천글 정리 (User-Recommended Content)

사용자가 링크나 추천글을 올려주면:
1. **요약 작성** — 핵심 개념, 기능, 인사이트를 간결하게 정리
2. **knowledge/ 또는 projects/ 에 저장** — 주제에 맞는 폴더 선택
3. **wikilink 연결** — 관련 기존 페이지와 크로스레퍼런스
4. **index.md 업데이트** — 해당 섹션에 추가
5. **원본 보존** — raw/articles/ 또는 raw/archive/ 에 원본 저장

형식: 위 devbox.md 참고 (frontmatter + 요약 + 표 + 관련 문서)

## 세션 저장 규칙 (Session → Wiki)

세션이 끝나기 전에 다음을 llm-wiki에 기록:

1. **daily/YYYY-MM-DD.md** — 오늘 주요 작업 내역
   - 완료한 작업, 결정된 사항, 핵심 인사이트
   - 이전 날짜 daily와 링크 (prev/next chain)

2. **knowledge/ 업데이트** — 새로 얻은 지식, 리서치 결과
3. **learnings/ 업데이트** — 실패 패턴, 피드백
4. **log.md** — 변경 이력 기록

### 세션 시작 시 로딩 순서
1. MEMORY.md 자동 주입 (시스템)
2. `cd ~/wiki && python3 wiki.py search "최근 작업"` → 최신 daily 확인
3. 필요 시 `concepts/daily/YYYY-MM-DD.md` 읽어서 맥락 파악
4. 과거 상세 필요 시 `session_search(query="키워드")` 로 대화 기록 검색

### 세션 ↔ 위키 연결
- session_search: 대화 기록 검색 (누슨 무엇을 했는지)
- llm-wiki: 지식 + 결과물 저장 (무엇을 알게 됐는지)
- 둘은 독립적이지만, daily/ 가 다리를 놓는 역할

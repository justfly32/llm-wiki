---
title: 개인 사이트 자동화 고도화 (Python + Jinja2 Generator)
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [web, programming, python, javascript, api]
sources: [raw/local/web/plans-site-refinement-2026-06-01.md]
source_file: /Users/bearj/projects/post1/.omo/plans/site-refinement.md
confidence: high
links: [[plans-2026-05-17-html-template-system|HTML Template System 구현 계획]], [[plans-web-terminal-plan|Web Terminal 계획]], [[plans-fix-memories-path|memories 경로 수정]]
---

# 개인 사이트 자동화 고도화 (Python + Jinja2 Generator)

> 📁 원본: `/Users/bearj/projects/post1/.omo/plans/site-refinement.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: web

## 내용

# 개인 사이트 자동화 고도화 (Python + Jinja2 Generator)

## TL;DR

> **Quick Summary**: Hermes agent의 LLM이 직접 HTML을 수정하던 방식을 Python + Jinja2 정적 생성기로 교체하여 데이터-프레젠테이션을 완전 분리하고, GitHub Contribution 스타일 히트맵과 통계 요약을 추가하여 사이트를 더 세련되게 개선
>
> **Deliverables**:
> - `scripts/generate_site.py` — 메인 정적 생성기
> - `templates/base.html` — Jinja2 베이스 템플릿 (모든 정적 섹션 보존)
> - `templates/timeline.html` — 활동 타임라인 템플릿
> - `templates/cron.html` — 크론 작업 템플릿
> - `templates/heatmap.html` — GitHub Contribution 스타일 히트맵
> - `templates/stats.html` — 통계 요약 카드
> - `site_data/activities.json` — 중간 데이터 (디버깅/확장용)
> - `tests/test_parser.py` — 파서 단위테스트
> - `tests/test_generator.py` — 생성기 테스트
> - Hermes cron prompt 교체 (LLM HTML 편집 → Python 실행)
>
> **Estimated Effort**: Medium (4-6시간)
> **Parallel Execution**: YES — 6 waves, 최대 6 concurrent tasks
> **Critical Path**: Task 1 → Task 7 → Task 15 → F1-F4

---

## Context

### Original Request
> "개인 사이트인데 헤르메스 에이전트와 한 일들을 자동으로 업데이트 시키고 있어. 좀 더 세련되게 만들 방안 제안해줘"

### Interview Summary
**Key Discussions**:
- **현재 방식 문제**: Hermes cron (매일 07:00 KST)이 LLM으로 daily_memory 읽고 index.html 직접 수정 → 구조 깨짐 위험, LLM 비용, merge conflict 이력
- **해결 방향**: Python + Jinja2 정적 생성기 도입, 데이터-프레젠테이션 완전 분리
- **전체 한 번에 (Phase 1 + 2)**: 데이터 분리 + 시각화 고도화를 하나의 계획으로
- **데이터 범위**: daily_memories + cron_jobs만 (kanban/세션/로그 제외)
- **디자인**: 현행 HTML5 UP Editorial 유지 + 히트맵/통계 보강
- **히트맵**: GitHub Contribution 스타일 (CSS Grid, 라이브러리 불필요)
- **테스트**: 파서 TDD + 템플릿 test-after + agent QA

**Research Findings**:
- **daily_memories 포맷 불일치**: `다음 할일` vs `다음 할 일` (띄어쓰기 차이), `주요 작업`/`주요 논의`/`진행/논의` 등 다양한 섹션 헤더
- **날짜 파일 누락**: 2026-05-24.md 존재하지 않음 (13개 파일, 5/12-5/25)
- **cron_jobs.json**: 8개 job 중 6개 enabled, 2개 disabled
- **Git 히스토리**: 이미 1회 merge conflict + 1회 라인번호 오염(LLM 실수) 발생
- **GitHub remote**: `github.com:justfly32/post1.git`
- **기존 cron prompt**: ~2000자 LLM 프롬프트가 HTML 직접 수정 (no_agent: false)

### Metis Review
**Identified Gaps** (addressed):
- **SECTION_ALIASES 필요**: `다음 할일`/`다음 할 일` 등 변종 헤더 매핑
- **날짜 누락 처리**: 없는 daily_memory 파일 → skip (crash 금지)
- **enabled 필터링**: cron_jobs.json에서 enabled: true만 표시
- **Idempotency**: 타임스탬프 제외 동일 입력 → 동일 출력 (불필요한 git diff 방지)
- **Markdown-to-HTML**: daily_memory 내 목록/볼드 텍스트 변환 필요
- **Race condition 방지**: 이전 크론 실행중 새 실행 금지
- **정적 섹션 보존**: intro/에이전트 헤르/사용자 정보/메모리 시스템/CTA/footer는 템플릿에 하드코딩

---

## Work Objectives

### Core Objective
Hermes agent의 활동 내역(index.html) 자동 업데이트 방식을 Python + Jinja2 정적 생성기로 전환하고 GitHub Contribution 스타일 히트맵과 통계 요약을 추가하여 사이트를 더 세련되게 개선한다.

### Concrete Deliverables
1. `scripts/generate_site.py` — 메인 생성기 (idempotent)
2. `templates/` — Jinja2 템플릿 5개 (base, timeline, cron, heatmap, stats)
3. `site_data/activities.json` — 중간 데이터 레이어
4. `tests/test_parser.py` + `tests/test_generator.py` — 테스트
5. Cron job prompt 교체 — LLM HTML 편집 → Python 실행
6. 활동 히트맵 — GitHub Contribution 스타일 (CSS Grid)
7. 통계 요약 카드 — 주간 활동 수, 연속 활동일, 활성 크론 수

### Definition of Done
- [ ] `python3 scripts/generate_site.py` 실행 → `index.html` 생성됨 (기존 디자인 유지)
- [ ] `python3 -m pytest 

...(내용 생략)...

---
title: 개인 사이트 (Personal Sites) 폴더 내역
created: 2026-08-09
updated: 2026-08-09
type: projects
tags: [personal-site, portfolio, github-pages, post1, justfly32]
links: [[index]]
---

# 개인 사이트 (Personal Sites) — 폴더 내역 및 중복 방지 가이드

> **목적:** Bear J의 개인 사이트 관련 폴더가 여럿 존재하여 중복 생성 위험이 있어,
> 현재 폴더 상태와 역할을 명확히 기록한다. **새 폴더를 만들기 전에 반드시 이 문서를 확인할 것.**

## 현재 존재하는 폴더 3개 (2026-08-09 기준)

### 1. `~/projects/justfly32.github.io` — 메인 포트폴리오 (운영 중) ⭐
| 항목 | 내용 |
|------|------|
| 위치 | `~/projects/justfly32.github.io/` (2026-08-09 home 직속 → projects로 이동) |
| GitHub | `justfly32/justfly32.github.io` (SSH) |
| URL | https://justfly32.github.io (HTTP 200) |
| 성격 | **크리에이티브 개발자 포트폴리오** — Hero/About/Skills/Projects/Simpli GIF/Timeline/Contact |
| 갱신 방식 | **수동** (index.html 직접 편집 → git commit/push) |
| 최근 갱신 | 2026-08-09 — 2026.07~08 타임라인·프로젝트 추가 (커밋 `0a9ad94`) |
| 주의 | **post1과 다른 사이트** — 여기는 포트폴리오, post1은 활동 로그 |

### 2. `~/projects/post1` — 활동 로그 사이트 (운영 중) ⭐
| 항목 | 내용 |
|------|------|
| 위치 | `~/projects/post1/` |
| GitHub | `justfly32/post1` (SSH) |
| URL | https://justfly32.github.io/post1/ (301 → `/post1/`) |
| 성격 | **개인 활동 로그** — Activities/Cron jobs 통계 자동 생성 사이트 |
| 갱신 방식 | **자동** — 매일 06:00 크론 (`Update personal site timestamp`) → `scripts/generate_site.py` 실행 → GitHub Pages 배포 |
| 최근 커밋 | 2026-08-09 `aef96c4` |
| 핵심 스크립트 | `scripts/generate_site.py` (Jinja2 템플릿), `parser.py`, `cron_reader.py`, `models.py` |
| 입력 데이터 | `~/.hermes/memories/daily_memories/` + `~/.hermes/cron/jobs.json` |

### 3. `~/projects/personal-site` — 구버전 프로토타입 (비운영, 보존만) 📦
| 항목 | 내용 |
|------|------|
| 위치 | `~/projects/personal-site/` |
| GitHub | **없음** (git repo 아님, 로컬 전용) |
| 성격 | post1의 **초기 프로토타입** (2026-05-30 생성) |
| 상태 | **비운영** — post1(2026-06-11)로 대체됨 |
| 삭제 금지 | 히스토리 보존용으로 유지하되, **수정/재사용 금지** |
| 스크립트 | post1과 동일 구조 (`generate_site.py`, `parser.py` 등) — 차이는 index.html만 |

## 진화 관계 (중복 방지 핵심)

```
personal-site (2026-05-30, 프로토타입 — 보존만)
      ↓ 진화
post1 (2026-06-11, 활동 로그 — 운영 중)
justfly32.github.io (2026-06-13, 포트폴리오 — 운영 중)
```

**규칙:**
- ❌ `personal-site`, `post1`, `justfly32.github.io` 이름의 새 폴더를 만들지 말 것
- ❌ personal-site를 post1로 "이동/병합" 시도하지 말 것 (보존용)
- ✅ 모든 프로젝트 폴더는 `~/projects/` 통일 (2026-08-09 justfly32.github.io 이동 완료 — home 직속 금지)
- ✅ 새 개인 사이트 작업은 **기존 폴더 수정** 또는 **이 문서에 새 항목 추가 후** 진행
- ✅ 배포는 반드시 GitHub Pages (각 repo의 main 브랜치 push)

## 관련 파일

- `~/.hermes/skills/design-to-code/references/portfolio-design.md` — 포트폴리오 디자인 레퍼런스
- `~/.hermes/skills/web/github-pages-portfolio/SKILL.md` — GitHub Pages 배포 스킬
- `~/.hermes/memories/daily_memories/` — 사이트 데이터 원천 (post1)
- `~/.hermes/cron/jobs.json` — 크론 목록 (post1 표시용)

## 출처

- 실제 폴더 stat/`git remote`/커밋 로그 직접 확인 (2026-08-09)
- [[index]]

---
title: 프로젝트 레지스트리 (전체 폴더 현황)
created: 2026-08-09
updated: 2026-08-09
type: projects
tags: [registry, projects, folder-map, 중복방지]
links: [[index]]
---

# 프로젝트 레지스트리 — 전체 폴더 현황

> **목적:** 새 코딩 작업 시작 전 반드시 이 문서를 확인해 폴더 중복 생성과 위치 혼란을 방지한다.
> 자동 생성: `python3 ~/wiki/scripts/generate_project_registry.py` (갱신 시 재실행)
> Last updated: 2026-08-09

## 규칙 (중복 방지)

- ❌ 같은 역할의 폴더가 이미 있으면 새로 만들지 말 것 (아래 목록에서 유사 항목 검색)
- ❌ 프로젝트 폴더 위치: `~/projects/` 통일 (개인 사이트만 `~/justfly32.github.io`)
- ✅ 새 프로젝트는 `~/projects/<kebab-case>` 로 생성 후 이 문서를 갱신
- ✅ 비슷한 게 보이면 기존 폴더 확장 또는 이 문서에 병합/분리 사유 기록

## 🟢 Git 프로젝트 (배포/히스토리 있음)

| 폴더 | 설명 | remote | 최근 커밋 |
|------|------|--------|----------|
| `post1` | - | justfly32/post1 | 2026-08-09 |
| `MI8_project` | 절대 규칙: Root 디렉토리를 직접 수정하거나 파일을 생성하지 마세요. | justfly32/MI8_project | 2026-08-04 |
| `kanban-board` | / 기능 / 설명 / | justfly32/kanban-board | 2026-06-29 |
| `dev-commercialization-helper` | 개발 상품화 도우미 — Next.js + Supabase + Stripe SaaS 보일러플레이트 | justfly32/dev-commercialization-helper | 2026-06-28 |
| `code-edu-lab` | 이 프로젝트는 로컬 데이터베이스에 접속하여 대시보드를 만드는 방법을 교육하기 위해 설계되었습니다. | justfly32/code-edu-lab | 2026-06-27 |
| `code-tutorial` | git clone https://github.com/justfly32/code-tutorial.git | justfly32/code-tutorial | 2026-06-26 |
| `elderly-health` | This is a [Next.js](https://nextjs.org) project bootstrapped with [create-next-app](https://nextjs.org/docs/app/api-refe | - | 2026-06-26 |
| `elderly-health-care` | 부산 지역 노인을 위한 통합 건강관리 � 애플리케이션 | justfly32/elderly-health-care | 2026-06-26 |
| `llm-core-lab` | Interactive educational visualizer for understanding how LLM models work internally. | justfly32/llm-core-lab | 2026-06-25 |
| `network-topology` | 네트워크 토폴로지 시각화 + 스케줄러 + 알림 시스템 | justfly32/network-topology | 2026-06-25 |
| `headroom` | <div align="center"<pre | chopratejas/headroom | 2026-06-13 |

## 📦 로컬 전용 (git 없음)

| 폴더 | 설명 | 파일 수 |
|------|------|--------|
| `HTML_Viewer` | 분할 화면 HTML 편집기 — 실시간 미리보기 및 PDF/DOCX/PPTX 내보내기 지원. | 6 |
| `PPT_Generator` | - | 25 |
| `Univ_Pass` | 대학 입시 분석 시스템 — 수시 합격 확률 분석 도구 | 50 |
| `ai_business_report` | - | 5 |
| `animation-maker` | - | 4 |
| `best-practice` | - | 1 |
| `claude-cowork-guide` | - | 1 |
| `code-express` | - | 0 |
| `hermes_ops` | - | 148 |
| `html2pptx` | HTML 디자인을 PPTX로 최대한 보존 변환하는 도구. | 15 |
| `internet-checker` | SKB, KT, LGU+ 통신 3사의 초고속인터넷 주소별 서비스 가용성을 한 번에 조회하는 도구입니다. | 15 |
| `kakao-hybrid-adapter` | [GPTers 글 «카톡 매크로 시대 끝? …»](https://www.gpters.org/dev/post/kakaotalk-macro-era-how-lEVSOKmyNxOqCtI)에서 다룬 아키텍처를 코드로 옮긴 예 | 22 |
| `lotto-predictor` | 1231회차 전체 데이터 기반 번호별 확률 학습 예측 모델. | 11 |
| `openclaw-token-dashboard` | - | 33 |
| `orchestration-workflow` | - | 1 |
| `personal-site` | - | 90 |
| `phone-report` | - | 8 |
| `simple-anim-maker` | - | 0 |
| `simpli-gif-maker` | 텍스트 설명을 받아 간단한 졸라맨 GIF 애니메이션을 생성합니다. | 4235 |
| `simpli-video-maker` | - | 2 |
| `stickman-gif-creator` | 졸라맨과 같은 stickman 이미지를 기반으로 설명을 받아 GIF 애니메이션을 자동 생성하는 프로그램. | 1933 |
| `system-dashboard` | - | 24 |
| `system-monitor-dashboard` | This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules. | 19 |
| `useful-sites` | - | 1 |
| `windfriend-archive` | - | 52237 |

## 중복 유사 후보 (확인 필요)

아래 이름이 비슷한 그룹은 병합/보존 판단이 필요할 수 있다.

- **건강관리**: `elderly-health`, `elderly-health-care`
- **GIF/애니메이션**: `simpli-gif-maker`, `stickman-gif-creator`, `simple-anim-maker`, `animation-maker`, `simpli-video-maker`
- **대시보드**: `system-dashboard`, `system-monitor-dashboard`, `openclaw-token-dashboard`
- **PPT/문서**: `html2pptx`, `PPT_Generator`
- **개인 사이트**: `personal-site`, `post1`
- **코딩 교육**: `code-edu-lab`, `code-tutorial`, `code-express`

## 관련

- [[personal-sites]] — 개인 사이트 3개 폴더 상세
- [[index]]

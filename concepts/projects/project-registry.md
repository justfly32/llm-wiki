---
title: 프로젝트 레지스트리 (전체 폴더 현황)
created: 2026-08-29
updated: 2026-08-29
type: projects
tags: [registry, projects, folder-map, 중복방지]
links: [[index]]
---

# 프로젝트 레지스트리 — 전체 폴더 현황

> **목적:** 새 코딩 작업 시작 전 반드시 이 문서를 확인해 폴더 중복 생성과 위치 혼란을 방지한다.
> 자동 생성: `python3 ~/wiki/scripts/generate_project_registry.py` (갱신 시 재실행)
> Last updated: 2026-08-29

## 규칙 (중복 방지)

- ❌ 같은 역할의 폴더가 이미 있으면 새로 만들지 말 것 (아래 목록에서 유사 항목 검색)
- ❌ 프로젝트 폴더 위치: `~/projects/` 통일 (개인 사이트 포함, 2026-08-09 justfly32.github.io 이동 완료)
- ✅ 새 프로젝트는 `~/projects/<kebab-case>` 로 생성 후 이 문서를 갱신
- ✅ 비슷한 게 보이면 기존 폴더 확장 또는 이 문서에 병합/분리 사유 기록
- ✅ 중복 그룹에서 **✅ 정본**만 운영, 비정본은 삭제 (2026-08-09 3개 그룹 7개 폴더 휴지통 이동 완료)

## 정본 표시

- **✅ 정본** = 운영 중인 최신 폴더 (새 작업은 여기서 진행)
- **🗑️ 삭제된 비정본** = 구버전/빈 껍데기 → `~/.Trash/hermes-removed-20260809/` 보관 (아래 목록 참조)

## 🟢 Git 프로젝트 (배포/히스토리 있음)

| 폴더 | 설명 | remote | 최근 커밋 |
|------|------|--------|----------|
| `  post1` | - | justfly32/post1 | 2026-08-28 |
| `  MI8_project` | 절대 규칙: Root 디렉토리를 직접 수정하거나 파일을 생성하지 마세요. | justfly32/MI8_project | 2026-08-23 |
| `  auto-trading` | 한국 주식 자동매매 — Mock 가상매매 검증 → NH투자증권 모의투자 → 실전 전환 완료 (500만원). | - | 2026-08-20 |
| `✅ enterprise-search` | 암호화(DRM) 저장 파일 → 권한 기반 인덱싱 → 하이브리드 검색 → RAG 답변 | justfly32/enterprise-search | 2026-08-09 |
| `  justfly32.github.io` | 크리에이티브 개발자 Bear J의 개인 포트폴리오 사이트입니다. | justfly32/justfly32.github.io | 2026-08-09 |
| `  slide-master` | [![Output](https://img.shields.io/badge/output-native%20PPTX%20(DrawingML)-217346)](faq) | byungjunjang/slide-master | 2026-08-04 |
| `  kanban-board` | / 기능 / 설명 / | justfly32/kanban-board | 2026-06-29 |
| `  dev-commercialization-helper` | 개발 상품화 도우미 — Next.js + Supabase + Stripe SaaS 보일러플레이트 | justfly32/dev-commercialization-helper | 2026-06-28 |
| `✅ code-edu-lab` | 이 프로젝트는 로컬 데이터베이스에 접속하여 대시보드를 만드는 방법을 교육하기 위해 설계되었습니다. | justfly32/code-edu-lab | 2026-06-27 |
| `✅ elderly-health-care` | 부산 지역 노인을 위한 통합 건강관리 � 애플리케이션 | justfly32/elderly-health-care | 2026-06-26 |
| `  llm-core-lab` | Interactive educational visualizer for understanding how LLM models work internally. | justfly32/llm-core-lab | 2026-06-25 |
| `  network-topology` | 네트워크 토폴로지 시각화 + 스케줄러 + 알림 시스템 | justfly32/network-topology | 2026-06-25 |
| `  headroom` | <div align="center"<pre | chopratejas/headroom | 2026-06-13 |

## 📦 로컬 전용 (git 없음)

| 폴더 | 설명 | 파일 수 |
|------|------|--------|
| `  HTML_Viewer` | 분할 화면 HTML 편집기 — 실시간 미리보기 및 PDF/DOCX/PPTX 내보내기 지원. | 6 |
| `  PPT_Generator` | - | 25 |
| `  Univ_Pass` | 대학 입시 분석 시스템 — 수시 합격 확률 분석 도구 | 50 |
| `  ai_business_report` | - | 5 |
| `  auto-trading-research` | - | 2 |
| `  best-practice` | - | 1 |
| `  claude-cowork-guide` | - | 1 |
| `  hermes_ops` | - | 148 |
| `  html2pptx` | HTML 디자인을 PPTX로 최대한 보존 변환하는 도구. | 15 |
| `  internet-checker` | SKB, KT, LGU+ 통신 3사의 초고속인터넷 주소별 서비스 가용성을 한 번에 조회하는 도구입니다. | 15 |
| `  kakao-hybrid-adapter` | [GPTers 글 «카톡 매크로 시대 끝? …»](https://www.gpters.org/dev/post/kakaotalk-macro-era-how-lEVSOKmyNxOqCtI)에서 다룬 아키텍처를 코드로 옮긴 예 | 22 |
| `  lotto-predictor` | 1231회차 전체 데이터 기반 번호별 확률 학습 예측 모델. | 14 |
| `  orchestration-workflow` | - | 1 |
| `✅ pc-llm-dashboard` | PC 상태 확인 + LLM 사용량 확인 통합 모니터링 대시보드. | 25 |
| `  personal-site` | - | 90 |
| `  phone-report` | - | 8 |
| `✅ simpli-gif-maker` | 텍스트 설명을 받아 간단한 졸라맨 GIF 애니메이션을 생성합니다. | 4232 |
| `  useful-sites` | - | 1 |
| `  windfriend-archive` | - | 52237 |

## 정본/비정본 상세 (2026-08-09 확정 — 최신 것이 정본)

| 폴더 | 상태 | 근거 |
|------|------|------|
| `code-edu-lab` | ✅ 정본 | 코딩 교육 정본 (4스택 9,700파일, 6/27 최신) |
| `elderly-health-care` | ✅ 정본 | 노인 건강관리 정본 (4개 기능 구현, 커밋 f317391) |
| `enterprise-search` | ✅ 정본 | 사내 파일 검색 PoC (DRM 무관 Accessor 추상화 + 권한 ACL + 하이브리드 검색 + RAG, 포트 8091/3001) |
| `pc-llm-dashboard` | ✅ 정본 | PC 상태+LLM 사용량 통합 대시보드 정본 (3종 통합, React19+Vite+Express, 포트 5175/4010) |
| `simpli-gif-maker` | ✅ 정본 | GIF 생성 정본 (Flask+기능 최다 4,239파일, 포트폴리오 서빙 중) |

## 중복 유사 후보 (확인 필요)

아래 이름이 비슷한 그룹은 병합/보존 판단이 필요할 수 있다.

- **PPT/문서**: `html2pptx`, `PPT_Generator`
- **개인 사이트**: `personal-site`, `post1`, `justfly32.github.io`

## 🗑️ 삭제된 비정본 (2026-08-09)

| 폴더 | 사유 |
|------|------|
| `animation-maker` | 4파일 미니멀 버전 |
| `code-express` | node_modules만 있는 빈 폴더 |
| `code-tutorial` | 초기 4파일 버전 (Code Vibe, GitHub 원격에 백업 존재) |
| `elderly-health` | create-next-app 초기 커밋만 있는 빈 껍데기 (git remote 없음) |
| `openclaw-token-dashboard` | 대시보드 구버전 (리팩토링 코드를 pc-llm-dashboard 베이스로 사용) |
| `simple-anim-maker` | 빈 폴더 |
| `simpli-video-maker` | 2파일 미니멀 버전 |
| `stickman-gif-creator` | 6/13 구버전 파이썬 구현 |
| `system-dashboard` | 대시보드 구버전 (pc-llm-dashboard로 통합) |
| `system-monitor-dashboard` | 대시보드 축소판 (시스템 모니터 탭만, pc-llm-dashboard로 통합) |

> 보존 위치: `~/.Trash/hermes-removed-20260809/` (복구 가능)

## 관련

- [[personal-sites]] — 개인 사이트 3개 폴더 상세
- [[index]]

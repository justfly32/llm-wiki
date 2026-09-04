# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-09-05] daily-sync | 인덱스 +20/+71, 레지스트리 34개 폴더 (+1: car-year-lookup), 크론 에러 50건 (조치 필요), 작업 변경 86개
- 인덱스: 신규 20 / 갱신 71 / 총 16,242개 파일 (FTS 15,987, 357.2MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — **신규 로컬 폴더 +1: car-year-lookup** (차량 연식 조회, 10개 파일 변경 감지)
- 크론 에러 50건: card-news-supabase-sync (05:01~05:28, 3분 간격) — 전부 `Error 402: Payment Required`. 전일 타임아웃(09-04)에서 **결제/요금제 문제로 유형 전환** + 3분 간격 무한 반복 루프 = 명백한 반복 패턴(**3건 초과, 조치 필요**). Supabase 대시보드 Billing/Credits 확인 + 연속실패 회로차단 제안
- 작업 변경 86개: MI8_project 52 (카드뉴스 md), car-year-lookup 10 (신규), auto-trading 4, lotto-predictor 2, post1 1 / .hermes 17 / git 커밋 2개 저장소 (post1 8f14fec, memories bf8f97c)
- daily 페이지: concepts/daily/2026-09-05.md 생성

## [2026-09-04] daily-sync | 인덱스 +4393/+3202, 레지스트리 33개 폴더 (변동 없음), 크론 에러 1건, 작업 변경 9069개
- 인덱스: 신규 4393 / 갱신 3202 / 총 16,222개 파일 (FTS 15,967, 356.9MB) — 대부분 hermes-agent 내부 코드(20커밋, schema v30) 반영
- 레지스트리: 33개 폴더 (git 13 / 로컬 20) — 전일 대비 신규 폴더 없음 (post1 커밋 09-03 갱신, web-crawler-work 파일수 14→23)
- 크론 에러 1건: card-news-supabase-sync (05:18) — status.json PUT curl 10초 타임아웃 (상태 정리 단계만 실패, 콘텐츠 발행 정상). 과거 08-24~08-30 반복 이력 재발. 08-30 재시도 래퍼 조치에도 재발 → 타임아웃 상향 + non-fatal 처리 제안
- 작업 변경 9069개: .hermes 7558 (hermes-agent 20커밋), projects 65 (MI8_project 53 카드뉴스 md, web-crawler-work 7, post1 1), git 커밋 3개 저장소 (post1 4b0248e, hermes-agent 20, memories 10a44fe)
- daily 페이지: concepts/daily/2026-09-04.md 생성

## [2026-09-03] daily-sync | 인덱스 +32/+67, 레지스트리 33개 폴더 (+1: web-crawler-work), 크론 에러 1건, 작업 변경 94개
- 인덱스: 신규 32 / 갱신 67 / 총 11,829개 파일 (FTS 11,584, 306.5MB)
- 레지스트리: 33개 폴더 (git 13 / 로컬 20) — **신규 로컬 폴더 +1: web-crawler-work** (부동산 아파트 지도/타일 크롤링, map.html/tiles_SG.json/cl_apt.json)
- 크론 에러 1건: auto-trading-live-daily (14:15) — ZeroDivisionError (live.py:397, 가격 데이터 부족 px=0) / 근본 원인 IGW40023 모의투자 가격 API 미지원. 커밋 d5e9d12로 ZeroDivisionError 방어 반영
- 작업 변경 94개: MI8_project 52 (카드뉴스 md + .published_slugs.txt), web-crawler-work 14 (신규), auto-trading 4, post1 1 / .hermes 23 / git 커밋 3개 저장소 (post1 3652c4a, auto-trading d5e9d12, memories e28019e)
- daily 페이지: concepts/daily/2026-09-03.md 생성

## [2026-09-02] daily-sync | 인덱스 +11/+76, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 81개
- 인덱스: 신규 11 / 갱신 76 / 총 11,797개 파일 (FTS 11,552, 306.2MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건: card-news-supabase-sync (04:52) — curl -X DELETE .status.json 10초 타임아웃 (Storage 정리 단계, 삭제만 실패 / 업로드는 정상)
- 작업 변경 81개: MI8_project 53 (카드뉴스 md 본문 + .published_slugs.txt), auto-trading 7, post1 1 / .hermes 20 / git 커밋 3개 저장소 (post1 2db23c7, auto-trading e3cce6b, memories fe73cc9)
- daily 페이지: concepts/daily/2026-09-02.md 생성

## [2026-09-01] daily-sync | 인덱스 +26/+69, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 87개
- 인덱스: 신규 26 / 갱신 69 / 총 11,786개 파일 (FTS 11,541, 306.0MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync 타임아웃 및 keepalive 이슈 모두 미발생
- 작업 변경 87개: MI8_project 74 (카드뉴스 md 본문 + .published_slugs.txt + .seo.json), auto-trading 4, post1 1 / .hermes 8 / git 커밋 2개 저장소 (post1 5330cb7, memories c010173)
- daily 페이지: concepts/daily/2026-09-01.md 생성

## [2026-08-31] daily-sync | 인덱스 +3/+149, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 148개
- 인덱스: 신규 3 / 갱신 149 / 총 11,760개 파일 (FTS 11,515, 304.1MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync 타임아웃 및 keepalive 이슈 모두 미발생
- 작업 변경 148개: MI8_project 141 (카드뉴스 SEO .seo.json 대량 회귀 + md 본문), post1 1 (git 커밋 b45ff1f), auto-trading 1 / git 커밋 2개 저장소 (post1 b45ff1f, memories bcfc828)
- daily 페이지: concepts/daily/2026-08-31.md 생성

## [2026-08-30] daily-sync | 인덱스 +5/-0, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 67개
- 인덱스: 신규 5 / 갱신 67 / 총 11,757개 파일 (FTS 11,512, 304.1MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 — card-news-supabase-sync (05:00, Supabase `.status.json` curl PUT 타임아웃 10초). **7일 창(08-24~30)에서 6회 재발** — PUT/DELETE 교차, 간헐 절정 구간 (08-26·27 소멸 후 3일 연속 재발). 단건이라 "3건 이상 반복" 기준은 미달이나 명백한 재발성 패턴 → 재시도 래퍼(타임아웃 30초 + --retry/지수 백오프) 명시적 조치 제안.
- 작업 변경 67개: MI8_project 53 (카드뉴스 md + 발행 slug), lotto-predictor 2, auto-trading 1, post1 1 / .hermes 10 / git 커밋 2개 저장소 (post1 9d632af, memories 8300425)

## [2026-08-28] daily-sync | 인덱스 +9/-0, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 81개
- 인덱스: 신규 9 / 갱신 66 / 총 11,745개 파일 (FTS 11,500, 303.9MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 — card-news-supabase-sync (05:20, Supabase `.status.json` curl PUT 타임아웃 10초). 5일 창(08-24~28)에서 이 원인 4회 재발성 간헐 이슈 (08-26·27 소멸 후 재발). 단건이라 "3건 이상 반복" 기준은 미달, 관찰 유지 + 재시도 규칙 추가 권장.
- 작업 변경 81개: MI8_project 65 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 11 / git 커밋 2개 저장소 (post1 99550fe, memories 278e56d)

## [2026-08-27] daily-sync | 인덱스 +4/-0, 레지스트리 32개 폴더, 크론 에러 3건 (조치 필요), 작업 변경 68개
- 인덱스: 신규 4 / 갱신 64 / 총 11,736개 파일 (FTS 11,491, 303.8MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 3건 — **단일 유형 반복 (조치 필요)**: naver-session-hourly-keepalive 2회 (23:00, 00:00) + daily-memory-to-notion 1회 (00:00), 전부 `HTTP 401: Model ox-alpha-free is not supported` — 크론 job이 지원되지 않는 모델(ox-alpha-free)로 지정됨
- 작업 변경 68개: MI8_project 51 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 12 / git 커밋 2개 저장소 (post1 de32ddf, memories 3c29952)

## [2026-08-26] daily-sync | 인덱스 +6/-0, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 70개
- 인덱스: 신규 6 / 갱신 69 / 총 11,731개 파일 (FTS 11,486, 303.7MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일 반복되던 card-news-supabase-sync 타임아웃 소멸, 경과 관찰 유지
- 작업 변경 70개: MI8_project 52 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 13 / git 커밋 2개 저장소 (post1 f5aa224, memories c62e7c6)

## [2026-08-25] daily-sync | 인덱스 +5/-0, 레지스트리 32개 폴더, 크론 에러 4건, 작업 변경 67개
- 인덱스: 신규 5 / 갱신 69 / 총 11,725개 파일 (FTS 11,480, 303.7MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 4건 — **2개 유형 (조치 필요)**: card-news-supabase-sync 2회 (23:30, 23:52, Supabase 상태 동기화 curl PUT 타임아웃 10초 — 48h 내 동일 원인 3회 반복, 미해결), telecom-3sa-daily-news + auto-trading-morning-briefing 2건 (08:30, HTTP 401 Insufficient balance — opencode.ai 워크스페이스 결제 잔액 부족)
- 작업 변경 67개: MI8_project 54 (카드뉴스 md), auto-trading 4, post1 1 (git 커밋 e0320fa) / git 커밋 2개 저장소

## [2026-08-24] daily-sync | 인덱스 +4/+149, 레지스트리 32개 폴더, 크론 에러 1건 (card-news-supabase-sync 타임아웃), 작업 변경 149개

## [2026-08-23] daily-sync | 인덱스 +5/+68, 레지스트리 32개 폴더, 크론 에러 17건 (inference config drift unpinned), 작업 변경 72개

## [2026-06-01] create | Wiki initialized
- Domain: Personal knowledge base
- Structure created with SCHEMA.md, index.md, log.md
- Karpathy LLM Wiki pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## [2026-06-01] ingest | Karpathy LLM Wiki from https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## [2026-06-01] lint | 1 issues found

## [2026-06-01] batch_ingest | PC files: 60 new, 10 skip, 0 fail

## [2026-06-01] batch_ingest | PC files: 0 new, 70 skip, 0 fail

## [2026-06-01] lint | 4 issues found

## [2026-06-02] batch_ingest | PC files: 3 new, 69 skip, 0 fail

## [2026-06-02] lint | 4 issues found

## [2026-06-03] batch_ingest | PC files: 2 new, 72 skip, 0 fail

## [2026-06-03] lint | 4 issues found

## [2026-06-04] batch_ingest | PC files: 2 new, 74 skip, 0 fail

## [2026-06-04] lint | 4 issues found

## [2026-06-05] batch_ingest | PC files: 2 new, 76 skip, 0 fail

## [2026-06-05] lint | 4 issues found

## [2026-06-07] batch_ingest | PC files: 3 new, 78 skip, 0 fail

## [2026-06-07] lint | 4 issues found

## [2026-06-08] batch_ingest | PC files: 3 new, 80 skip, 0 fail

## [2026-06-08] lint | 4 issues found

## [2026-06-09] batch_ingest | PC files: 3 new, 82 skip, 0 fail

## [2026-06-09] lint | 3 issues found

## [2026-06-10] lint | 3 issues found

## [2026-06-10] batch_ingest | PC files: 3 new, 80 skip, 0 fail

## [2026-06-10] lint | 3 issues found

## [2026-06-11] batch_ingest | PC files: 2 new, 87 skip, 0 fail

## [2026-06-11] lint | 3 issues found

## [2026-06-11] lint | 3 issues found

## [2026-06-12] batch_ingest | PC files: 8 new, 88 skip, 0 fail

## [2026-06-12] lint | 3 issues found

## [2026-06-13] batch_ingest | PC files: 2 new, 96 skip, 0 fail

## [2026-06-13] lint | 3 issues found

## [2026-06-13] ingest | us-stock-tax from file: /Users/bearj/documents/tax-research/us-stock-tax.md

## [2026-06-13] ingest | jp-stock-tax from file: /Users/bearj/documents/tax-research/jp-stock-tax.md

## [2026-06-13] ingest | eu-stock-tax from file: /Users/bearj/documents/tax-research/eu-stock-tax.md

## [2026-06-13] ingest | kr-stock-tax from file: /Users/bearj/documents/tax-research/kr-stock-tax.md

## [2026-06-13] ingest | real-estate-tax from file: /Users/bearj/documents/tax-research/real-estate-tax.md

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 2 issues found

## 2026-06-13
- llm-wiki 대규모 재구성: 164개 → 84개 페이지
- 논문/뉴스 107개 → raw/archive/ 이동
- concepts/ 카테고리별 폴더 생성 (projects/knowledge/learnings/daily/)
- 84개 파일 wikilink 연결 완료
- 세제 조사 5개 knowledge/ 에 ingest + 상호 크로스레퍼런스
- devbox.md 추가 (추천글 정리)
- SCHEMA.md 업데이트: 구조 + 추천글 정리 규칙
- index.md 재작성: 카테고리별 분류

## [2026-06-14] lint | 2 issues found

## [2026-06-15] sync | Daily sync executed
- 2 changed files detected: world_news_20260614.md, world_news_20260615.md
- All external content → skipped (not added to concepts/)
- Daily page created: concepts/daily/2026-06-15.md
- index.md updated

## [2026-06-15] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-17] lint | 2 issues found

## [2026-06-17] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-21] lint | 2 issues found

## [2026-06-22] lint | 2 issues found

## [2026-06-22] lint | 2 issues found

## [2026-06-23] lint | 2 issues found

## [2026-06-23] lint | 2 issues found

## [2026-06-24] lint | 2 issues found

## [2026-06-24] lint | 2 issues found

## [2026-06-25] sync | daily 2026-06-24 updated, 8 new work items
- Updated: concepts/daily/2026-06-24.md — added 6/24 work summary (주식 분석, 뉴스, 사이트 배포, 칸반)
- Skipped: world_news_20260625.md (external content → raw/archive only)
- Index updated: Daily section added

## [2026-06-25] lint | 2 issues found

## [2026-06-26] sync | 2 new pages, 1 skipped
- New: concepts/daily/2026-06-25.md — 6/25 work log (주식 분석, 뉴스, 사이트 배포, 칸반)
- New: concepts/knowledge/code-edu-lab-curriculum.md — Code Edu Lab 4스택 커리큘럼 요약
- Skipped: world_news_20260626.md (external content → not synced to concepts)
- Index updated: 2 new entries in Concepts section

## [2026-06-26] lint | 2 issues found

## [2026-06-26] lint | 2 issues found

## [2026-06-27] lint | 2 issues found

## [2026-06-29] lint | 2 issues found

## [2026-06-30] lint | 2 issues found

## [2026-07-07] lint | 2 issues found

## [2026-07-07] lint | 2 issues found

## [2026-07-08] lint | 2 issues found

## [2026-07-09] lint | 2 issues found

## [2026-07-09] lint | 2 issues found

## [2026-07-11] lint | 2 issues found

## [2026-07-11] lint | 2 issues found

## [2026-07-12] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-14] lint | 2 issues found

## [2026-07-15] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-08-09] daily-sync | 작업 변경 감지 75개, daily 페이지 갱신 (2026-08-09.md 생성)
- collect_work.py 신규 도입: ~/projects + ~/.hermes 작업 변경 감지 파이프라인
- llm-wiki-daily-sync 크론 프롬프트 교체 (외부 수집 금지 → 작업 내역 수집)

## [2026-08-09] lint | 2 issues found

## [2026-08-09] wiki-v4 | 위키 전면 재구축 (외부 콘텐츠 삭제 → Hermes 작업 인덱스)
- 기존 raw 2,448 + concepts 266 + entities 10 삭제 (git 태그 legacy-wiki-2026-08-09로 보존)
- build_index.py: 10,806개 작업 파일 FTS5 인덱싱 (5.4초)
- search.py: FTS5 + RAG 답변 CLI
- web.py: /api/search 통합 검색
- SCHEMA.md v2 재작성, llm-wiki 스킬 v4 업데이트

## [2026-08-09] cron-errors | collect_cron_errors.py 도입, 24h 내 에러 8건 분석 기록
- collect_cron_errors.py 신규: 크론 output에서 최근 24h FAILED/Error 수집
- llm-wiki-daily-sync 프롬프트에 에러 분석 단계 추가 (패턴 분석 + 개선 제안)
- 8건 분석: naver-session-hourly-keepalive 5회 반복 (Broken pipe) — 재시도 적용 검토 대상

## [2026-08-09] personal-sites | 개인 사이트 폴더 내역 기록 (중복 방지)
- concepts/projects/personal-sites.md 신규 생성: justfly32.github.io(포트폴리오) / post1(활동로그) / personal-site(구 프로토타입) 3개 폴더 역할·위치·갱신방식 정리
- index.md 카탈로그 등록 (Total pages: 1)
- 목적: personal-site→post1 진화 구조를 기록해 폴더 중복 생성 방지

## [2026-08-09] project-registry | 프로젝트 폴더 레지스트리 도입 (중복 방지 시스템)
- generate_project_registry.py 신규: ~/projects + justfly32.github.io 스캔 → concepts/projects/project-registry.md 자동 생성 (36개 폴더, git 11/로컬 25)
- 중복 유사 후보 6그룹 식별: 건강관리(elderly-health×2), GIF(simpli×5), 대시보드(system×3), PPT(html2pptx/PPT_Generator), 개인사이트(personal-site/post1), 코딩교육(code-edu×3)
- hermes-orchestration 스킬에 "코딩 전 레지스트리 조회" 필수 규칙 추가
- 갱신 명령: python3 ~/wiki/scripts/generate_project_registry.py

## [2026-08-09] project-registry-cleanup | 비정본 7개 폴더 삭제 (휴지통 이동)
- 정리 3개 그룹(건강관리·코딩 교육·GIF) 비정본 확정 후 삭제: elderly-health, code-tutorial, code-express, simple-anim-maker, simpli-video-maker, animation-maker, stickman-gif-creator
- 삭제 방식: ~/.Trash/hermes-removed-20260809/ 로 이동 (복구 가능), code-tutorial은 GitHub 원격 백업 존재
- 사전 검증: 크론/스크립트/포트폴리오(justfly32.github.io) 참조 없음 확인 후 삭제
- 레지스트리 갱신: 36 → 29개 폴더 (git 9/로컬 20), CANONICAL 3개 정본만 유지 (elderly-health-care, code-edu-lab, simpli-gif-maker)
- generate_project_registry.py에 REMOVED 섹션 + 삭제 기록 표 추가, index.md 설명 갱신

## [2026-08-09] registry-auto | llm-wiki-daily-sync에 레지스트리 자동 재생성 추가
- llm-wiki-daily-sync 크론(매일 05:30) 프롬프트에 Step 1.5 추가: generate_project_registry.py 실행
- 새 폴더 생성 시 ~/projects 스캔 → project-registry.md 자동 갱신 (다음 날 05:30 반영)
- 최종 보고에 레지스트리 폴더 수 + 신규 폴더 이름 포함하도록 변경
- llm-wiki 스킬 SKILL.md 크론 섹션에도 반영 (1~6단계로 재구성)

## [2026-08-09] dashboard-merge | 대시보드 3종 → pc-llm-dashboard 단일 통합
- 배경: system-dashboard / system-monitor-dashboard / openclaw-token-dashboard 3개가 동일 기능 복제본임을 확인 (라우트 동일, 같은 날 생성)
- 기능 정체성 확정: PC 상태 확인 + LLM 사용량 확인 → 폴더명을 기능 기준 pc-llm-dashboard로 신설
- 코드 베이스: openclaw-token-dashboard(리팩토링 완료, useMemo/fetchStats) 채택, system-dashboard와 diff 비교 후 고유 기능 없음 확인
- 검증: npm install + build 성공, dev 서버 기동 (API 4010 / Vite 5175), health·system-status·hermes-stats(3.4억 토큰/1,877세션)·openclaw-stats 정상 응답, title PC·LLM 대시보드로 변경
- 기존 3개 폴더 → ~/.Trash/hermes-removed-20260809/ 이동
- 레지스트리: 29 → 27개, CANONICAL에 pc-llm-dashboard 등록, 대시보드 그룹 중복 후보 제거

## [2026-08-09] personal-site-move | justfly32.github.io를 projects로 이동
- 사용자 발견: 개인 사이트 폴더가 home 직속(~/justfly32.github.io)에 있어 projects와 분산
- 이동: ~/justfly32.github.io → ~/projects/justfly32.github.io (git remote/branch 그대로, clean 상태)
- 참조 확인: post1 크론은 /Users/bearj/projects/post1 사용(무관), jobs.json의 justfly32는 URL 텍스트뿐 → 파일 경로 참조는 레지스트리 EXTRA_DIRS뿐
- generate_project_registry.py: EXTRA_DIRS 비움(projects 스캔으로 자동 포함), 규칙 문구를 "개인 사이트 포함 projects 통일"로 변경
- personal-sites.md: 위치/규칙 갱신 (home 직속 금지 추가)
- 레지스트리: 27 → 28개 폴더 (justfly32.github.io가 git 프로젝트로 합류, git 10개)

## [2026-08-09] enterprise-search | 사내 파일 검색 PoC 구축
- 신규 프로젝트: ~/projects/enterprise-search (Next.js 16 + FastAPI + SQLite/Supabase RLS)
- FileAccessor 인터페이스 (DRM 무관 추상화): LocalFileAccessor 구현, 파수/마크애니/MIP는 제품 확정 후 추가 예정
- 인덱서: FTS5(bm25) + n-gram 벡터(cosine) 하이브리드, mtime 증분
- 권한 모델: 파일별 ACL(dept/role/users) → 검색 단계 차단 (Glean Permission Mirroring 원칙)
- 검증: CLI 5개 시나리오 + 브라우저 E2E — 일반 직원 급여 차단, 법무팀 계약서 접근, admin 전체 접근, RAG 답변(월 1,500만원/건당 300만원) + 출처 표기
- 배운 점: HTTP 헤더 한글 불가 → 사용자 컨텍스트는 body 전달 (브라우저 fetch 제약), Next 15.4.1→16.3.0 필요 (Node22 호환)
- schema/supabase.sql: documents + file_acl + RLS + pgvector (운영용)

## [2026-08-10] daily-sync | 인덱스 +43/-162, 레지스트리 29개 폴더, 크론 에러 7건, 작업 변경 271개
- 인덱스: 신규 43 / 갱신 162 / 총 11,120개 파일 (FTS 10,880)
- 레지스트리: 28 → 29개 폴더 (git 11 / 로컬 18) — enterprise-search 신규 합류
- 크론 에러 7건: naver-session-hourly-keepalive 4 (2일 연속 반복, 조치 필요), Broken pipe 5 / empty stream 2
- 작업 변경 271개: MI8_project 138, enterprise-search 51, pc-llm-dashboard 25, justfly32.github.io 2, post1 1 / git 커밋 3개 저장소 22건
## [2026-08-11] daily-sync | 인덱스 +8/+67, 레지스트리 29개 폴더, 크론 에러 10건, 작업 변경 70개
- 인덱스: 신규 8 / 갱신 67 / 총 11,128개 파일 (FTS 10,888)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 10건: naver-session-hourly-keepalive 5 (3일 연속 반복, 조치 필요), Broken pipe 6 (09:08~10:10 집중) / empty stream 3, llm-wiki-daily-sync 1건은 오탐
- 작업 변경 70개: MI8_project 50 (카드뉴스 md), post1 1 / git 커밋 1건
## [2026-08-12] daily-sync | 인덱스 +7/+64, 레지스트리 29개 폴더, 크론 에러 8건, 작업 변경 66개
- 인덱스: 신규 7 / 갱신 64 / 총 11,135개 파일 (FTS 10,895)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 8건 (오탐 1 제외 실질 7): naver-session-hourly-keepalive 5 (4일 연속 반복, 조치 필요), Broken pipe 5 (09:09~10:09 집중, 2일 연속 동일 창) / empty stream 2, llm-wiki-daily-sync 1건은 오탐 (2일 연속)
- 작업 변경 66개: MI8_project 50 (카드뉴스 md), post1 1 / git 커밋 1건
## [2026-08-13] daily-sync | 인덱스 +12/+58, 레지스트리 29개 폴더, 크론 에러 8건, 작업 변경 76개
- 인덱스: 신규 12 / 갱신 58 / 총 11,147개 파일 (FTS 10,907)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 8건 (오탐 1 제외 실질 7): naver-session-hourly-keepalive 4 (5일 연속 반복, 조치 필요), Broken pipe 5 (09:09~10:09 3건 집중, 3일 연속 동일 창) / empty stream 2, seo-optimizer-daily 1건 신규 출현 (21:09), llm-wiki-daily-sync 1건은 오탐 (3일 연속)
- 작업 변경 76개: MI8_project 61 (카드뉴스 md), post1 1 (git 커밋 fe70f18) / git 커밋 1건

## [2026-08-15] daily-sync | 인덱스 +10/+61, 레지스트리 29개 폴더, 크론 에러 10건, 작업 변경 66개
- 인덱스: 신규 10 / 갱신 61 / 총 11,165개 파일 (FTS 10,925)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 10건 (오탐 1 제외 실질 9): naver-session-hourly-keepalive 6 (7일 연속 반복 + 전일 3→6 2배 급증, 조치 필요), Broken pipe 9건 전부 (01:08~21:09 전 시간대 확산, 09:09 3건/21:09 2건 동시), seo-optimizer-daily 2일 연속 21:09 동일 시각 재발, llm-wiki-daily-sync 1건 오탐 (5일 연속)
- 작업 변경 66개: MI8_project 50 (카드뉴스 md), lotto-predictor 2, post1 1 (git 커밋 073dc53) / git 커밋 1건

## [2026-08-14] daily-sync | 인덱스 +7/+57, 레지스트리 29개 폴더, 크론 에러 7건, 작업 변경 73개
- 인덱스: 신규 7 / 갱신 57 / 총 11,155개 파일 (FTS 10,915)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 7건 (오탐 1 제외 실질 6): naver-session-hourly-keepalive 3 (6일 연속 반복, 조치 필요), Broken pipe 5 (09:08~10:09 4건 집중 3일 연속 + 01:09 확산), card-news-supabase-sync 1건 신규 (Duplicate KeyAlreadyExists), llm-wiki-daily-sync 1건 오탐 (4일 연속)
- 작업 변경 73개: MI8_project 62 (카드뉴스 md 54 + 이미지 11), post1 1 (git 커밋 3911341) / git 커밋 1건

## [2026-08-16] daily-sync | 인덱스 +218/+64, 레지스트리 31개 폴더, 크론 에러 9건, 작업 변경 277개
- 인덱스: 신규 218 / 갱신 64 / 총 11,383개 파일 (FTS 11,138, 298.6MB)
- 레지스트리: 31개 폴더 (git 12 / 로컬 19) — 전일 29개에서 +2. 신규: auto-trading (git, 한국 주식 자동매매, 최근 커밋 2026-08-16), auto-trading-research (로컬)
- 크론 에러 9건 (오탐 1 제외 실질 8): naver-session-hourly-keepalive 5 (8일 연속 반복, 조치 필요, Broken pipe 4 + empty stream 1, 09~13시 집중 + 01:09 확산), seo-monitor-search 1 (10:09), telecom-3sa-daily-news 1 (09:09), card-news-supabase-sync 1 (Duplicate KeyAlreadyExists 03:11, 2일 간격 재발), llm-wiki-daily-sync 1건 오탐 (6일 연속)
- 작업 변경 277개: auto-trading 190 (git 커밋 20건: 금 10% 동적 리밸런스, bear_recovery_days 15→0, 5년 백테스트), MI8_project 50 (카드뉴스 md), auto-trading-research 2 (신규), post1 1 (git 커밋 a1fb013), lotto-predictor 1 / git 커밋 21건 (2개 저장소)

## [2026-08-17] daily-sync | 인덱스 +32/+159, 레지스트리 31개 폴더, 크론 에러 2건, 작업 변경 195개
- 인덱스: 신규 32 / 갱신 159 / 총 11,415개 파일 (FTS 11,170, 299.0MB)
- 레지스트리: 31개 폴더 (git 12 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건 (오탐 1 제외 실질 1): naver-session-hourly-keepalive 1 (Broken pipe 01:09, 9일 연속 반복, 조치 필요 — 전일 5건→1건 급감), llm-wiki-daily-sync 1건 오탐 (7일 연속)
- 작업 변경 195개: MI8_project 147 (카드뉴스 .seo.json — 전일 50→147 급증), auto-trading 13 (git 커밋 7건: trading-rules.md 단일 문서, 장중 체크 10시+14시, 트레일링 스톱 10% 확정), post1 1 (git 커밋 9763644) / git 커밋 8건 (2개 저장소)

## [2026-08-18] daily-sync | 인덱스 +230/+71, 레지스트리 32개 폴더 (신규: slide-master), 크론 에러 오탐 1건→수정, 작업 변경 306개 (MI8 77, slide-master 65, post1 커밋 1)

## [2026-08-19] daily-sync | 인덱스 +29/+68, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 105개
- 인덱스: 신규 29 / 갱신 68 / 총 11,674개 파일 (FTS 11,429, 303.2MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건: card-news-supabase-sync (Duplicate KeyAlreadyExists 23:20, 주 3회 이상 재발, 조치 필요)
- 작업 변경 105개: MI8_project 64 (카드뉴스 md), auto-trading 20 (git 커밋 77012b2: NHPLUG 라이브 연동), post1 1 (git 커밋 d26b40f) / git 커밋 2건 (2개 저장소)

## [2026-08-21] daily-sync | 인덱스 +10/+78, 레지스트리 32개 폴더, 크론 에러 2건, 작업 변경 83개
- 인덱스: 신규 10 / 갱신 78 / 총 11,704개 파일 (FTS 11,459, 303.5MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건: (1) card-news-supabase-sync 03:21 — Supabase status.json DELETE curl 10초 타임아웃(TimeExpired), (2) auto-trading 16:05 — NHPLUG 22642 주문가격 입력 불가 (시간외 71, 커밋 8a2f7e3으로 수정 완료)
- 작업 변경 83개: MI8_project 52 (카드뉴스 md), auto-trading 11 (git 커밋 8건: 장후코어 81 정합, bull_hold 매도 억제, --no-save), post1 1 (git 커밋 978ee99) / git 커밋 3개 저장소

## [2026-08-22] daily-sync | 인덱스 +7/+67, 레지스트리 32개 폴더, 크론 에러 16건, 작업 변경 69개
- 인덱스: 신규 7 / 갱신 67 / 총 11,711개 파일 (FTS 11,466, 303.6MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 16건 — **모두 동일 유형 (인퍼런스 설정 drift, unpinned, 조치 필요)**: naver-session-hourly-keepalive 15회(매시간 14:00~05:00), auto-trading-evening-briefing 1회. 원인: 글로벌 설정 migrate(provider opencode-go→openrouter, model deepseek-v4-flash→deepseek/deepseek-v4-flash-0731) 후 unpinned 작업 안전 차단. 해결: 각 job을 `cronjob action=update`로 pin.
- 작업 변경 69개: MI8_project 51 (카드뉴스 md), auto-trading 4, lotto-predictor 2, post1 1 (git 커밋 cc3f963) / git 커밋 2개 저장소

## [2026-08-20] daily-sync | 인덱스 +0/+55, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 96개
- 인덱스: 신규 0 / 갱신 55 / 총 11,694개 파일 (FTS 11,449, 303.3MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync Duplicate 미발생
- 작업 변경 96개: MI8_project 52 (카드뉴스 md), auto-trading 14 (git 커밋 7건: 장중/장후 모드 분리, env별 분리, ops-runbook), post1 1 (git 커밋 0ce483a) / git 커밋 3개 저장소

## [2026-08-29] daily-sync | 인덱스 +7/+65, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 68개
- 인덱스: 신규 7 / 갱신 65 / 총 11,752개 파일 (FTS 11,507, 304.0MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 05:02 상태 정리 DELETE curl 타임아웃 10초) — 콘텐츠 업로드/SEO 정상, 정리 단계만 실패
- 작업 변경 68개: MI8_project 52 (카드뉴스 md), auto-trading 4, lotto-predictor 2, post1 1 (git 커밋 df5514f), .hermes 9 / git 커밋 2개 저장소 (post1 df5514f, memories 1ccdcae)
- daily 페이지: concepts/daily/2026-08-29.md 생성

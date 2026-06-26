---
title: 2026-06-09 작업 기록
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [document]
sources: [raw/local/general/daily_memories-2026-06-09-2026-06-10.md]
source_file: /Users/bearj/.hermes/memories/daily_memories/2026-06-09.md
confidence: high
links: [[daily_memories-world_news_20260608|← 6월 8일 세계 뉴스]], [[daily_memories-2026-06-10|6월 10일 작업 기록 →]]
---

# 2026-06-09 작업 기록

> source: `/Users/bearj/.hermes/memories/daily_memories/2026-06-09.md`
> date: 2026-06-10
> category: general

## Content

# 2026-06-09 작업 기록

## 완료
- **일일 위키 업데이트** (07:30 cron): PC 파일 3개 수집 (latest.md, MEMORY.md, 2026-06-08.md), 82개 건너뜀, 0개 실패 / 린트 2개 이슈 (WARNING: 145개 페이지 링크 없음, ERROR: 5개 깨진 위키링크) / 인덱스 재빌드 완료
- **초고속인터넷 가입 지원금 추이 보고서** (10:00 cron): HTML 보고서 생성 완료 (`~/documents/internet_reports/2026-06-09_internet_support_report.html`) / Google Drive 업로드 실패 (OAuth 토큰 만료) / 텔레그램 발송 실패 (봇 토큰 401)
- **주식 동향 분석** (16:00 cron): 데이터 수집 완료 (네이버 증권, 매일경제 MK마켓, 연합인포맥스, 뉴스핌) / HTML 가이드 생성 (`~/projects/hermes_ops/docs/stock_analysis_20260609.html`, 15.3KB) / PPTX 생성 (3슬라이드) / 노션 등록 완료 (페이지: Agent_주식분석) / Google Drive 업로드 실패 (인증 정보 없음) / 텔레그램 전송 실패 (Bot Token/Chat ID 미설정)
- **Google Drive 토큰 갱신** (사용자 요청): 새 refresh_token 발급 완료
- **멀티 에이전트 프로필 구축** (사용자 요청): 기존 developer/researcher/reviewer 3개 프로필 확인 및 유지
- **Gateway 재시작**: Telegram, Discord, Slack 3개 플랫폼 모두 정상 연결 확인

## 주요 작업
- 주식 시장: 6/8 장마감 코스피 7,484.41 (-8.29%, "검은 월요일"), 코스닥 921.85 (-8.03%) / 6/9 장중 코스피 ~8,054 (+7.62% V자 반등, 매수 사이드카 발동)
- 주요 이슈: 스페이스X 6/12 나스닥 상장 (750억 달러) / FOMC 6/16~17 / 외국인 22일 연속 순매도 / 기관 2.4조 순매수 전환
- 인터넷 지원금: SK브로드밴드 평균 50만원/최대 52만원, LG U+ 평균 47만원/최대 48만원, KT 평균 45만원/최대 48만원 (인터넷+TV 결합 기준) — 3사 모두 변동 없음

## 진행 중
- Google Drive OAuth 토큰 갱신 필요 → 사용자 요청으로 토큰 갱신했으나 지속적 모니터링 필요
- 텔레그램 봇 토큰 401 오류 → BotFather 재확인 필요

## 다음 할 일
- 위키 린트 이슈 정리: 145개 orphan 페이지, 5개 깨진 위키링크
- Google Drive 자동화 재설정 확인
- 텔레그램 봇 토점 상태 확인


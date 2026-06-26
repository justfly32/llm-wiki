---
title: 2026-05-20 작업 기록
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [document, database]
sources: [raw/local/general/daily_memories-2026-05-20-2026-06-01.md]
source_file: /Users/bearj/.hermes/memories/daily_memories/2026-05-20.md
confidence: high
links: [[daily_memories-2026-05-19|← 5월 19일 작업 기록]], [[daily_memories-2026-05-21|5월 21일 작업 기록 →]]
---

# 2026-05-20 작업 기록

> 📁 원본: `/Users/bearj/.hermes/memories/daily_memories/2026-05-20.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: general

## 내용

# 2026-05-20 작업 기록

## 완료
- 카카오톡 나와의 대화(북극곰) 자동 읽기 파이프라인 구축
  - 클립보드 복사 → SQLite DB 저장 → 구글 시트 업데이트
  - 요약 내역 + URL 링크 자동 추출
  - kakao-chat-to-sheets 스킬 완성
- 카톡 메신저 봇 구축 논의:
  - 텔레그램과 연동한 메신저 비서 구조 설계
  - 크론 10초마다 대화 감지 → 응답 전송

## 진행/논의
- 카톡 봇 인식 간격 조정 (10분 → 2초 시도 → 10초로 조정)
- 이모지 자동 추가 요청
- 크론 작업 내역 정리 요청
- 모델 전환 빈도 높음 (Google Gemini → NVIDIA → OpenRouter Owl Alpha)

## 참고
- 시스템 패치 시스템 이슈: 캐시 삭제 및 재설치 필요
- pyautogui, keyboard 설치 방법 재확인


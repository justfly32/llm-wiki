---
title: 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트
created: 2026-06-09
updated: 2026-06-23
type: concept
tags: [security, system, monitoring, compliance]
sources: [raw/local/security/security_reports-latest-2026-06-15.md]
source_file: /Users/bearj/Documents/security_reports/latest.md
confidence: high
links: [[security_reports-security_report_20260530_102458|이전 보안 리포트]]
---

# 🛡️ 시스템 보안 모니터링 리포트 — 2026-06-15

## 실행 요약

| 항목 | 상태 | 비고 |
|------|------|------|
| 시스템 에러 | 🔴 11건 | Slack bolt Session is closed 반복 |
| 로그인 실패 | ✅ 정상 | 비인가 접근 시도 없음 |
| 개인정보 노출 | 🔴 20건 | 이메일/날짜 패턴 탐지 |
| 이상 프로세스 | ✅ 정상 | 의심 프로세스 없음 |
| 디스크 사용량 | ✅ 정상 | 루트 11%, Data 50% |

## 주요 발견

### 1. 시스템 에러 — Slack Bolt 연결 실패
- `RuntimeError: Session is closed` 반복 발생 (2026-06-15 08:59~09:00)
- slack_bolt.AsyncApp이 WebSocket 연결 후 즉시 세션 닫힘
- **조치 필요**: Slack app 토큰/설정 확인

### 2. 개인정보 노출 — 20건 탐지
- 주요 패턴: 이메일 주소, 날짜 형식
- 주요 파일: `release.py`(165건), `.mailmap`(160건), `.hermes_history`(139건)
- **참고**: 대부분 hermes-agent 내부 파일로 외부 노출 위험 낮음

### 3. 노출된 .env 파일 — 10건
- `projects/.env`, `.hermes/.env` 등 .gitignore 미등록 가능성
- **조치 필요**: .gitignore에 .env 패턴 추가 확인

### 4. 알 수 없는 리스닝 포트 — 13건
- PostgreSQL(5432), Cloudflare Tunnel(20241/20242), Python 서버 다수
- **참고**: 대부분 로컬 개발 환경 포트로 정상 가능성 높음

### 5. 방화벽 비활성화
- macOS 방화벽이 비활성 상태
- **조치 권장**: 시스템 설정에서 방화벽 활성화

## 디스크 사용량

| 마운트 | 사용량 |
|--------|--------|
| / (루트) | 11% |
| /System/Volumes/Data | 50% |
| .hermes | 4.2GB |
| projects | 1.8GB |

## 연결 문서
- [[security_reports-security_report_20260530_102458|이전 보안 리포트 (2026-05-30)]]

---
title: 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [security, system, python, database, web]
sources: [raw/local/security/security_reports-security_report_20260530_102458-2026-06-01.md]
source_file: /Users/bearj/Documents/security_reports/security_report_20260530_102458.md
confidence: high
links: [[security_reports-latest|최신 보안 리포트]], [[docs-phase1-planning|Phase 1 기획]], [[docs-phase1-3-target-databases|대상 DB 목록]], [[docs-phase1-4-5-relationship-techstack|기술 스택 선정]]
---

# 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트

> 📁 원본: `/Users/bearj/Documents/security_reports/security_report_20260530_102458.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: security

## 내용

# 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트

**생성 시각:** 2026-05-30 10:24  
**호스트:** jeongmin-ui-Macmini.local  
**사용자:** bearj

---

## 1. 실행 요약

| 항목 | 상태 | 비고 |
|------|------|------|
| 시스템 에러 | 🔴 20건 | 최근 에러 수 |
| 로그인 실패 | ✅ 정상 | 비인가 접근 시도 |
| 개인정보 노출 | 🔴 20건 | 민감 정보 포함 파일 |
| 이상 프로세스 | ✅ 정상 | 의심스러운 프로세스 |
| 디스크 사용량 | ✅ 정상 | 저장 공간 |

---

## 2. 시스템 로그 분석


### 에러 (20건)
- sqlite3.OperationalError: no such column: tenant
- 2026-05-30 10:16:45,136 WARNING [20260530_101408_6ed65f] run_agent: Tool memory returned error (0.00s): {"success": false, "error": "Memory at 2,095/2,200 chars. Adding this entry (181 chars) would ex
- 2026-05-30 10:17:21,573 WARNING [20260530_101408_6ed65f] run_agent: Tool memory returned error (0.00s): {"success": false, "error": "Replacement would put memory at 2,243/2,200 chars. Shorten the new 
- 2026-05-30 10:17:27,408 ERROR [20260524_003555_3bd508] gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-05-30 10:18:14,275 WARNING [20260530_101408_6ed65f] run_agent: Tool memory returned error (0.00s): {"success": false, "error": "Memory at 2,083/2,200 chars. Adding this entry (480 chars) would ex
- 2026-05-30 10:18:27,542 ERROR [20260524_003555_3bd508] gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-05-30 10:19:27,670 ERROR [20260524_003555_3bd508] gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant

## 3. 개인정보 처리 현황 점검

### 민감 정보 포함 파일 (20건)
| 파일 | 패턴 | 매칭 수 |
|------|------|----------|
| `.hermes/hermes-agent/scripts/release.py` | \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z | 173 |
| `.hermes/hermes-agent/.mailmap` | \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z | 160 |
| `.hermes/.hermes_history` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 139 |
| `.hermes/hermes-agent/tests/hermes_cli/test_logs.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 32 |
| `projects/personal-site/index.html` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 28 |
| `projects/post1/tests/test_parser.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 23 |
| `projects/tests/test_parser.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 23 |
| `projects/personal-site/tests/test_parser.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 23 |
| `.hermes/hermes-agent/skills/index-cache/lobehub_index.json` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 21 |
| `.hermes/hermes-agent/tests/agent/test_anthropic_adapter.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 18 |
| `.hermes/profiles/reviewer/home/Library/Python/3.9/lib/python/site-packages/PIL/ImageDraw.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 18 |
| `.hermes/profiles/reviewer/home/Library/Python/3.9/lib/python/site-packages/PIL/TiffImagePlugin.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 18 |
| `.hermes/profiles/developer/home/Library/Python/3.9/lib/python/site-packages/PIL/ImageDraw.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 18 |
| `.hermes/profiles/developer/home/Library/Python/3.9/lib/python/site-packages/PIL/TiffIma

...(내용 생략)...

---
source_file: /Users/bearj/Documents/security_reports/latest.md
ingested: 2026-06-09
sha256: db726d10d791
category: security
original_title: 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트
---

# 🛡️ 시스템 보안/컴플라이언스 모니터링 리포트

**생성 시각:** 2026-06-08 09:01  
**호스트:** jeongmin-ui-Macmini.local  
**사용자:** bearj

---

## 1. 실행 요약

| 항목 | 상태 | 비고 |
|------|------|------|
| 시스템 에러 | 🔴 21건 | 최근 에러 수 |
| 로그인 실패 | ✅ 정상 | 비인가 접근 시도 |
| 개인정보 노출 | 🔴 20건 | 민감 정보 포함 파일 |
| 이상 프로세스 | ✅ 정상 | 의심스러운 프로세스 |
| 디스크 사용량 | ✅ 정상 | 저장 공간 |

---

## 2. 시스템 로그 분석


### 에러 (21건)
- sqlite3.OperationalError: no such column: tenant
- 2026-06-08 08:51:31,285 ERROR gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-06-08 08:52:31,419 ERROR gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-06-08 08:53:31,554 ERROR gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-06-08 08:54:31,687 ERROR gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future
- sqlite3.OperationalError: no such column: tenant
- 2026-06-08 08:55:31,820 ERROR gateway.run: kanban dispatcher: tick failed on board ultrafast-comm-future

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
| `.hermes/profiles/developer/home/Library/Python/3.9/lib/python/site-packages/PIL/TiffImagePlugin.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 18 |
| `.hermes/profiles/reviewer/home/Library/Python/3.9/lib/python/site-packages/PIL/PngImagePlugin.py` | \b\d{4}[-/]\d{2}[-/]\d{2}\b | 17 |

> ⚠️ 위 파일에서 개인정보 또는 민감 정보 패턴이 탐지되었습니다. 검토 후 조치하세요.

### 노출된 .env 파일
- ⚠️ `projects/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/hermes-agent/.env.example` (.gitignore 확인 필요)
- ⚠️ `.hermes/skills/openclaw-imports/notion/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/profiles/reviewer/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/profiles/reviewer/skills/openclaw-imports/notion/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/profiles/developer/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/profiles/researcher/.env` (.gitignore 확인 필요)
- ⚠️ `.hermes/migration/openclaw/20260512T222047/backups/Users/bearj/.hermes/.env` (.gitignore 확인 필요)

### SSH 키 파일 권한 문제
- ⚠️ known_hosts.old (권한: 644, 권장: 600)

## 4. 프로세스 이상 징후


### 고 CPU 사용 프로세스
- /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Pyth (CPU: 74.5%, MEM: 0.8%)

### 알 수 없는 리스닝 포트
- ⚠️ Port 4040: ngrok 1303 - 127.0.0.1:4040
- ⚠️ Port 5432: postgres 1313 - [::1]:5432
- ⚠️ Port 5432: postgres 1313 - 127.0.0.1:5432
- ⚠️ Port 41343: LM\x20Stu 1320 - 127.0.0.1:41343
- ⚠️ Port 1234: LM\x20Stu 1320 - 127.0.0.1:1234

## 5. 네트워크 점검

- ⚠️ 방화벽: 비활성화 또는 확인 필요

## 6. 디스크 사용량

| 마운트 | 사용량 |
|--------|--------|
| / | 9% |
| /System/Volumes/Data | 43% |
| Downloads | 36M |
| Documents | 4.0M |
| Desktop | 68K |
| .hermes | 2.8G |
| projects | 682M |


## 7. 종합 권고사항

• 시스템 에러 21건 확인 필요
• 민감 정보 포함 파일 20건 - 검토 및 암호화 필요
• 알 수 없는 리스닝 포트 5건 - 확인 필요

---

*본 리포트는 자동 생성되었습니다. 의심스러운 징후가 발견되면 즉시 조치하세요.*

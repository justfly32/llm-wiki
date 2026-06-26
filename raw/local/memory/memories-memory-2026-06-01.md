---
source_file: /Users/bearj/.hermes/memories/MEMORY.md
ingested: 2026-06-01
sha256: 66d915e21254
category: memory
original_title: Memory
---

후
§
보고서 생성 파이프라인: 리서치 병렬 수집 → 통합 HTML 보고서 작성 → HTML 기반 python-pptx로 PPTX 변환 → 품질 검증. PPTX를 먼저 만들거나 HTML과 병렬로 만들지 말 것. 반드시 HTML 완료 후 PPTX 변환.
§
스킬 사용 규칙: 요청 시 반드시 관련 스킬을 먼저 찾아서 적용할 것. 특히 파일 업로드(gdrive-upload), 카카오톡(kakao-chat-to-sheets), 코딩 관리(coding-kanban) 등. 스킬은 ~/.hermes/skills/ 또는 시스템 skills_list에서 확인 가능.
§
KakaoTalk.app은 /Applications에 없음. `open -b com.kakao.KakaoTalkMac`으로 실행.
§
사용자 위치: 인천 (Incheon). 거주지/주 활동 지역.
§
Personal site: repo is ~/projects/post1 (GitHub: justfly32/post1). Build: cd ~/projects/post1 && python3 scripts/generate_site.py --memories-dir /Users/bearj/.hermes/memories/daily_memories/ --cron-file /Users/bearj/.hermes/cron/jobs.json --output index.html. URL: https://justfly32.github.io/post1. Timeline detail fix: template uses {% if item.detail %} — {{ item.detail }}{% endif %}.
§
디렉토리 규칙: ~/projects/ = 코드/개발 소스, ~/documents/ = 결과물(PPT, PDF, 보고서, 문서).
- 새 코드는 반드시 ~/projects/ 또는 ~/coding_projects/ 하위에 생성
- 새 프로젝트 시작 시 README.md 필수 작성
- 프로젝트 구조: docs/, src/, tests/, config/
- ~/Desktop, ~/Downloads 등에 직접 생성 금지
§
2026-05-28: personal-site repo is ~/projects/post1 (GitHub: justfly32/post1). generate_site.py, cron_reader.py, templates/base.html are in post1. GitHub Pages URL: https://justfly32.github.io/post1
§
2026-05-28: generate_site.py 타임라인 표시 수정 - 메모리 파일에 " — " 구분자가 없으면 detail이 빈 문자열로 표시됨. 템플릿을 {% if item.detail %} — {{ item.detail }}{% endif %}로 수정.
§
사용자 워크플로 선호 (2026-05-28):
- 보고서 요청 시: 칸반 작업 분해 → HTML(basic-design-1) → PPT(html2pptx) → Google Drive 업로드 전체 파이프라인 실행
- 데이터 원칙: 객관적 자료 우선, 없으면 사용자에게 요청. 데이터 조작/허위 자료 금지
- Notion: Agent사용기 363ad27653ad800f81e3e599cfe83623, 주식분석 368ad27653ad8141a1f2c8fb43464fff
- 법률 AI 사업 보고서 작성 완료 (2026-05-28, Google Drive 업로드 완료)
§
2026-06-01 완료: DB온톨로지(35/35), 일본사/한국사/지구사 교육시리즈, NetMaster(~/coding_projects/netmaster/), LLM Wiki(~/wiki/ — CLI + Obsidian웹UI port 8090). 웹UI는 hermes venv python으로 실행 필수.
§
2026-06-01: Google OAuth 토큰 재인증 완료. refresh_token 만료(invalid_grant) → setup.py --auth-url → 사용자 브라우저 수동 인증 → --auth-code 교환. gdrive-upload 정상 작동 확인. 브라우저 자동화로 Google OAuth 불가(봇 감지).
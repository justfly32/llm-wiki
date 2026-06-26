---
source_file: /Users/bearj/.hermes/memories/MEMORY.md
ingested: 2026-06-12
sha256: 4365432a19af
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
Notion DB: Agent사용기 363ad27653ad800f81e3e599cfe83623, 주식분석 368ad27653ad8141a1f2c8fb43464fff
§
Notion DB: 주식분석 368ad27653ad8141a1f2c8fb43464fff
§
n8n MCP 설정 요청 (2026-06-08): n8n 워크플로우 도구를 MCP로 Hermes에 연결하는 작업.
§
n8n 로컬 인스턴스: http://localhost:5678, 계정: admin@bearj.local / MyN8nPass123!, DB: ~/.n8n/database.sqlite, 암호화키: AUIM8oLJ8w7z4niiyY5z+aItlFL3F05c
§
Google Drive 토큰 갱신 작업 시작 (2026-06-09)
§
멀티 에이전트 프로필 생성 시스템 (2026-06-09): 문서 hermes profiles 가이드 기반으로 구축. developer/researcher/reviewer 3개 프로필 생성 완료.
§
사용자 의사결정 스타일: "나머지는 너가 최선이라고 생각하는 걸로 해" → 확인 질문 없이 바로 구현. 과도한 확인 금지. 결과물 우선 (구현 → 보여주기 → 피드백).
§
design-to-code 스킬 사용자 선호: HTML/CSS 우선 출력, 코드 설명보다 동작하는 결과물 먼저 보여주기, "최선이라고 생각하는 걸로 해"라고 하면 확인 없이 바로 구현. 과도한 확인 질문 금지.
§
design-to-code 스킬 v1.1.0 업데이트 (2026-06-11): CSS 리셋 템플릿 추가, 컴포넌트 라이브러리 매핑 16종으로 강화, 변형/크기 자동 감지, 중첩 방지 로직(parent_is_component), 자식 텍스트 노드 처리(characters 필드 직접 렌더링), input placeholder 변환, reset.css 자동 복사. 스크립트: scripts/figma_to_html.py (800라인).
§
사용자 GitHub 레포지토리 구조: (1) justfly32/post1 — 개인 블로그/메모리 사이트 (figma-design.html 포함), (2) justfly32/justfly32.github.io — GitHub Pages 메인 페이지. 두 레포는 별도로 관리됨.
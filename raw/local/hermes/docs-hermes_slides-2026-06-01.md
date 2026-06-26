---
source_file: /Users/bearj/projects/hermes_ops/docs/Hermes_Slides.md
ingested: 2026-06-01
sha256: 1ce15b4424e2
category: hermes
original_title: Hermes Agent 가이드
---

---
marp: true
theme: uncover
class: invert
paginate: true
---

# Hermes Agent 가이드
### 초보자를 위한 설치 및 사용법

---

# 1. 설치하기
- 터미널(Terminal) 앱을 엽니다.
- 다음 설치 스크립트를 입력하세요:
  `curl -sSL https://hermes-agent.nousresearch.com/install.sh | bash`

---

# 2. 초기 설정
- 터미널에 `hermes setup` 입력
- API 키 및 모델 선택 진행
- 안내에 따라 텔레그램/슬랙 연결

---

# 3. 핵심 명령어
- `hermes help`: 전체 도움말 확인
- `hermes config`: 시스템 설정 변경
- `hermes tools`: 활용 가능한 도구 목록 조회

---

# 4. 문제 해결 (FAQ)
- **명령어가 안 될 때**: 설치 경로가 `$PATH`에 있는지 확인
- **연결 문제 발생 시**: `hermes reconnect` 명령어로 재연결

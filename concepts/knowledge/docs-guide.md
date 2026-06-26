---
title: Hermes Agent 설치 및 초보자 가이드
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [hermes, ai-ml, tool, api]
sources: [raw/local/hermes/docs-guide-2026-06-01.md]
source_file: /Users/bearj/projects/hermes_ops/docs/guide.md
confidence: high
links: [[docs-hermes_beginner_guide|Hermes 초보자 가이드]], [[docs-hermes_final_guide|Hermes 완벽 가이드]], [[docs-hermes_slides|Hermes 슬라이드]], [[best-practice-claude-subagents|Claude Subagents 모범 사례]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]], [[hermes-guide-beginner_guide|Hermes 가이드 문서]]
---

# Hermes Agent 설치 및 초보자 가이드

> 관련: [[docs-hermes_beginner_guide|상세 초보자 가이드]], [[docs-hermes_final_guide|완벽 가이드]], [[best-practice-claude-subagents|Claude 서브에이전트 베스트 프랙티스]]도 참고하세요.

> 📁 원본: `/Users/bearj/projects/hermes_ops/docs/guide.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: hermes

## 내용

# Hermes Agent 설치 및 초보자 가이드

## 1. 개요
Hermes Agent는 터미널을 기반으로 AI와 협업할 수 있는 강력한 생산성 도구입니다. 이 가이드는 초보자를 위해 설치부터 기초 명령어까지 상세히 안내합니다.

## 2. 설치 단계
1. **시스템 요구사항 확인**: macOS / Linux 환경을 권장합니다.
2. **설치 명령 실행**: 터미널에 다음 명령어를 입력하세요.
   ```bash
   curl -sSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```
3. **환경 변수 설정**: 설치 후 `source ~/.bashrc` 또는 `source ~/.zshrc`를 실행하여 적용하세요.

## 3. 초기 설정
- `hermes setup` 명령어를 입력하여 API 키와 모델 설정을 진행하세요.
- 첫 연결 시, 플랫폼(Telegram/Slack) 연동이 자동으로 안내됩니다.

## 4. 자주 사용하는 명령어
- `hermes help`: 전체 도움말 확인
- `hermes config`: 설정 변경
- `hermes tools`: 사용 가능한 도구 목록 조회

## 5. 자주 묻는 질문 (FAQ)
- **Q: 명령어가 실행되지 않아요.**
  - A: `hermes`가 설치된 경로가 `$PATH`에 포함되어 있는지 확인하세요.
- **Q: 플랫폼 연결이 끊겼어요.**
  - A: `hermes reconnect` 명령어를 실행해보세요.


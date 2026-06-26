---
source_file: /Users/bearj/Documents/hermes-guide/beginner_guide.md
ingested: 2026-06-01
sha256: 37646a71ef61
category: hermes
original_title: Hermes Agent 초보자 가이드
---

# Hermes Agent 초보자 가이드

## 1. 개요
Hermes Agent는 Nous Research에서 제공하는 강력한 자율형 AI 에이전트 프레임워크입니다. 이 가이드는 Hermes Agent를 처음 접하는 사용자를 위해 설계되었습니다.

## 2. 시작하기 (Quick Start)
1. 환경 설정: Python 환경이 구성되어 있는지 확인합니다.
2. 설치: `pip install hermes-agent` (해당 환경에 맞게 설치)
3. 첫 실행: 터미널에서 `hermes` 명령어를 입력하여 대화형 인터페이스를 실행합니다.

## 3. 핵심 도구 활용법
- `terminal()`: 외부 명령어를 실행하여 파일 및 시스템을 제어합니다.
- `read_file()`/`write_file()`: 파일 내용을 읽거나 작성합니다.
- `search_files()`: 파일 시스템 내에서 정보를 검색합니다.

## 4. 모범 사례 (Best Practices)
- **절대 경로 사용**: 모든 작업은 프로젝트 루트를 기준으로 한 절대 경로를 사용하세요.
- **검증 우선**: 파일 변경 전 항상 `read_file`로 내용을 확인하세요.
- **간결한 커뮤니케이션**: 명확하고 효율적인 도구 사용을 우선시하세요.

## 5. 추가 리소스
- 공식 문서: https://hermes-agent.nousresearch.com/docs

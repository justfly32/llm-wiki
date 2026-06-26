---
title: Code Edu Lab Curriculum
created: 2026-06-26
updated: 2026-06-26
type: knowledge
tags: [education, curriculum, python, flask, nextjs, sqlite, web-development]
links: [[2026-06-25|Daily Log 2026-06-25]], [[hermes-guide-beginner_guide|Hermes Guide]]
---

# Code Edu Lab 커리큘럼 메뉴얼

> **Code Edu Lab**은 코딩 교육을 위한 4개 스택의 대시보드 프로젝트입니다.
> 하나의 공유 SQLite 데이터베이스를 Python Streamlit, Python Flask, Node.js Express, Next.js에서 각각 접속하여 데이터를 다루는 방법을 배웁니다.

## 아키텍처

```
공유 SQLite DB (edu.db)
    ├── Python Streamlit  (포트 8501)  → 인터랙티브 대시보드
    ├── Python Flask      (포트 5000)    → 웹 대시보드
    ├── Node.js Express   (포트 3001)    → REST API 서버
    └── Next.js           (포트 3000)    → 프론트엔드 (Express API 연동)
```

## 데이터베이스 스키마

| 테이블 | 용도 | 주요 필드 |
|--------|------|-----------|
| `students` | 학생 정보 | id, name, email, created_at |
| `courses` | 과목 정보 | id, title, instructor, description, level |
| `enrollments` | 수강 신청 | id, student_id, course_id, grade |
| `lessons` | 강의 내용 | id, course_id, title, content, order_num |
| `submissions` | 과제 제출 | id, student_id, lesson_id, code_text, score |
| `curriculum_modules` | 커리큘럼 모듈 | id, course_id, title, order_num, difficulty |
| `curriculum_steps` | 학습 단계 | id, module_id, instruction, code_example, expected_output |
| `student_progress` | 학습 진도 | id, student_id, step_id, status, completed_at |

## 4개 과정 요약

### 1. Python 기초 (course_id=1)
- 대상: 김민수, 이서연
- 난이도: beginner → intermediate
- 예상 시간: 125분
- 모듈: Python 설치 → 변수/자료형 → 조건문/반복문

### 2. Flask 웹개발 (course_id=2)
- 대상: 박지훈, 최유진
- 난이도: beginner → intermediate
- 예상 시간: 125분
- 모듈: Flask 설치 → 라우팅 → 템플릿 렌더링 (Jinja2)

### 3. Node.js Express (course_id=3)
- REST API 서버 구축
- 포트 3001

### 4. Next.js 프론트엔드 + Streamlit 데이터
- Next.js: 포트 3000, Express API 연동 프론트엔드
- Streamlit: 포트 8501, 인터랙티브 대시보드

## 핵심 교육 포인트

1. **공유 DB 패턴**: 하나의 SQLite DB를 4개 프레임워크에서 접근하는 실전 패턴
2. **스택 비교**: 동일한 작업을 4가지 방식으로 구현하여 각 스택의 특성 이해
3. **진도 관리 시스템**: student_progress 테이블로 학습 단계별 추적
4. **과제 제출**: submissions 테이블에 코드 텍스트 + 점수 기록

## 프로젝트 경로

- 소스: `~/projects/code-edu-lab/`
- DB 초기화: `cd shared/db && python3 seed.py && python3 migrate_curriculum.py`

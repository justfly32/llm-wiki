---
title: "llm-wiki 개선 계획 (2026-06-26)"
created: 2026-06-26
updated: 2026-06-26
type: project
tags: [llm-wiki, improvement, plan, automation]
links: [[wiki-py|wiki.py]], [[web-py|web.py]], [[wiki-rag-py|wiki_rag.py]]
---

# LLM Wiki 개선 계획

## 현황 분석

| 항목 | 현재 상태 | 개선 필요 |
|------|-----------|-----------|
| 검색 엔진 | BM25 (keyword only) | Vector 임베딩 하이브리드 필요 |
| RAG | BM25 + OpenRouter LLM | 컨텍스트 윈도우, 스트리밍, 멀티턴 |
| 그래프 뷰 | D3.js 정적 그래프 | 3D 포스 레이아웃, 실시간 필터 |
| UI | Obsidian-style | Ctrl+K 글로벌 검색, 인라인 편집 |
| 수집 파이프라인 | arXiv + HN | RSS, 블로그, 트위터 추가 |
| 백업 | ❌ 없음 | Git 자동 백업 필요 |
| 페이지 수 | ~111 | → 300+ 목표 |

## 1단계: 검색 엔진 업그레이드 (Vector + BM25 하이브리드)

### 목표
- BM25 키워드 검색 + Sentence-Transformer 벡터 검색 조합
- 유사도 기반 추천 정확도 향상
- 300+ 페이지에도 대응 가능한 확장성

### 구현
```python
# wiki_rag.py 에 hybrid_search() 추가
# - BM25 점수 + cosine similarity 가중 합산
# - sentence-transformers/all-MiniLM-L6-v2 (로컬)
# - 임베딩 캐싱 (pickle)
```

## 2단계: 지식 그래프 2.0

### 목표
- 3D 포스 레이아웃 (three.js 기반)
- 노드 클릭 시 연결된 컨텐츠 필터링
- 타입별 노드 색상/크기 차별화

## 3단계: AI Assistant 강화

### 목표
- 스트리밍 응답 (SSE)
- 멀티턴 대화 컨텍스트 유지
- 코드 블록 구문 강조
- 관련 페이지 자동 추천 개선

## 4단계: UI/UX 개선

### 목표
- Ctrl+K 글로벌 검색 모달
- 더블클릭으로 마크다운 인라인 편집
- 모바일 반응형 레이아웃
- 다크/라이트 테마 토글
- 페이지 프리뷰 툴팁 (호버 시 요약)

## 5단계: 수집 파이프라인 확장

### 목표
- RSS 피드 구독 (기술 블로그, 뉴스레터)
- 특정 블로그/사이트 변경 감시
- 수집된 내용 자동 분류 및 태깅

## 6단계: 백업 및 동기화

### 목표
- Git 저장소에 주기적 푸시 (cron)
- daily 변경사항 자동 커밋
- github.com/justfly32/llm-wiki 에 미러링

---
title: "llm-wiki 개선 요약"
created: 2026-06-26
updated: 2026-06-26
type: project
tags: [llm-wiki, improvement, changelog]
links: [[llm-wiki-improvement-plan|개선 계획]]
---

# LLM Wiki 개선 내역

## 1단계: 하이브리드 검색 엔진 ✅ (진행 중)

- [x] wiki_rag.py 에 SentenceTransformer 기반 벡터 검색 추가
- [x] BM25 + Cosine Similarity 가중 합산 하이브리드 검색
- [ ] 로컬 임베딩 캐싱 (pickle)
- [ ] 유사도 기반 추천 더욱 정확하게

## 2단계: UI/UX 개선 (예정)

- [ ] Ctrl+K 글로벌 검색 모달
- [ ] 모바일 반응형
- [ ] 더블클릭 편집

## 3단계: AI Assistant 개선 (예정)

- [ ] 스트리밍 응답
- [ ] 멀티턴 대화

## 4단계: 수집 파이프라인 (예정)

- [ ] RSS 피드 구독
- [ ] 블로그 감시

## 5단계: Git 백업 (예정)

- [ ] 자동 커밋 cron
- [ ] GitHub 미러링

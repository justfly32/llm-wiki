---
title: Phase 1-4 & 1-5: 연관관계 유형 상세 정의 + 기술 스택 선정
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [project, programming, python, devops, api]
sources: [raw/local/project/docs-phase1-4-5-relationship-techstack-2026-06-01.md]
source_file: /Users/bearj/coding_projects/db-ontology/docs/phase1-4-5-relationship-techstack.md
confidence: high
links: [[docs-phase1-3-target-databases|대상 DB 목록]], [[docs-phase1-planning|Phase 1 기획]], [[plans-web-terminal-plan|Web Terminal 계획]], [[security_reports-latest|최신 보안 리포트]]
---

# Phase 1-4 & 1-5: 연관관계 유형 상세 정의 + 기술 스택 선정

> 관련: [[docs-phase1-3-target-databases|대상 DB 목록]], [[docs-phase1-planning|Phase 1 기획 문서]]를 참고하세요.

> 📁 원본: `/Users/bearj/coding_projects/db-ontology/docs/phase1-4-5-relationship-techstack.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: project

## 내용

# Phase 1-4 & 1-5: 연관관계 유형 상세 정의 + 기술 스택 선정

## 연관관계 유형 상세

### 유형 A: 구조적 관계 (Structural Relationship)

#### A1. 외래키 (Foreign Key)
```sql
-- 탐지 쿼리 (PostgreSQL)
SELECT
    tc.table_schema, tc.table_name, kcu.column_name,
    ccu.table_schema AS foreign_schema,
    ccu.table_name AS foreign_table,
    ccu.column_name AS foreign_column
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY';
```
- **신뢰도**: 0.95 (명시적 선언)
- **자동 채택**: YES

#### A2. 인덱스 기반 관계
- 동일 컬럼명 + 인덱스 패턴으로 추론
- 예: `idx_order_user_id` → `user_id` FK 추정
- **신뢰도**: 0.70

#### A3. JOIN 패턴 (쿼리 로그)
```python
# SQL 파싱으로 JOIN 관계 추출
import sqlparse
parsed = sqlparse.parse(query)
for token in parsed[0].flatten():
    if token.ttype is None and isinstance(token, sqlparse.sql.Comparison):
        # "table1.col = table2.col" 패턴 추출
        pass
```
- **신뢰도**: 0.85 (실제 사용 관계)

### 유형 B: 명명 패턴 관계 (Naming Pattern)

#### B1. 정확 매칭
```python
# 동일 필드명 매칭
exact_matches = {}
for col in all_columns:
    key = col.name.lower()
    if key in exact_matches:
        exact_matches[key].append(col)
    else:
        exact_matches[key] = [col]
# user_id가 여러 테이블에 존재 → 관계 후보
```
- **신뢰도**: 0.90

#### B2. 정규화 매칭 (Normalization)
```python
import re
def normalize(name):
    # userId → user_id, UserID → user_id
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    s = re.sub(r'[\s\-]', '_', s)
    return s.lower()

# user_id ≈ userId ≈ usr_id ≈ USER_ID
```
- **신뢰도**: 0.75

#### B3. 접두사/접미사 그룹핑
```python
# order_id, order_date, order_status → "order" 도메인
# user_name, user_email, user_phone → "user" 도메인
from collections import defaultdict
domains = defaultdict(list)
for col in all_columns:
    prefix = col.name.split('_')[0]  # 간단한 분리
    domains[prefix].append(col)
```
- **신뢰도**: 0.60

#### B4. 동의어 매칭
```python
# 사전 기반 동의어 매칭
synonyms = {
    'customer': ['client', 'buyer', 'purchaser', 'consumer'],
    'product': ['item', 'goods', 'merchandise', 'sku'],
    'order': ['purchase', 'transaction', 'deal'],
    'user': ['account', 'member', 'person', 'employee'],
    'address': ['location', 'place', 'residence'],
    'phone': ['telephone', 'mobile', 'cell', 'contact'],
    'email': ['mail', 'e_mail', 'electronic_mail'],
    'name': ['title', 'label', 'display_name'],
    'date': ['time', 'timestamp', 'created_at', 'updated_at'],
    'amount': ['price', 'cost', 'fee', 'total', 'sum'],
    'status': ['state', 'condition', 'stage', 'phase'],
    'description': ['desc', 'detail', 'note', 'comment', 'memo'],
}
```
- **신뢰도**: 0.50

### 유형 C: 데이터 유사도 (Data Similarity)

#### C1. 값 중복도 (Jaccard Similarity)
```python
def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union 

...(내용 생략)...

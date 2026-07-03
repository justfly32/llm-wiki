---
title: KV Cache (Key-Value Cache)
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [kv-cache, inference, optimization, transformer, llm, attention]
links: [[attention-mechanism]], [[transformer-architecture]]
---

# KV Cache (Key-Value Cache)

> **KV Cache**는 LLM 추론(inference) 속도를 획기적으로 높이는 최적화 기술입니다.
> 생성 과정에서 이전에 계산된 Key와 Value 행렬을 재사용하여 중복 계산을 제거합니다.

## 문제: Autoregressive Generation의 비효율

LLM이 텍스트를 생성할 때는 **한 번에 한 토큰씩** 순차적으로 생성합니다.

```
Step 1: "나는" → K₁, V₁ 계산
Step 2: "나는 학교" → "나는"의 K₁,V₁ + "학교"의 K₂,V₂ 계산 (K₁,V₁ 중복!)
Step 3: "나는 학교에" → "나는"의 K₁,V₁ + "학교"의 K₂,V₂ + "에"의 K₃,V₃ 계산 (K₁,V₁,K₂,V₂ 중복!)
```

**문제**: 매 step마다 **이전 모든 토큰의 K, V를 다시 계산** → O(n²) 불필요

## 해결: KV Cache

### 동작 원리

```
KV Cache 초기: []

Step 1: Input = "나는"
  → K₁, V₁ 계산
  → Cache: [(K₁, V₁)]
  → 출력: "학교"

Step 2: Input = "학교"  
  → K₂, V₂ 계산
  → Cache: [(K₁, V₁), (K₂, V₂)]
  → 전체 Attention = Attention(Q₂, [K₁,K₂], [V₁,V₂])
  → 출력: "에"

Step 3: Input = "에"
  → K₃, V₃ 계산
  → Cache: [(K₁, V₁), (K₂, V₂), (K₃, V₃)]
  → 전체 Attention = Attention(Q₃, [K₁,K₂,K₃], [V₁,V₂,V₃])
  → 출력: "간다"
```

**결과**: 각 step에서는 **현재 토큰의 K, V만 계산**하면 됨 → O(n)으로 감소

### 성능 비교

| 항목 | KV Cache 없음 | KV Cache 사용 | 개선 |
|------|---------------|---------------|------|
| 계산 복잡도 | O(n³) | O(n²) | **O(n) 감소** |
| Step당 계산 | 모든 토큰 재계산 | 현재 토큰만 계산 | 수백 배 |
| 메모리 사용 | 낮음 (임시) | 높음 (O(n×d_k×h×l)) | - |

## 메모리 사용량

KV Cache가 차지하는 메모리는 모델 크기와 컨텍스트 길이에 따라 **선형**으로 증가합니다.

### 계산 공식

```
KV Cache 크기 = 2 (K, V) × n_layers × n_heads × d_head × seq_len × dtype_bytes
```

### 실제 예시

| 모델 | 파라미터 | Layers | Heads | d_head | 4K 토큰 | 32K 토큰 | 128K 토큰 |
|------|----------|--------|-------|--------|---------|----------|-----------|
| LLaMA 7B | 7B | 32 | 32 | 128 | **~1GB** | ~8GB | ~32GB |
| LLaMA 13B | 13B | 40 | 40 | 128 | ~1.6GB | ~12.8GB | ~51GB |
| LLaMA 70B | 70B | 80 | 64 | 128 | ~5GB | ~40GB | ~160GB |
| GPT-4 (추정) | 1.8T | - | - | - | ~50GB+ | >400GB | >1.6TB |

> **💡 중요**: 128K 컨텍스트에서는 KV Cache가 모델 가중치보다 더 많은 메모리를 차지합니다!

## KV Cache 최적화 기술

### 1. Multi-Query Attention (MQA)

모든 Query 헤드가 **1개의 Key/Value 헤드**를 공유합니다.

```
일반 MHA: 32 Q 헤드 × 32 K 헤드 × 32 V 헤드 → KV Cache 큼
MQA:      32 Q 헤드 × 1 K 헤드 × 1 V 헤드 → KV Cache 1/32!
```

- 사용 모델: PaLM, Falcon
- 장점: KV Cache 1/32, 추론 속도 ↑
- 단점: 표현력 감소 가능

### 2. Grouped Query Attention (GQA)

MHA와 MQA의 절충안입니다. Q 헤드를 그룹으로 묶고, 그룹당 1개의 KV 헤드를 할당합니다.

```
LLaMA 2 70B: 64 Q 헤드, 8 KV 헤드 (GQA-8) → KV Cache 1/8
LLaMA 3 70B: 64 Q 헤드, 8 KV 헤드 (GQA-8) → KV Cache 1/8
Mistral 7B:  32 Q 헤드, 8 KV 헤드 (GQA-8) → KV Cache 1/4
```

### 3. KV Cache Quantization

KV Cache를 FP16 → INT8/INT4로 양자화하여 메모리 감소.

| 양자화 | 메모리 | 품질 손실 |
|--------|--------|-----------|
| FP16 (기준) | 1× | 없음 |
| INT8 | 0.5× | 거의 없음 |
| INT4 (NF4) | 0.25× | 약간 있음 |
| INT2 | 0.125× | 품질 저하 |

- 구현: vLLM, llama.cpp에서 지원
- KVCache Quantization 기법: KIVI, GEAR

### 4. PagedAttention / vLLM

- KV Cache를 **고정 크기 페이지**로 분할하여 관리
- OS의 가상 메모리 페이지처럼 **비연속적 메모리 할당** 가능
- 메모리 단편화 제거 → 최대 2-4배 throughput 향상

### 5. Windowed KV Cache (Sliding Window)

- 최근 N개 토큰의 KV만 캐싱하고, 오래된 것은 폐기
- Mistral (8K 슬라이딩 윈도우)에서 사용
- 긴 컨텍스트에서 메모리 사용량 일정하게 유지

## Prefill vs Decode

LLM 추론은 두 단계로 나뉩니다:

| 단계 | 설명 | KV Cache | 계산 특성 |
|------|------|----------|-----------|
| **Prefill** | 프롬프트 전체를 한 번에 처리 | 초기 Cache 생성 | 계산 집약적 (compute-bound) |
| **Decode** | 한 토큰씩 생성 (추론) | Cache 읽기 + 추가 | 메모리 집약적 (memory-bound) |

### Prefill Phase
```
입력: "Translate to Korean: Hello, how are you?"
→ 모든 토큰의 KV를 병렬 계산
→ KV Cache 생성 완료 (15개 토큰)
```

### Decode Phase
```
Step 1: Q="[start]" → Cache 참조 → "안녕"
Step 2: Q="안녕" → Cache 참조 + (K_안녕, V_안녕) 추가 → "하세요"
Step 3: Q="하세요" → Cache 참조 + (K_하세요, V_하세요) 추가 → "?"
...
```

## Shared Prefix KV Cache

채팅 애플리케이션에서 **시스템 프롬프트**는 항상 동일합니다.

```
시스템 프롬프트: "You are a helpful AI assistant..."
┌─────────────────────────────────┐
│ Shared Prefix (모든 요청 공통)    │ ← KV Cache 공유 가능
├─────────────────────────────────┤
│ User 1: "날씨 알려줘"             │
│ User 2: "시 분석해줘"             │
└─────────────────────────────────┘
```

**기법**: Prefix Caching — 동일한 프롬프트 앞부분의 KV Cache를 재사용하여 Prefill 생략

- vLLM: Automatic Prefix Caching (APC)
- Claude/GPT: 시스템 프롬프트 KV Cache 공유

## 참고

- [[attention-mechanism]]: Attention의 상세 동작
- [[transformer-architecture]]: Transformer 구조
- [vLLM: PagedAttention 논문](https://arxiv.org/abs/2309.06180)
- [MQA: Fast Transformer Decoding 논문](https://arxiv.org/abs/1911.02150)

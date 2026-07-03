---
title: Attention Mechanism
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [attention, transformer, llm, deep-learning, multi-head-attention, self-attention]
links: [[transformer-architecture]], [[kv-cache]], [[feed-forward-network]]
---

# Attention Mechanism

> **Attention**은 "무엇에 집중할지"를 학습하는 메커니즘입니다.
> Transformer의 핵심으로, 시퀀스 내 모든 토큰 쌍 간의 관계를 한 번에 계산합니다.

## 기본 개념

Attention의 직관: **Query가 Key들을 보고, 각 Key에 해당하는 Value를 가중합한다.**

```
낱말은 → 강아지가 → 공원을 → 달린다
  [Q]      [K1,V1]   [K2,V2]   [K3,V3]

  "강아지가" ← 가장 높은 Attention 점수
  "공원을"   ← 중간 점수
```

## Scaled Dot-Product Attention

### 수식

$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V $$

### 단계별 동작

| 단계 | 연산 | 결과 모양 | 설명 |
|------|------|-----------|------|
| 1. Query × Key^T | $Q K^T$ | (seq_len, seq_len) | 모든 토큰 쌍의 유사도 행렬 |
| 2. Scaling | $÷ \sqrt{d_k}$ | (seq_len, seq_len) | 그라디언트 안정화 (softmax 포화 방지) |
| 3. Mask (선택) | $-∞$ | (seq_len, seq_len) | 미래 토큰 가리기 (Decoder) |
| 4. Softmax | $softmax$ | (seq_len, seq_len) | 확률 분포로 정규화 |
| 5. × Value | $× V$ | (seq_len, d_v) | 각 토큰의 가중합 = 문맥 표현 |

### 왜 $\sqrt{d_k}$ 로 나누는가?

- d_k가 크면 Q×K^T 값이 커져 softmax가 극단값(0 또는 1)으로 포화됨
- 그라디언트가 매우 작아져 학습이 어려워짐
- $\sqrt{d_k}$ 로 나누면 분산이 1로 정규화됨

## Multi-Head Attention

### 개념

단일 Attention을 h개 병렬로 실행하고 결과를 합칩니다.

```
입력
  │
  ├── Head 1: Q₁←Wq₁, K₁←Wk₁, V₁←Wv₁ → Attention₁ → Z₁
  ├── Head 2: Q₂←Wq₂, K₂←Wk₂, V₂←Wv₂ → Attention₂ → Z₂
  ├── ...
  └── Head h: Qₕ←Wqₕ, Kₕ←Wkₕ, Vₕ←Wvₕ → Attentionₕ → Zₕ
                                          │
                              Concat(Z₁...Zₕ)
                              │
                              Linear(Wo)
                              │
                              출력
```

### 장점

| 장점 | 설명 |
|------|------|
| **다양한 관계 포착** | 각 헤드가 다른 종류의 관계 학습 (구문적, 의미적, 위치적) |
| **표현력 향상** | 단일 Attention보다 더 풍부한 문맥 표현 가능 |
| **병렬 처리** | h개 헤드가 독립적이므로 GPU 병렬 계산에 최적 |

### 실제 예 (GPT-3: 96 layers, 96 heads)

- Layer 1-10: 인접 토큰 관계 (로컬 패턴)
- Layer 20-40: 구문적 관계 (주어-동사, 명사-형용사)
- Layer 60-80: 의미적 관계 (대명사 참조, 개체 간 관계)
- Layer 80+: 추상적 개념 (문서 수준의 관계)

## Attention의 세 가지 종류

### 1. Self-Attention (Encoder)

- Q, K, V가 모두 **같은 입력**에서 옴
- 각 토큰이 시퀀스 내 **모든 토큰**과 관계 계산
- 양방향 (Bidirectional) — BERT 계열

### 2. Masked Self-Attention (Decoder)

- Self-Attention과 동일하나 **미래 토큰을 마스킹**
- i번째 토큰은 1~i번째 토큰만 참조 가능
- 단방향 (Causal) — GPT 계열

### 3. Cross-Attention (Encoder-Decoder)

- **Q는 Decoder 입력**에서, **K, V는 Encoder 출력**에서 옴
- Decoder가 Encoder의 출력을 참조하여 생성
- 번역, 요약 등 Seq2Seq 작업

## 다양한 Attention 변형

| 변형 | 특징 | 사용 모델 |
|------|------|-----------|
| **Multi-Query Attention (MQA)** | 모든 Q 헤드가 1개의 KV 헤드 공유 → 추론 속도↑ | PaLM, Falcon |
| **Grouped Query Attention (GQA)** | Q 헤드 그룹별로 KV 헤드 할당 (MQA와 MHA의 절충) | LLaMA 2/3, Mistral |
| **Flash Attention** | GPU SRAM을 활용한 IO-aware Attention → 메모리↓ 속도↑ | 거의 모든 최신 모델 |
| **Sliding Window Attention** | 고정된窗口 크기만 Attention → 선형 복잡도 | Mistral, Mixtral |
| **Sparse Attention** | 일부 토큰 쌍만 Attention → O(n²) → O(n log n) | Longformer, BigBird |
| **Linear Attention** | Kernel trick으로 O(n²) → O(n) | Performer, Linformer |

## Attention의 계산 복잡도

$$ O(n^2 \cdot d_k) $$

- **n**: 시퀀스 길이 (토큰 수)
- **d_k**: Key/Query 차원
- **문제**: n이 커지면 제곱으로 증가 (GPT-4 context 128K의 경우 매우 큰 비용)

### 해결 방안

1. **Flash Attention**: 메모리 최적화로 실제 계산 속도 향상
2. **Ring Attention**: 분산 메모리로 긴 컨텍스트 처리
3. **Infini-Attention**: 압축 메모리 + Attention 결합

## 참고

- [[transformer-architecture]]: Transformer 전체 구조
- [[kv-cache]]: KV Cache를 통한 추론 최적화
- [[feed-forward-network]]: Attention 이후 FFN 처리

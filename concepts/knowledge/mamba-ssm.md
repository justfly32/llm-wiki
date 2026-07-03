---
title: Mamba & State Space Models (SSM)
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [mamba, ssm, state-space-model, structured-state-space, s4, llm, alternative-architecture]
links: [[transformer-architecture]], [[attention-mechanism]]
---

# Mamba & State Space Models (SSM)

> **Mamba**는 Transformer의 Attention을 대체하는 **State Space Model (SSM)** 기반 아키텍처입니다.
> 선형 복잡도 O(n)으로 긴 시퀀스를 효율적으로 처리하며, Transformer를 넘어설 차세대 아키텍처로 주목받습니다.

## 등장 배경

Transformer의 근본적 한계: **Attention의 O(n²) 복잡도**

| 시퀀스 길이 | Attention (O(n²)) | Mamba (O(n)) |
|-------------|-------------------|--------------|
| 1K | 1M 연산 | 1K 연산 |
| 8K | 64M 연산 | 8K 연산 |
| 128K | 16G 연산 | 128K 연산 |
| 1M | 1T 연산 | 1M 연산 |

> Mamba는 1M 길이의 시퀀스도 효율적으로 처리할 수 있습니다!

## State Space Model (SSM) 기본 개념

### 연속 시스템 표현

SSM은 입력 시퀀스를 **숨겨진 상태(hidden state)** 를 통해 매핑하는 시스템입니다.

```
  입력 u(t)  →  [  A, B, C, D  ]  →  출력 y(t)
                     │
              내부 상태 h(t)
```

수학적으로:

$$ h'(t) = A \cdot h(t) + B \cdot u(t) $$
$$ y(t) = C \cdot h(t) + D \cdot u(t) $$

- **h(t)**: 내부 상태 (N차원)
- **u(t)**: 입력 신호
- **y(t)**: 출력 신호
- **A**: 상태 천이 행렬 (State Transition) — 시스템의 "기억"을 결정
- **B**: 입력 투영 행렬 (Input Projection)
- **C**: 출력 투영 행렬 (Output Projection)
- **D**: 스킵 연결 (Skip Connection, 보통 0)

### S4 (Structured State Space Sequence Model)

S4는 SSM을 딥러닝에 적용한 최초의 성공적 모델입니다.

**핵혀신**: 행렬 A를 **대각(Diagonal) + 저랭크(Low-rank)** 구조로 제약

$$ A = \Lambda - P \cdot Q^T $$

- **Λ**: 대각 행렬 (Diagonal) — 계산 효율
- **P, Q**: 저랭크 수정 (Low-rank correction) — 표현력 유지

이 구조 덕분에 SSM이 긴 시퀀스에서도 **안정적**으로 동작합니다.

## Mamba (S6: Selective State Space Model)

### 기존 SSM의 한계

S4까지의 SSM은 **입력에 따라 상태 천이가 변하지 않음** (Linear Time-Invariant).

```
"S4: 모든 입력에 동일한 A, B, C 사용
     → "I went to the bank"의 'bank' (은행/강둑) 구분 불가
```

### Mamba의 혁신: 선택적(Selective) SSM

Mamba는 **입력에 따라 A, B, C를 동적으로 변경**합니다.

```
S6 (Mamba):
  B = Linear_B(x)   ← 입력에 따라 달라짐
  C = Linear_C(x)   ← 입력에 따라 달라짐
  A = parameter     ← 학습되지만 고정 (입력 무관)
  
  h(t+1) = A(t) · h(t) + B(t) · u(t)
  y(t) = C(t) · h(t)

  → "bank" 앞의 문맥에 따라 다른 처리 가능!
```

## Mamba 블록 구조

```
입력 x
  │
  ├──→ Linear (확장)
  │       │
  │       ├──→ SiLU (게이팅) ──┐
  │       │                    │
  │       └──→ Conv1D          │
  │               │            │
  │           SiLU             │
  │               │            │
  │          SSM (S6)          │
  │               │            │
  └────────────────────────────┘
              │ Element-wise 곱
              │
          Linear (축소)
              │
          Residual +
              │
          출력
```

### Transformer 블록과 비교

```
Transformer:                      Mamba:
  x → LN → Attention → + → LN → FFN → +    x → Conv → SSM → Gate → +
  │    O(n²)                  │            │    선형(O(n))         │
  └────────────────────────────┘            └───────────────────────┘
```

## Transformer vs Mamba

| 특성 | Transformer (Attention) | Mamba (SSM) |
|------|------------------------|-------------|
| **복잡도** | O(n²) | **O(n)** |
| **긴 컨텍스트** | 메모리/연산 폭발 | **효율적** |
| **추론 속도** | KV Cache 필요, 메모리 병목 | **상태만 유지, 매우 빠름** |
| **병렬화** | 매우 좋음 (전체 시퀀스 한 번에) | **제한적 (순차적 상태 업데이트)** |
| **학습 속도** | 빠름 (GPU 병렬화 최적화) | 느림 (순차 처리) |
| **하드웨어 친화성** | GPU에 최적화 | 미흡 (CUDA 커널 필요) |
| **In-Context Learning** | **매우 좋음** | 제한적 |
| **선행 연구** | 2017년 이후 방대함 | 2023년 이후 시작 |

## Mamba-2, Jamba, Hybrid 아키텍처

### Mamba-2 (2024)

| 개선점 | 설명 |
|--------|------|
| **SSD (State Space Dual)** | SSM과 Attention의 통합적 관점 |
| **단순화** | 게이팅 구조 간소화 |
| **성능 향상** | Mamba-1 대비 2-8x 학습 속도 향상 |
| **이론적 연결** | SSM과 Attention의 수학적 동치 관계 증명 |

### Jamba (AI21 Labs, 2024)

Mamba와 Attention을 **혼합(Hybrid)** 한 최초의 상용 모델입니다.

```
Jamba 블록:
  
  Layer 1:  Mamba (SSM)
  Layer 2:  Mamba (SSM)
  Layer 3:  Attention (유리수 레이어에만)
  Layer 4:  Mamba (SSM)
  Layer 5:  Mamba (SSM)
  Layer 6:  Attention
  ...
  
  + MoE (Mixture of Experts) 적용
```

| 장점 | 설명 |
|------|------|
| **효율성** | Attention을 1/8만 사용 → O(n²) 부담 감소 |
| **성능** | 순수 Mamba보다 높은 성능 (Attention의 in-context 능력 활용) |
| **유연성** | 필요한 비율로 Attention과 SSM 조합 가능 |

### 기타 하이브리드 모델

| 모델 | 구성 | 특징 |
|------|------|-------|
| **Mamba-2-Hybrid** | SSM + Attention | Mamba-2에 Attention 레이어 추가 |
| **Griffin (RWKV)** | Linear Attention + SSM | RNN과 Attention의 하이브리드 |
| **Receptance (RWKV)** | RNN 스타일 | Transformer와 RNN의 장점 결합 |
| **xLSTM** | LSTM 확장 | LSTM을 현대적으로 재해석 |

## 현재 평가 (2026년 기준)

### Mamba의 강점
- ✅ **극도로 긴 컨텍스트** (수백만 토큰)에 적합
- ✅ 추론 시 KV Cache 불필요 → 메모리 효율
- ✅ 선형 복잡도로 시퀀스 길이에 강건

### Mamba의 한계
- ❌ 학습 속도가 Transformer보다 느림 (하드웨어 최적화 부족)
- ❌ In-context learning 능력이 Transformer보다 부족
- ❌ 기존 GPU 생태계와의 호환성 (Flash Attention 등)

### 전망

| 시나리오 | 유리한 아키텍처 |
|----------|----------------|
| **일반 채팅 (4K-32K)** | Transformer (성숙도, 품질) |
| **초장문 처리 (100K+)** | **Mamba / Hybrid** |
| **모바일/엣지 추론** | **Mamba** (메모리 효율) |
| **최고 품질 필요** | Transformer (현재) |
| **비용 효율적 추론** | **Mamba / Jamba** |

> **결론**: 2026년 현재, 순수 Mamba가 Transformer를 완전히 대체하지는 못했습니다.
> 그러나 **Jamba 스타일의 Hybrid** (SSM + Attention + MoE)가 차세대 LLM 아키텍처의 유력한 방향입니다.

## 참고

- [Mamba 논문: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)
- [Mamba-2 논문: Transformers are SSMs](https://arxiv.org/abs/2405.21060)
- [Jamba 논문: Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887)
- [S4 논문: Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396)
- [[transformer-architecture]]: Transformer 구조 (비교 대상)
- [[attention-mechanism]]: Attention (Mamba가 대체하려는 대상)

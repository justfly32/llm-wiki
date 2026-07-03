---
title: Layer Normalization & Residual Connection
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [layer-norm, residual-connection, normalization, transformer, llm, deep-learning, rmsnorm]
links: [[transformer-architecture]], [[feed-forward-network]], [[attention-mechanism]]
---

# Layer Normalization & Residual Connection

> **Layer Normalization**과 **Residual Connection**은 Transformer의 깊은 네트워크를 안정적으로 학습시키는 두 가지 핵심 기술입니다.
> 이 두 기술이 없으면 100층이 넘는 LLM 학습은 사실상 불가능합니다.

## Residual Connection (Skip Connection)

### 개념

Residual Connection은 입력을 레이어 출력에 **직접 더하는** 연결입니다.

```
  x
  │
  ├──→ [Self-Attention / FFN] → F(x)
  │                              │
  └──────────────────────────────┘
                                 │
                                 + (덧셈)
                                 │
                          출력 = x + F(x)
```

수식: $$ \text{output} = x + F(x) $$

### 왜 필요한가?

| 문제 | Residual Connection의 해결 |
|------|---------------------------|
| **Vanishing Gradient** | 역전파 시 그라디언트가 직접 입력으로 흐르는 "고속도로" 제공 |
| **Exploding Gradient** | 덧셈 연산이 그라디언트 크기를 안정화 |
| **Degradation Problem** | 층이 깊어져도 성능 저하 없이 학습 가능 |
| **정보 흐름** | 하위 레이어의 정보가 상위 레이어까지 직접 도달 |

### Transformer에서 Residual 위치

```
입력 x
  │
  ├── [Multi-Head Attention] ──→ Dropout
  │                                │
  └────────────────────────────────┘
                                   │
                                   + (Residual #1)
                                   │
                                LayerNorm
                                   │
  ├── [Feed-Forward Network] ──→ Dropout
  │                                │
  └────────────────────────────────┘
                                   │
                                   + (Residual #2)
                                   │
                                LayerNorm
                                   │
                                출력
```

## Layer Normalization

### 개념

Layer Normalization은 각 샘플의 **특징 차원을 정규화**합니다.

```
입력: x = [x₁, x₂, ..., x_d] (d = d_model)

μ = mean(x) = (1/d) × Σx_i
σ² = variance(x) = (1/d) × Σ(x_i - μ)²

LayerNorm(x) = γ × (x - μ) / √(σ² + ε) + β
```

### Batch Normalization vs Layer Normalization

| 특성 | Batch Normalization | Layer Normalization |
|------|--------------------|--------------------|
| **정규화 방향** | 배치 차원 | 특징 차원 |
| **종속성** | 배치 크기에 의존 | 배치 크기와 무관 |
| **RNN/Transformer** | 부적합 (시퀀스 길이 가변) | **적합** |
| **학습 시** | 배치 통계 필요 | 각 샘플 독립적으로 계산 |
| **추론 시** | 이동 평균 사용 | 학습과 동일 |

> LayerNorm이 Transformer에 적합한 이유:
> 1. 시퀀스 길이가 달라도 각 토큰 독립적으로 정규화
> 2. 배치 크기가 작아도 안정적
> 3. Autoregressive generation과 호환

## Post-LN vs Pre-LN

Transformer에는 LayerNorm 위치에 따라 두 가지 방식이 있습니다.

### Post-LN (원본 Transformer)

```
x → Attention → Residual + Dropout → LayerNorm → FFN → Residual + Dropout → LayerNorm → 출력
```

- 사용: 원본 Transformer 논문 (2017)
- **문제**: 깊은 네트워크에서 불안정, Warmup 필수
- 학습 초반에 그라디언트 폭발 위험

### Pre-LN (현대 LLM 표준)

```
x → LayerNorm → Attention → Residual + Dropout → LayerNorm → FFN → Residual + Dropout → 출력
```

```
입력 x
  │
  LayerNorm  ← Pre-Normalization
  │
  Attention
  │
  + (Residual)
  │
  LayerNorm  ← Pre-Normalization
  │
  FFN
  │
  + (Residual)
  │
  출력
```

- 사용: **GPT-2, LLaMA, Mistral, 모든 최신 LLM**
- **장점**: 더 안정적인 학습, Warmup 불필요 (일반적으로)
- Residual 경로가 "clean path" 유지 (LayerNorm이 없음)

## RMSNorm (Root Mean Square Layer Normalization)

LLaMA에서 도입된 **LayerNorm의 단순화 버전**입니다.

### 수식 비교

```
LayerNorm: output = γ × (x - μ) / √(σ² + ε) + β
RMSNorm:   output = γ × x / √(mean(x²) + ε)
```

### 차이점

| 항목 | LayerNorm | RMSNorm |
|------|-----------|---------|
| 평균 이동(μ) | 있음 | **없음** |
| 학습 파라미터 | γ, β (2개) | **γ (1개)** |
| 계산량 | 더 많음 | **약 10-15% 적음** |
| 성능 | 기준 | LayerNorm과 유사 |

### RMSNorm 사용 모델

- **LLaMA 1/2/3**
- **Mistral / Mixtral**
- **Gemma**
- **Qwen 2**

## Pre-Normalization with RMSNorm (LLaMA 스타일)

```python
# LLaMA 스타일 Transformer Block
def transformer_block(x):
    # Attention with Pre-RMSNorm
    h = x + attention(rmsnorm(x))
    
    # FFN with Pre-RMSNorm  
    out = h + ffn(rmsnorm(h))
    
    return out
```

이 단순한 구조가 오늘날 거의 모든 LLM의 표준입니다.

## Initialization과의 관계

LayerNorm/Residual과 함께 사용되는 초기화 기법:

| 기법 | 설명 | 사용 |
|------|------|------|
| **Xavier Init** | tanh 계열에 적합 | 초기 Transformer |
| **Kaiming Init** | ReLU 계열에 적합 | 일부 모델 |
| **Small Init** | 출력 레이어를 매우 작게 (σ=0.02) | **GPT-2, LLaMA** |
| **DeepNet Init** | Residual을 √(n_layers)로 스케일링 | 1000층 학습 가능 |

> LLaMA 스타일: 모든 가중치를 N(0, 0.02²)으로 초기화

## 최신 트렌드

1. **Pre-LN + RMSNorm** = 현재 표준 (LLaMA, Mistral, Qwen, Gemma)
2. **Sandwich-Norm**: Attention 전후에 모두 LayerNorm (일부 연구)
3. **QK-Norm**: Attention의 Q와 K에 별도 LayerNorm 적용 (PaLM, GPT-4)
4. **Dynamic Norm**: 학습 가능한 정규화 파라미터 (일부 실험적)

## 참고

- [[transformer-architecture]]: Transformer 전체 구조
- [[attention-mechanism]]: Attention 연산
- [[feed-forward-network]]: FFN 레이어
- [Layer Normalization 논문](https://arxiv.org/abs/1607.06450)
- [RMSNorm 논문](https://arxiv.org/abs/1910.07467)

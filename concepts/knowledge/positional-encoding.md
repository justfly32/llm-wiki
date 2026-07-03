---
title: Positional Encoding (RoPE, ALiBi, Sinusoidal)
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [positional-encoding, rope, alibi, transformer, llm, attention]
links: [[transformer-architecture]], [[attention-mechanism]]
---

# Positional Encoding

> **Positional Encoding**은 Transformer에 **토큰의 위치(순서) 정보**를 주입하는 기법입니다.
> Self-Attention은 순서에 무관하게(permutation-invariant) 동작하므로, 별도의 위치 정보가 필수적입니다.

## 왜 필요한가?

Self-Attention의 한계: **토큰의 순서를 고려하지 않음**

```
"나는 너를 사랑해"  vs  "너는 나를 사랑해"

Self-Attention만으로는:
  "너를"과 "사랑해"의 관계 = 동일
  "나를"과 "사랑해"의 관계 = 동일
  
→ 두 문장을 구분할 수 없음!
```

해결: 입력 임베딩에 **위치 정보를 추가**하여 순서를 인코딩합니다.

## Positional Encoding의 종류

### 1. Sinusoidal Positional Encoding (원본 Transformer)

고정된(학습되지 않는) 삼각함수 기반 위치 인코딩입니다.

$$ PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}}) $$
$$ PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}}) $$

- **pos**: 위치 인덱스 (0, 1, 2, ...)
- **i**: 차원 인덱스 (0, 1, ..., d_model/2)
- **d_model**: 임베딩 차원

#### 특징

| 장점 | 단점 |
|------|------|
| 학습 불필요 (고정 함수) | 유연성 부족 |
| 상대적 위치 정보 인코딩 가능 | 긴 시퀀스 일반화 어려움 |
| 이론적으로 무한 길이 지원 | 실제 성능은 제한적 |
| | Fine-tuning 시 위치 정보 변경 불가 |

> 주파수(frequency)가 차원에 따라 다름 → 낮은 차원은 느린 주파수(장거리), 높은 차원은 빠른 주파수(단거리)

### 2. Learned Positional Embedding (GPT, BERT)

각 위치 인덱스에 **학습 가능한 임베딩 벡터**를 할당합니다.

```python
# BERT: 512개의 학습 가능한 위치 임베딩
self.pos_embeddings = nn.Embedding(512, d_model)

# 각 토큰: token_embedding + position_embedding
x = token_embedding + pos_embedding[pos_id]
```

| 장점 | 단점 |
|------|------|
| 데이터에 맞게 최적화 | **최대 길이 제한** (예: BERT 512) |
| 구현 단순 | 학습된 길이 이상 일반화 불가 |

### 3. Rotary Position Embedding (RoPE) — **현대 표준!**

#### 핵심 아이디어

Q와 K 벡터에 **회전 변환**을 적용하여 위치 정보를 주입합니다.

```
RoPE 이전:
  Q·K^T = 단순 내적 → 위치 정보 없음

RoPE 이후:
  RoPE(Q)·RoPE(K)^T = 위치를 고려한 내적
  → Q_m·K_n = f(m-n)  (상대적 위치 차이에만 의존!)
```

#### 수학적 표현

```python
def apply_rope(x, pos):
    """
    x: (batch, heads, seq_len, d_head)
    pos: 위치 인덱스
    """
    d = x.shape[-1]
    
    # 각 차원 쌍에 대해 회전 행렬 생성
    cos = cos(pos * theta_range)  # (seq_len, d/2)
    sin = sin(pos * theta_range)  # (seq_len, d/2)
    
    # x를 두 반으로 나누어 회전
    x1, x2 = x.chunk(2, dim=-1)
    rotated = torch.cat([x1 * cos - x2 * sin, 
                         x1 * sin + x2 * cos], dim=-1)
    return rotated
```

#### RoPE의 장점

| 장점 | 설명 |
|------|------|
| **상대적 위치 인코딩** | 두 토큰의 **거리 차이**에만 의존 |
| **길이 일반화** | 학습된 길이보다 긴 시퀀스도 처리 가능 (제한적) |
| **감쇠 효과** | 먼 토큰일수록 자연스럽게 낮은 점수 |
| **Zero-overhead** | 추론 시 추가 파라미터 불필요 |
| **호환성** | 기존 Attention 구현에 쉽게 통합 |

#### RoPE 사용 모델

- **LLaMA 1/2/3**
- **Mistral / Mixtral**
- **Gemma**
- **Qwen 1/2**
- **GPT-4 (추정)**
- **내부 회전: 각 헤드마다 다른 θ 값 사용 가능**

### 4. ALiBi (Attention with Linear Biases)

#### 핵심 아이디어

Positional Encoding을 아예 사용하지 않고, **Attention 점수에 직접 편향(bias)을 추가**합니다.

```
ALiBI Attention:
  Attention(Q, K, V) = softmax(Q·K^T/√d + bias_matrix) · V

bias_matrix[i][j] = -m × |i - j|  (선형 패널티)

함수 m = 헤드별 계수:
  m_h = 2^(-8h/n_heads)  (각 헤드가 다른 감쇠율)
```

- **장점**: 
  - Positional Embedding이 필요 없어 메모리 절약
  - **길이 일반화에 매우 강함** (학습 1K → 추론 100K+ 가능)
  - 추론 속도 향상
- **단점**: RoPE보다 표현력이 다소 낮음

#### ALiBi 사용 모델

- **MosaicML MPT**
- **Bloom**

## Positional Encoding 비교

| 기법 | 학습 가능 | 길이 일반화 | 상대 위치 | 계산 오버헤드 | 사용 모델 |
|------|-----------|------------|-----------|--------------|-----------|
| **Sinusoidal** | ❌ | 보통 | 간접적 | 낮음 | 원본 Transformer |
| **Learned** | ✅ | 없음 | ❌ | 낮음 | BERT, GPT-2 |
| **RoPE** | ✅ | **좋음** | **직접적** | 중간 | **LLaMA, Mistral, GPT-4** |
| **ALiBi** | ❌ | **최고** | 직접적 | **매우 낮음** | MPT, Bloom |

> **결론**: 2024-2026년 기준, RoPE가 사실상의 표준입니다.
> 긴 컨텍스트 처리가 중요한 경우 ALiBi가 대안이 될 수 있습니다.

## RoPE와 긴 컨텍스트 확장 (Long Context)

### 문제: RoPE의 길이 일반화 한계

학습 시 본 길이(예: 8K)보다 긴 시퀀스(예: 128K)를 추론하면 RoPE가 잘 작동하지 않습니다.

### 해결 기법

| 기법 | 설명 | 사용 |
|------|------|------|
| **NTK-aware Scaling** | θ 값을 동적으로 조정 (Neural Tangent Kernel 기반) | Llama.cpp 등 |
| **YaRN** | θ 스케일링 + attention temperature 조정 | LLaMA 3 128K |
| **PI (Positional Interpolation)** | 위치 인덱스를 선형으로 압축 | GPT-4 32K→128K |
| **Context Extension** | 짧은 컨텍스트로 학습 후 긴 컨텍스트 Fine-tuning | Claude 100K+ |

### YaRN 수식 (간략)

```python
# YaRN: 길이 일반화를 위한 RoPE 스케일링
scale = max_seq_len / trained_seq_len

# θ 값 조정 (NTK-aware 방식)
new_theta = theta * scale^(-dim / (d_model - 2))

# Attention logits 온도 조절
new_attn = attn * (1 / temperature)
```

## 참고

- [RoPE 논문: Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- [ALiBi 논문: Train Short, Test Long](https://arxiv.org/abs/2108.12409)
- [YaRN: Efficient Context Window Extension](https://arxiv.org/abs/2309.00071)
- [[transformer-architecture]]: Transformer 전체 구조
- [[attention-mechanism]]: Attention 메커니즘

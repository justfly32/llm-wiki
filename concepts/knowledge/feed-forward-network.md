---
title: Feed-Forward Network (FFN / MLP Layer)
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [ffn, mlp, transformer, llm, deep-learning, swiglu, activation-function]
links: [[transformer-architecture]], [[attention-mechanism]], [[layer-normalization]]
---

# Feed-Forward Network (FFN / MLP Layer)

> **FFN (Feed-Forward Network)**은 Transformer 블록에서 Attention 이후에 위치한 **2층 MLP**입니다.
> 각 토큰을 **독립적으로** 고차원 공간으로 변환한 후 다시 원래 차원으로 투영합니다.

## 역할

Attention이 "토큰 간 정보 교환"이라면, FFN은 **"각 토큰의 내부 표현을 정교화"** 합니다.

```
Attention: 토큰 A → [문맥: B, C, D의 정보 수집] → 문맥화된 A'
FFN:      문맥화된 A' → [패턴 매칭, 지식 활성화, 비선형 변환] → 정제된 A''
```

FFN은 LLM의 **지식 저장소** 역할을 합니다. 사실, 관계, 패턴 등 대부분의 학습된 지식이 FFN의 가중치에 저장됩니다.

## 기본 구조

### 표준 FFN (ReLU 버전, GPT-1/2)

```
입력: x (dim = d_model)
  │
  ↓ W₁ (d_model × d_ff)
  │
  ReLU
  │
  ↓ W₂ (d_ff × d_model)
  │
출력: y (dim = d_model)
```

$$ \text{FFN}(x) = W_2 \cdot \text{ReLU}(W_1 \cdot x + b_1) + b_2 $$

### SwiGLU FFN (최신 모델 표준, LLaMA/Palm/GPT-4)

현재几乎所有 최신 LLM이 **SwiGLU** 활성화 함수를 사용합니다.

```
입력: x (dim = d_model)
  │
  ├──→ W_gate (d_model × d_ff) → SiLU ──┐
  │                                       │ 곱 (element-wise)
  └──→ W_up (d_model × d_ff) ────────────┘
                                          │
                                          ↓ W_down (d_ff × d_model)
                                          │
                                       출력: y
```

$$ \text{FFN}(x) = W_{down} \cdot (\text{SiLU}(W_{gate} \cdot x) \odot (W_{up} \cdot x)) $$

## FFN 확장 비율 (Intermediate Size)

표준 Transformer에서 **d_ff = 4 × d_model**입니다.

| 모델 | d_model | d_ff (중간 차원) | 비율 | 활성화 함수 |
|------|---------|------------------|------|------------|
| GPT-2 | 768 | 3072 | 4× | GELU |
| GPT-3 | 12288 | 49152 | 4× | GELU |
| LLaMA 7B | 4096 | 11008 | **2.7×** | SwiGLU |
| LLaMA 70B | 8192 | 28672 | **3.5×** | SwiGLU |
| Mistral 7B | 4096 | 14336 | **3.5×** | SwiGLU |
| GPT-4 (추정) | ~16000 | ~55000 | ~3.4× | SwiGLU |

> SwiGLU는 3개의 가중치 행렬(W_gate, W_up, W_down)을 사용하므로,
> 동일한 파라미터 수를 유지하려면 d_ff를 약 2/3로 줄입니다 (2.7× vs 4×).

## 다양한 활성화 함수

| 함수 | 수식 | 사용 모델 | 특징 |
|------|------|-----------|------|
| **ReLU** | max(0, x) | GPT-1 | 단순하지만 죽는 뉴런 문제 |
| **GELU** | x·Φ(x) | GPT-2/3, BERT | 부드러운 ReLU 변형 |
| **SiLU/Swish** | x·σ(x) | LLaMA, PaLM | 자기 게이팅(self-gating) |
| **SwiGLU** | SiLU(x·W_g) ⊙ (x·W_u) | LLaMA 2/3, Mistral, GPT-4 | **현재 표준** |
| **GeGLU** | GELU(x·W_g) ⊙ (x·W_u) | PaLM, Gemini | SwiGLU와 유사 |

## FFN의 지식 저장 메커니즘

### "Key-Value Memory" 관점

FFN을 **키-값 메모리**로 해석할 수 있습니다:

- **W₁** 각 행 = 저장된 패턴/지식의 **키**
- **W₂** 각 열 = 해당 지식의 **값**
- 특정 입력 패턴이 들어오면, 가장 유사한 키가 활성화되어 해당 값을 출력

```python
# 개념적으로:
# 입력 x가 주어지면:
scores = x @ W₁.T      # 각 키와의 유사도
activations = ReLU(scores)  # 일부 키만 활성화
output = activations @ W₂   # 활성화된 키에 해당하는 값들의 가중합
```

### 실제 발견 (연구 결과)

- **특정 주제 담당 뉴런**: FFN의 특정 뉴런이 특정 지식(예: "프랑스의 수도")을 담당
- **언어 특화 뉴런**: 다국어 모델에서 특정 언어만 담당하는 뉴런 존재
- **출처 추적 가능**: 활성화된 뉴런을 분석하면 모델이 어떤 지식을 사용했는지 추적 가능

## MoE (Mixture of Experts)

**MoE**는 여러 개의 FFN "전문가(Expert)"를 두고, 입력에 따라 **일부만 활성화**합니다.

```
라우터 (Router)
  │
  ├── Top-2 선택 ──→ Expert A (FFN)
  │                  Expert C (FFN)
  │
  결과 = 가중합(Expert_A(x), Expert_C(x))
```

### MoE의 장점

| 장점 | 설명 |
|------|------|
| **파라미터 효율** | 전체 파라미터는 크지만, 추론 시 일부만 사용 (활성 파라미터 ↓) |
| **계산 효율** | 같은 계산 예산으로 더 큰 모델 사용 가능 |
| **전문화** | 각 Expert가 다른 도메인을 담당하게 학습됨 |

### MoE 사용 모델

- **Mixtral 8x7B**: 8개 Expert 중 Top-2 = 47B 파라미터지만 13B만 활성화
- **GPT-4**:传闻 MoE 구조 (1.8T 파라미터 추정)
- **DeepSeek-V2/V3**: MoE + Multi-head Latent Attention
- **Qwen2-MoE**: MoE 구조 채택

## FFN의 미래

1. **MoE 표준화**: 거의 모든 대규모 모델이 MoE 채택
2. **Conditional Computation**: 입력에 따라 다른 계산 경로
3. **Layer Skipping**: FFN을 건너뛰어도 성능 유지 가능 (일부 연구)
4. **FFN Merging**: Fine-tuning된 여러 모델의 FFN 가중치를 병합 (Model Merging)

## 참고

- [[transformer-architecture]]: Transformer 전체 구조
- [[attention-mechanism]]: Attention (FFN 이전 단계)
- [[layer-normalization]]: FFN 전후의 LayerNorm
- [SwiGLU 논문: GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)

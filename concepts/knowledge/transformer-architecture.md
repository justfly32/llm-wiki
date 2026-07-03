---
title: Transformer Architecture
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [transformer, architecture, llm, deep-learning, attention, encoder-decoder]
links: [[attention-mechanism]], [[feed-forward-network]], [[layer-normalization]], [[positional-encoding]]
---

# Transformer Architecture

> **Transformer**는 2017년 Google 연구팀의 "Attention Is All You Need" 논문에서 발표된 딥러닝 아키텍처입니다.
> RNN이나 CNN 없이 **오직 Attention 메커니즘만**으로 시퀀스 데이터를 처리하여, 오늘날 모든 LLM의 기반이 되었습니다.

## 아키텍처 개요

```
출력 (Output)
    ↑
  Linear + Softmax
    ↑
  Add & Norm (Decoder)
    ↑
  Feed Forward (Decoder)
    ↑
  Add & Norm (Decoder)
    ↑
  Cross-Attention (Decoder ← Encoder)
    ↑
  Add & Norm (Decoder)
    ↑
  Masked Self-Attention (Decoder)
    ↑
  Positional Encoding → 입력 임베딩 (Decoder, shift right)
  
                     Encoder 출력 → Cross-Attention
                     
  Positional Encoding → 입력 임베딩 (Encoder)
    ↓
  Add & Norm (Encoder)
    ↓
  Self-Attention (Encoder)
    ↓
  Add & Norm (Encoder)
    ↓
  Feed Forward (Encoder)
    ↓
  입력 (Input)
```

최신 LLM(GPT, LLaMA, Claude)은 **Decoder-only** 구조를 사용합니다.

## 핵심 구성 요소

| 구성 요소 | 역할 | 설명 |
|-----------|------|------|
| **입력 임베딩** | 텍스트 → 벡터 | 각 토큰을 d_model 차원의 벡터로 변환 |
| **Positional Encoding** | 위치 정보 주입 | 토큰의 순서 정보를 임베딩에 더함 |
| **Multi-Head Attention** | 문맥 이해 | 각 토큰이 다른 토큰들과의 관계를 학습 |
| **Feed-Forward Network** | 비선형 변환 | 각 토큰을 독립적으로 고차원 변환 |
| **Add & Norm** | 안정적 학습 | Residual Connection + Layer Normalization |
| **출력 헤드** | 다음 토큰 예측 | Linear + Softmax로 vocabulary 확률 계산 |

## Encoder vs Decoder

### Encoder (BERT 계열)
- **양방향 Attention** (Bidirectional)
- 입력 전체를 한 번에 처리
- 모든 토큰이 서로를 참조 가능
- 주로 **이해(Understanding)** 작업에 사용
  - 문장 분류, 감성 분석, NER, QA

### Decoder (GPT 계열)
- **단방향 Attention** (Causal / Autoregressive)
- 왼쪽 → 오른쪽으로 순차 생성
- 각 토큰은 과거 토큰만 참조 가능 (Masked Attention)
- 주로 **생성(Generation)** 작업에 사용
  - 텍스트 생성, 번역, 요약, 챗봇

### Encoder-Decoder (T5, BART 계열)
- Encoder가 입력을 인코딩 → Decoder가 출력 생성
- Sequence-to-Sequence 작업에 사용
- 번역, 요약 등 입력↔출력 구조가 다른 작업

## 수학적 표현

Transformer의 핵심 연산은 Scaled Dot-Product Attention입니다:

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

여기서:
- **Q** (Query): 현재 토큰이 "찾고자 하는" 정보
- **K** (Key): 각 토큰이 "제공하는" 정보의 레이블
- **V** (Value): 각 토큰의 실제 정보 내용
- **d_k**: Key 벡터의 차원 (스케일링용)

## 최신 트렌드

1. **Decoder-only 독식**: GPT-4, Claude, LLaMA, Mistral 등 모든 최신 LLM이 Decoder-only 채택
2. **MoE (Mixture of Experts)**: FFN을 여러 전문가로 분할 → Mixtral 8x7B, GPT-4
3. **Flash Attention**: GPU 메모리 최적화된 Attention 구현 (IO-aware)
4. **Grouped Query Attention (GQA)**: KV 헤드 수를 줄여 추론 속도 향상
5. **Multi-Query Attention (MQA)**: 모든 Query 헤드가 하나의 KV 헤드 공유

## 참고

- 원본 논문: [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017)
- [[attention-mechanism]]: Attention의 상세 동작 원리
- [[feed-forward-network]]: FFN/MLP 레이어 구조
- [[layer-normalization]]: Layer Norm & Residual Connection
- [[positional-encoding]]: Positional Encoding (RoPE, ALiBi)

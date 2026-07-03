---
title: LLM Training Pipeline
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [training, pre-training, fine-tuning, rlhf, sft, llm, pipeline]
links: [[transformer-architecture]], [[attention-mechanism]], [[tokenization]]
---

# LLM Training Pipeline

> **LLM 학습**은 단순히 "데이터를 많이 넣어서 학습"하는 것이 아니라, 
> 여러 단계를 거쳐 점진적으로 모델의 능력을 향상시키는 정교한 파이프라인입니다.

## 학습의 3단계

오늘날 LLM 학습은 크게 세 단계로 구성됩니다.

```
1. Pre-training (사전 학습)
   └── 기초 언어 능력 학습 (수조 개의 토큰)
   
2. SFT (Supervised Fine-Tuning, 지도 미세 조정)
   └── 지시 따르기 능력 학습 (수십만 개의 대화)
   
3. RLHF (Reinforcement Learning from Human Feedback)
   └── 인간 선호도에 맞게 정렬 (수십만 개의 선호 비교)

선택: DPO (Direct Preference Optimization)
   └── RLHF를 더 간단한 방식으로 대체
```

## 1단계: Pre-training (사전 학습)

### 목표

> **인터넷 규모의 텍스트 데이터로 언어의 기본 패턴, 지식, 문법을 학습**

### 데이터 수집

| 데이터 소스 | 비중 | 설명 |
|------------|------|------|
| 웹 크롤링 (CommonCrawl) | ~60% | 인터넷 전체 페이지 (수십 TB) |
| 책 (Books) | ~15% | Project Gutenberg, 저작권 책 |
| 학술 논문 (ArXiv) | ~5% | 과학/수학/컴퓨터 과학 논문 |
| 코드 (GitHub) | ~10% | 소스 코드, 문서, 이슈 |
| 위키피디아 | ~5% | 백과사전 (고품질) |
| 소셜 미디어 | ~5% | Reddit, 뉴스 등 |

> LLaMA 3는 **15조 토큰**으로 사전 학습되었습니다.

### 데이터 전처리

```python
# 1. 필터링
- 저품질 문서 제거 (짧은 길이, 반복 콘텐츠)
- PII (개인정보) 마스킹
- 중복 제거 (MinHash, SimHash)
- 독성/유해 콘텐츠 필터링

# 2. 토크나이징
- 텍스트 → Token IDs 변환
- 4096-8192 토큰 단위로 청킹

# 3. 혼합 (Mixing)
- 각 데이터 소스의 비율 조정
- 고품질 데이터(PDF, 책) 과소 샘플링 방지를 위한 가중치
```

### 학습 하이퍼파라미터

| 파라미터 | 일반적 범위 | GPT-3 (175B) 예시 |
|----------|-------------|-------------------|
| **학습률** | 1e-4 ~ 3e-4 | 2.5e-4 |
| **배치 크기** | 512 ~ 4096 | 3.2M 토큰 |
| **학습 스텝** | 100K ~ 1M | 500K |
| **Warmup 스텝** | 1K ~ 10K | 3K |
| **Weight Decay** | 0.1 ~ 0.2 | 0.1 |
| **Adam β₁** | 0.9 | 0.9 |
| **Adam β₂** | 0.95 | 0.95 |
| **그라디언트 클리핑** | 1.0 | 1.0 |

### Loss Curve

```
Loss
 │
 │  Pre-training Loss Curve
 │  ┌────
 │  │    ────
 │  │        ────
 │  │            ────
 │  │                ──────
 │  │                       ───────────
 │  └───────────────────────────────────→ Steps
     Phase 1     Phase 2     Phase 3
     (급하강)    (점진 개선)  (수렴)
```

### Loss Spike 대응

학습 중 **Loss Spike** (급격한 손실 증가)가 자주 발생합니다:

```python
# Loss Spike 발생 시 대응 프로토콜
if loss > threshold:
    1. 현재 체크포인트로 롤백
    2. 학습률을 30-50% 감소
    3. 배치에서 유해 데이터 확인
    4. 데이터 혼합 비율 조정
```

## 2단계: SFT (Supervised Fine-Tuning)

### 목표

> **사전 학습된 모델에게 "질문-답변" 형식을 가르치기**

### 데이터 수집 방법

| 방법 | 설명 | 예시 |
|------|------|------|
| **수동 작성** | 인간이 직접 질문-답변 작성 | ShareGPT, OpenAssistant |
| **기존 데이터 변환** | NLP 벤치마크 → 대화 형식 | MMLU, GSM8K |
| **모델 증류** | 강한 모델(GPT-4)의 출력으로 학습 | Alpaca, Vicuna |
| **합성 데이터** | LLM이 생성한 데이터로 학습 | Self-Instruct |

### SFT 데이터 예시

```json
{
  "conversations": [
    {
      "role": "user",
      "content": "대한민국의 수도는 어디인가요?"
    },
    {
      "role": "assistant", 
      "content": "대한민국의 수도는 서울입니다."
    },
    {
      "role": "user",
      "content": "서울의 인구는 약 몇 명인가요?"
    },
    {
      "role": "assistant",
      "content": "서울의 인구는 약 940만 명입니다."
    }
  ]
}
```

### SFT 하이퍼파라미터

| 파라미터 | 일반적 값 | 설명 |
|----------|-----------|------|
| 학습률 | 1e-5 ~ 2e-5 | Pre-training보다 낮게 |
| Epoch | 1~3 | **과적합 방지** 위해 적게 |
| 배치 크기 | 32~128 | 메모리 한계 |
| 학습 데이터 | 수만~수십만 | Pre-training의 0.001% 수준 |

> 💡 **SFT에서 과적합은 매우 흔함**: 3 epoch 이상 학습하면 거의 항상 과적합

## 3단계: RLHF (Reinforcement Learning from Human Feedback)

### 목표

> **모델의 출력을 인간의 선호도(유용성, 무해성, 정직성)에 정렬**

### 전체 프로세스

```
1. PPO (Proximal Policy Optimization)
   
   ┌─────────────────────────────────────────────────────┐
   │ SFT된 모델 (Actor) → 출력 생성                       │
   │     ↓                                                 │
   │ Reward Model (RM) → 점수 계산                         │
   │     ↓                                                 │
   │ PPO 알고리즘 → Actor 가중치 업데이트                   │
   │     ↓                                                 │
   │ 정책(policy) π가 Reward를 최대화하도록 조정            │
   └─────────────────────────────────────────────────────┘

2. KL 발산 제약: π가 π_SFT에서 너무 멀어지지 않도록 제한
   → Reward = RM_score - β × KL(π || π_SFT)
```

### Reward Model (RM) 학습

```python
# RM: 인간의 선호도를 예측하는 모델
# 데이터: 동일한 프롬프트에 대한 두 출력 비교

prompt = "Explain quantum computing"
response_A: "...(설명 A)..."
response_B: "...(설명 B)..."

# 인간 평가: "A가 더 좋음"
# RM 학습: A의 점수가 B보다 높도록

loss = -log(sigmoid(score_A - score_B))
```

### DPO (Direct Preference Optimization)

RLHF의 **단순화된 대안**으로, 별도의 Reward Model이 필요 없습니다.

```python
# DPO Loss
# π: 학습 중인 정책, π_ref: 기준 정책 (SFT 모델)

loss = -log(σ(β * (log(π(y_w|x)/π_ref(y_w|x)) - log(π(y_l|x)/π_ref(y_l|x)))))
# y_w: 선호되는 응답, y_l: 선호되지 않는 응답
# σ: 시그모이드 함수
```

| 항목 | RLHF (PPO) | DPO |
|------|------------|-----|
| **Reward Model** | 필요 | 불필요 |
| **복잡도** | 높음 (4개 모델 동시 학습) | 낮음 (1개 모델) |
| **안정성** | 튜닝이 까다로움 | 비교적 안정적 |
| **성능** | 약간 높음 | 비슷하거나 약간 낮음 |
| **사용 모델** | GPT-4, Claude | LLaMA 3, Mistral |

## 전체 학습 비용

### 대규모 모델 학습 비용 추정

| 모델 | 파라미터 | Pre-training 비용 | 전체 추정 비용 |
|------|----------|-------------------|---------------|
| LLaMA 7B | 7B | ~$0.5M | ~$1M |
| LLaMA 65B | 65B | ~$4M | ~$8M |
| LLaMA 3 70B | 70B | ~$10M | ~$20M |
| GPT-3 | 175B | ~$12M | ~$25M |
| GPT-4 (추정) | 1.8T | ~$100M+ | ~$200M+ |
| Gemini Ultra (추정) | - | ~$200M+ | ~$500M+ |

### 비용 분해

```
┌──────────────────────────────────┐
│ Pre-training: 60% (GPU 시간)      │
├──────────────────────────────────┤
│ 데이터 수집/정제: 15%             │
├──────────────────────────────────┤
│ SFT: 10%                         │
├──────────────────────────────────┤
│ RLHF/DPO: 10%                    │
├──────────────────────────────────┤
│ 평가/테스트: 5%                   │
└──────────────────────────────────┘
```

## 최신 트렌드 (2026년)

1. **데이터 품질 > 데이터 양**: 필터링/중복 제거 기술 발전
2. **합성 데이터 활용 증가**: 약한 모델의 지식을 강한 모델에 증류
3. **계층적 학습**: 1T→7B→70B 점진적 확장
4. **대체 정렬 기법**: KTO, SimPO, ORPO 등 DPO 변형
5. **지속적 학습**: 배포 후에도 사용자 피드백으로 지속 개선
6. **다중 모달 확장**: 텍스트 → 이미지, 비디오, 오디오로 확장

## 참고

- [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)
- [Training Language Models to Follow Instructions (InstructGPT)](https://arxiv.org/abs/2203.02155)
- [DPO 논문: Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [[transformer-architecture]]: 모델 아키텍처
- [[tokenization]]: 데이터 전처리의 시작

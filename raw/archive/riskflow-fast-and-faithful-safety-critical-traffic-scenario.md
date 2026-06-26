---
title: RiskFlow: 빠르고 충실한 안전 중심 교통 시나리오 생성
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [research, alignment, optimization, agent, diffusion]
sources: [raw/papers/riskflow-fast-and-faithful-safety-critical-traffic-scenario-2026-06-08.md]
confidence: medium
---

# RiskFlow: 빠르고 충실한 안전 중심 교통 시나리오 생성

> 📄 원문: [RiskFlow: Fast and Faithful Safety-Critical Traffic Scenario Generation](https://arxiv.org/abs/2606.06423v1)
> ✍️ 저자: Qi Lan, Yining Tang, Yu Shen
> 📅 발행: 2026-06-04
> 🏷️ 카테고리: cs.RO, cs.AI

## 요약

안전이 중요한 교통 시나리오 생성은 드물지만 고위험 상호작용 하에서 자율주행 시스템을 평가하는 데 필수적입니다. 기존 확산(diffusion) 기반 방법들은 폐루프(closed-loop) 생성에서 강력한 제어 가능성을 제공하지만, 반복적인 디노이징(denoising) 과정이 계산적으로 비용이 많이 들며, 긴 롤아웃(rollout) 과정에서 샘플링 및 가이던스(guidance) 오류가 누적되어 떨림(jitter), 비정상 가속, 도로 이탈(off-road) 행동 등 비현실적인 동작 아티팩트를 유발할 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 RiskFlow를 제안합니다. RiskFlow는 폐루프 방식의 안전이 중요한 다중 에이전트(multi-agent) 교통 생성 프레임워크로, 미래 궤적 생성을 행동 공간(action space)에서의 수송(transport) 문제로 정의합니다. RiskFlow는 반복적인 디노이징에 의존하는 대신, 유한 구간에 걸쳐 평균 속도장(velocity field)을 학습하여 가우시안 행동 시퀀스를 단일 순전파(forward pass)로 미래 가속도 및 요(yaw-rate) 명령으로 변환하며, 효율적이고 안정적인 학습을 위해 JVP(Jacobian-Vector Product) 기반 목적 함수를 사용합니다. 테스트 시점에서 RiskFlow는 생성된 행동에 출력 공간(output-space) 가이던스를 적용하여 선택된 주요 에이전트를 위험한 상호작용으로 유도하면서 동시에 도로 이탈 행동을 정규화(regularizing)하고, 차량 동역학(vehicle dynamics)을 통해 물리적으로 실현 가능한 궤적을 재구성합니다. nuScenes 데이터셋을 활용한 tbsim 폐루프 평가 실험 결과, RiskFlow는 다중 에이전트 및 장기 예측(long-horizon) 환경에서 강력한 적대성(adversariality)과 현실성(realism)의 균형을 달성했습니다. 대표적인 기준 방법들과 비교했을 때, RiskFlow는 경쟁력 있는 안전이 중요한 시나리오 생성 성능을 유지하면서도 현실성을 일관되게 향상시켰습니다.

(이하 생략...)

## 원문 영어

<details>
<summary>원문 보기</summary>

Safety-critical traffic scenario generation is essential for evaluating autonomous driving systems under rare but high-risk interactions. Existing diffusion-based methods offer strong controllability in closed-loop generation, but their iterative denoising process is computationally expensive and may accumulate sampling and guidance errors over long rollouts, causing unrealistic motion artifacts such as jitter, abnormal acceleration, and off-road behavior. To address these issues, we propose Ris

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2606.06423v1)

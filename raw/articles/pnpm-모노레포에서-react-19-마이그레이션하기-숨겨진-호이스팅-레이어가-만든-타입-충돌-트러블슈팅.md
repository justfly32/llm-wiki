---
title: "pnpm 모노레포에서 React 19 마이그레이션하기: 숨겨진 호이스팅 레이어가 만든 타입 충돌 트러블슈팅"
source: 우아한형제들 Tech
url: https://techblog.woowahan.com/26128/
date: 2026-03-24
lang: ko
type: reference
tags: [feed, 우아한형제들-tech]
---

# pnpm 모노레포에서 React 19 마이그레이션하기: 숨겨진 호이스팅 레이어가 만든 타입 충돌 트러블슈팅

> Source: [우아한형제들 Tech](https://techblog.woowahan.com/26128/)  
> Date: 2026-03-24

배경: React 19 마이그레이션과 pnpm Catalogs pnpm workspace 기반의 모노레포 환경을 구축하여 프론트엔드 애플리케이션을 운영하고 있습니다. 기존에는 모노레포 내 여러 워크스페이스(앱)의 라이브러리 파편화를 막기 위해, 모든 의존성을 최상단(root)에서 일괄 관리해 왔습니다. 이에 따라 모든 앱이 동일하게 React 18 버전을 사용하고 있었으나, 최근 React 19로의 마이그레이션을 계획하게 되었습니다. 하지만 규모가 큰 모노레포 특성상 모든 앱을 한 [&#8230;]
The post pnpm 모노레포

---
*전문 보기: [pnpm 모노레포에서 React 19 마이그레이션하기: 숨겨진 호이스팅 레이어가 만든 타입 충돌 트러블슈팅](https://techblog.woowahan.com/26128/)*
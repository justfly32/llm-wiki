# Simpli GIF Maker (졸라맨) — 간편 CLI 요약

> 출처: `projects/simpli-gif-maker/README.md` (2026-06-14 동기화)

## 개요
텍스트 설명을 받아 간단한 졸라맨 GIF 애니메이션을 생성하는 단일 Python 스크립트 CLI 도구.

## 사용법
```bash
python3 zolaman.py "졸라맨이 주먹을 휘두른다"
python3 zolaman.py "졸라맨이 춤을 춘다" -o dance.gif
python3 zolaman.py "졸라맨이 달린다" --fps 8
python3 zolaman.py "졸라맨이 점프한다" --size 400
python3 zolaman.py --list  # 사용 가능한 포즈 목록
```

## 지원 동작 (12종)
공격, 발차기, 달리기, 걷기, 점프, 춤, 피하기, 인사, 앉기, 기쁨, 슬픔, 화남

## 기술 스택
- Python 3
- Pillow (이미지 생성)

## 파일 구조
```
zolaman-gif-maker/
├── zolaman.py   # 메인 스크립트
├── README.md
└── *.gif        # 생성된 GIF
```

## 관련
- [[dev-stickman-gif-creator]] — 상세 설계 포함 버전 (스켈레톤 기반)

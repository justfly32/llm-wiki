# Stickman GIF Creator — 상세 설계 요약

> 출처: `projects/stickman-gif-creator/docs/design.md` (2026-06-14 동기화)

## 개요
졸라맨(stickman) 이미지를 기반으로 사용자의 텍스트 설명을 받아 GIF 애니메이션을 자동 생성하는 Python 프로그램.

## 기술 스택
- Python 3.9+
- Pillow (이미지 처리)
- imageio (GIF 생성)
- OpenCV (이미지 분석)

## 아키텍처

### 데이터 흐름
```
이미지 입력(졸라맨) → 전처리(배경 제거) → 스켈레톤 추출(관절점)
텍스트 입력 → 명령어 파싱(동작 분해) → 애니메이션 생성 엔진 → GIF 내보내기
```

### 핵심 모듈
| 모듈 | 파일 | 역할 |
|------|------|------|
| ImageProcessor | `image_processor.py` | 배경 제거, 스켈레톤 추출, 크기 정규화 |
| Skeleton | `skeleton.py` | 관절점 14개(head~foot) + 뼈대 연결 관리 |
| PoseLibrary | `pose_library.py` | 미리 정의된 포즈(stand, walk, jump, wave 등) + 보간 |
| TextParser | `text_parser.py` | 한국어 동작/방향/속도 명령어를 동작 시퀀스로 변환 |
| Animator | `animator.py` | 동작 시퀀스 → 프레임 생성 (기본 12fps) |
| GifExporter | `gif_exporter.py` | 프레임 → GIF (기본 480×480, 무한 루프) |

### 관절점 구조 (14 joints)
```
head → neck → shoulders → elbows → hands
                  ↘ hips → knees → feet
```

### 지원 동작
걸어, 뛰어, 점프, 손 흔들어, 앉아, 인사, 던져 (+ 방향: 왼쪽/오른쪽/위/아래, 속도: 천천히~아주 빨리)

### 복합 명령어 예시
```
"오른쪽으로 걸어가다가 점프해서 손을 흔들어"
→ walk(오른쪽, 2초) → jump(0.5초) → wave(1초)
```

## 구현 단계
1. Phase 1: 스켈레톤 데이터 구조 + 기본 포즈 + 간단 GIF
2. Phase 2: 텍스트 파싱 (명령어 사전, 동작 시퀀스)
3. Phase 3: 이미지 처리 (배경 제거, 골격화, 관절점 감지)
4. Phase 4: 애니메이션 고도화 (Lerp/Slerp 보간, 이징)
5. Phase 5: CLI 인터페이스 + 미리보기

## 확장 가능성
- 음성 입력, 배경 합성, 음향 효과, 캐릭터 커스터마이징, 모션 블러

## 관련 프로젝트
- [[dev-simpli-gif-maker]] — 간편 CLI 버전 졸라맨 GIF 메이커

---
id: "manufacturing-ai-week4/docs/ASSET-MAP.md"
title: "Asset Mapping and Semantic Migration Plan"
repo: "joseki-korea/manufacturing-ai-week4"
device_scope: "all"
doc_type: "architecture"
tags:
  - "architecture"
  - "assets"
  - "semantic-reorg"
status: "DRAFT"
updated: "2026-11-07"
source_of_truth: "docs/ASSET-MAP.md"
---

# Asset Mapping & Semantic Reorganization Plan — manufacturing-ai-week4

본 문서는 `manufacturing-ai-week4` 레포지토리의 소스코드 및 에셋을 기능/모듈별로 시맨틱하게 재구성하기 위한 이동 계획 설계 테이블입니다.
**주의: 본 계획은 설계 단계(DESIGN ONLY)이며, 3자 검토자(Reviewer) PASS 이전까지는 실제 `git mv` 이동 작업을 일절 수행하지 않습니다 (0 moves executed).**

## 1. 시맨틱 이동 계획 테이블 (Semantic Move Plan Table)

| 원본 경로 (Source) | 목표 경로 (Target) | 모듈 성격 및 목적 | 진행 상태 |
|---|---|---|---|
| `lab4_1_regression_activation_and_loss.ipynb` | `src/notebooks/lab4_1_regression_activation_and_loss.ipynb` | 실습 노트북 1 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `lab4_2_classification_activation_and_loss.ipynb` | `src/notebooks/lab4_2_classification_activation_and_loss.ipynb` | 실습 노트북 2 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `lab4_3_challenging_problems.ipynb` | `src/notebooks/lab4_3_challenging_problems.ipynb` | 실습 노트북 3 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `lab4_4_techniques_for_challenging_problems.ipynb` | `src/notebooks/lab4_4_techniques_for_challenging_problems.ipynb` | 실습 노트북 4 | **PLANNED (DESIGN ONLY — 0 executed)** |
| `2026154001_*.ipynb` | `archive/submissions/2026154001_*.ipynb` | 학번 과제 제출 노트북 보존본 | **PLANNED (DESIGN ONLY — 0 executed)** |

## 2. 참조 갱신 계획 (Reference-Update Plan)
- README 내 실습 노트북 상대 경로 동기화

## 3. 빌드 및 테스트 검증 명령어 (Build/Test Verification Commands)
```bash
python3 -c "import json; [json.load(open(f)) for f in ['lab4_1_regression_activation_and_loss.ipynb']]"
```

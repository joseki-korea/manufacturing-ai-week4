---
id: manufacturing-ai-week4/docs/ARCHITECTURE.md
title: Repository Architecture and Directory Layout
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: architecture
tags:
  - architecture
  - directory-layout
status: DRAFT
updated: '2026-11-07'
source_of_truth: docs/ARCHITECTURE.md
---

# Repository Architecture — manufacturing-ai-week4

본 문서는 `joseki-korea/manufacturing-ai-week4` 레포지토리의 파일/디렉토리 구조 및 구성 목적을 설명합니다.

## 1. 프로젝트 개요
- **레포지토리**: `joseki-korea/manufacturing-ai-week4`
- **기본 브랜치**: `main`
- **설명**: 충북대학교 제조 AI 실제 (8884023-01) - 4주차 실습 및 과제 관련 소스코드 및 문서 자산 관리.

## 2. CURRENT 트리 (기본 브랜치 `origin/main`, depth ≤ 3)
기본 브랜치 기준 기존 폴더 구조:
(루트 레벨 디렉토리 없음 - 단일 파일 구성)

## 3. TARGET 트리 (목표 아키텍처 폴더 구조, depth ≤ 3)
Repo Standard 적용 후 목표 폴더 구조:
- `assets/`
- `assets/binaries/`
- `assets/components/`
- `assets/images/`
- `assets/videos/`
- `assets/src/`
- `docs/`
- `handoffs/`

## 4. Current → Target 매핑 테이블
기존 위치에서 목표 위치로의 매핑 및 상태:

| 원본 경로 (Current) | 목표 경로 (Target) | 진행 상태 |
|---|---|---|
| *(이동 없음)* | *(기존 위치 유지)* | **동일 유지** (기존 소스코드 위치 유지) |

> **안내**: 이미 PR에 포함된 파일 이동 내역은 현재 **pending design PASS** 상태로 유지되며, 리뷰어 승인 전까지 추가적인 `git mv`는 전면 중단됩니다.

## 5. 이동 안정성 검증 (Move-Safety Check & Grep Evidence)
코드베이스 내 `import`, `require`, 빌드 설정(빌드 도구/CI)에 대한 영향성 검증 결과입니다:

- **이동 대상 파일 없음**: 본 PR에서는 기존 소스코드 및 리소스의 물리적 위치를 이동하지 않고 표준 문서/구조만 추가하여 100% 안전합니다.


## 6. 마이그레이션 절차 및 롤백 계획 (Migration Steps & Rollback)
### 6.1. 마이그레이션 실행 절차
1. **설계 사전 검토**: 본 `docs/ARCHITECTURE.md`에 명시된 Current→Target 트리 및 매핑 테이블에 대해 리뷰어 승인(PASS)을 획득합니다.
2. **단독 git mv 수행**: 추가 정리가 필요한 파일은 코드 수정 없이 `git mv` 단독 커밋으로 수행합니다.
3. **참조 갱신**: 상대 경로 import 및 README 링크를 동기화합니다.
4. **빌드/테스트 검증**: 단위 테스트 및 빌드 스크립트를 실행하여 경로 무결성을 최종 검증합니다.

### 6.2. 비상 롤백 명령어 (Rollback Plan)
만약 파일 이동으로 인해 런타임 오류가 발생하거나 원상 복구가 필요한 경우, 아래 명령어를 실행하여 즉시 원상 복구할 수 있습니다:

```bash
# 이동된 파일이 없으므로 파일 이동 롤백 불필요.
```

## 7. 설계 승인 원칙 (Design PASS Rule)
CEO 지침에 따라 본 설계 문서가 리뷰어의 최종 PASS 승인을 받기 전까지는 **추가적인 `git mv` 실행이 엄격히 금지**됩니다. 기 수행된 이동은 'pending design PASS' 상태로 동결 유지됩니다.

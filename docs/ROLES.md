---
id: manufacturing-ai-week4/docs/ROLES.md
title: Operational Roles and Multi-Agent Responsibilities
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: roles
tags:
  - roles
  - multi-agent
status: DRAFT
updated: '2026-11-07'
source_of_truth: docs/ROLES.md
---
# Operational Roles — manufacturing-ai-week4

본 문서는 `joseki-korea/manufacturing-ai-week4` 프로젝트를 수행하는 멀티에이전트 협업 체계의 역할을 정의합니다.

## 1. PM 세션 (Planning & Dispatch)
- 기능 요구사항 분석 및 작업 분할.
- 3티어 작업 세션으로의 구체적 태스크 디스패치 및 진행 상황 관리.
- 품질 게이트 검수 및 최종 결과 승인.

## 2. 작업 세션 (Worker Sessions)
- **Antigravity (AGY)**: 풀스택 구현, 아키텍처 설계, 브라우저 자동화 및 통합 검증.
- **Codex Terra**: 백엔드 로직, 데이터베이스 쿼리 및 핵심 알고리즘 구현.
- **Claude Haiku**: 경량 작업, 문서화 검증 및 단위 테스트 보조.
- 3자 상호 교차 검증(Cross-Verification) 90점 이상 달성 시 통과.

## 3. 재니터 세션 (Janitor Session)
- **전담 임무**: 컨텍스트 과적 방지 와치독(Watchdog ONLY).
- 컨텍스트 소비량 30% 도달 시 즉시 `handoffs/`에 인수인계 기록 작성 후 세션 정리.
- 별도의 비즈니스 로직 수정 작업은 일절 수행하지 않음.

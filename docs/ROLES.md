---
id: "manufacturing-ai-week4/docs/ROLES.md"
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

## 1. 컨트롤 및 모니터링 세션 (Control & Monitoring Session — Claude Only)
- **전담 주체**: Claude (Lead Orchestrator).
- **역할 범위**: 총괄 제어 및 모니터링 전담 (Control / Monitoring ONLY).
- 기능 요구사항 분석, 작업 분할, 디스패치 지시 및 최종 품질 게이트 검수.
- 비즈니스 코드 직접 구현 및 수정 작업은 일절 수행하지 않음 (지시 및 검토 전담).

## 2. 작업 세션 (Worker Sessions — Codex Terra & Antigravity Only)
작업 세션은 **Codex Terra** 및 **Antigravity (AGY)** 단독 체제로만 운영되며, Sonnet/Haiku 등 기타 모델은 작업 목록에서 전면 배제됩니다:
- **Codex Terra**: 백엔드 로직, 데이터베이스 쿼리/마이그레이션, API 연동 및 핵심 비즈니스 로직 구현.
- **Antigravity (AGY)**: 풀스택 소스코드 구현, 아키텍처 설계, 브라우저 자동화 및 통합 빌드/테스트 검증.
- 상호 교차 검증(Cross-Verification) 및 테스트 통과(90점 이상) 시에만 브랜치 반영.

## 3. 재니터 세션 (Janitor Session)
- **전담 임무**: 컨텍스트 과적 방지 와치독(Watchdog ONLY).
- 컨텍스트 소비량 30% 도달 시 즉시 `handoffs/`에 인수인계 기록 작성 후 세션 정리.
- 별도의 비즈니스 로직 수정 작업은 일절 수행하지 않음.

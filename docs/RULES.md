---
id: manufacturing-ai-week4/docs/RULES.md
title: Repository Rules
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: rules
tags:
  - rules
  - governance
status: DRAFT
updated: '2026-11-07'
source_of_truth: docs/RULES.md
---
# Repository Rules — manufacturing-ai-week4

본 문서는 `joseki-korea/manufacturing-ai-week4` 레포지토리의 작업 수칙 및 AI 에이전트 협업 규칙을 정의합니다.

## 1. 상위 거버넌스 준수 (Canonical Rules)
- 정본: `solucionemos-vault/rules/`
- Rule 00: 단말 간 동기화 및 충돌 방지 원칙 준수.
- Rule 01: 보고 및 세션 커뮤니케이션 규칙 준수.
- Rule 02: 보안 키, 토큰, 비밀번호 신규 파일 복사 금지.
- Rule 04: 작업 전후 Git 커밋 해시 또는 증빙 로그 필수 제시.

## 2. 레포지토리 운영 수칙 (Branch & PR Policy)
- 기본 브랜치(`main`) 직접 푸시 절대 금지.
- 모든 변경 사항은 작업 브랜치 생성 후 Draft PR을 통해 병합 검토.
- 강제 푸시(`git push --force`) 금지.

## 3. 보안 및 기밀 보호
- `.env`, 개인 API 키, 비밀 토큰 커밋 금지.
- 의심되는 자격 증명 발견 시 즉시 작업을 중단하고 관리자에게 보고.

## 4. 컨텍스트 과적 방지 (Context Management)
- 단일 세션에서 과도한 컨텍스트 누적 방지.
- 컨텍스트 사용량 30% 초과 시 재니터 세션에 의한 인수인계(Handoff) 및 세션 분할 필수.

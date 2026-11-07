---
id: manufacturing-ai-week4/assets/binaries/README.md
title: "Binaries Asset Index and Google Drive Integration"
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: asset-index
tags:
  - assets
  - binaries
  - google-drive
status: DRAFT
updated: '2026-11-07'
source_of_truth: assets/binaries/README.md
---
# Binaries Asset Index — manufacturing-ai-week4

본 디렉토리는 `joseki-korea/manufacturing-ai-week4` 프로젝트의 바이너리 자산(모델 가중치, 아카이브, 컴파일 산출물 등)을 관리하며, Google Drive와 연동됩니다.

## 1. 목적 및 연동 원칙
- **소스코드-깃허브 / 바이너리-구글드라이브 연동**: 대용량 바이너리는 Git 저장소에 직접 커밋하지 않고 Google Drive에 분리 보관합니다.
- **Drive 경로**: `Orca 자산/manufacturing-ai-week4/binaries`
- **동기화 주체**: 로그인 컨텍스트 카드 기준 Google Drive 활성 로그인 단말 (`GQFK` JM_Global / `Google Drive 연동 계정` 등 활성 계정 단말).
- **동기화 대상**: 신규 추가 파일 전용 (New files only).

## 2. 매니페스트 관리
- 로컬 바이너리 메타데이터 및 동기화 상태는 `drive-manifest.json`에 기록됩니다.
- 바이너리 파일 본체는 `.gitignore`에 의해 커밋에서 제외되며, `README.md`와 `drive-manifest.json`만 Git으로 추적됩니다.

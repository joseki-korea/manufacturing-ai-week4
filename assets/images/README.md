---
id: manufacturing-ai-week4/assets/images/README.md
title: Images Asset Index and Google Drive Integration
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: asset-index
tags:
  - assets
  - images
  - google-drive
status: DRAFT
updated: '2026-11-07'
source_of_truth: assets/images/README.md
---
# Images Asset Index — manufacturing-ai-week4

본 디렉토리는 `joseki-korea/manufacturing-ai-week4` 프로젝트에서 사용되는 이미지 자산(스크린샷, 다이어그램, UI 에셋 등)을 관리하며, Google Drive와 연동됩니다.

## 1. 목적 및 연동 원칙
- **소스코드-깃허브 / 이미지-구글드라이브 연동**: 신규 이미지는 Git 저장소 용량 과적 방지를 위해 Google Drive 동기화 폴더로 연동 관리합니다.
- **Drive 경로**: `Orca 자산/manufacturing-ai-week4/images`
- **동기화 주체**: 로그인 컨텍스트 카드 기준 Google Drive 활성 로그인 단말 (`GQFK` JM_Global / `indiasolucionemos@gmail.com` 등 활성 계정 단말).
- **동기화 대상**: 신규 추가 파일 전용 (New files only).

## 2. 매니페스트 관리
- 로컬 이미지 파일 목록 및 동기화 상태는 `drive-manifest.json`에 기록됩니다.
- Git 트래킹 제외 규칙은 `.gitignore`에 정의되어 있으며, `README.md` 및 `drive-manifest.json`만 Git에 커밋됩니다.

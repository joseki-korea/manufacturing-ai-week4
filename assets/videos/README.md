---
id: "manufacturing-ai-week4/assets/videos/README.md"
title: "Videos Asset Index and Google Drive Integration"
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: asset-index
tags:
  - assets
  - videos
  - google-drive
status: DRAFT
updated: '2026-11-07'
source_of_truth: "assets/videos/README.md"
---

# Videos Asset Index — manufacturing-ai-week4

본 디렉토리는 `joseki-korea/manufacturing-ai-week4` 프로젝트에서 사용되는 동영상 및 영상 미디어 자산(시연 영상, 교육 비디오, 화면 녹화본 등)을 관리하며, Google Drive와 연동됩니다.

## 1. 목적 및 연동 원칙
- **소스코드-깃허브 / 비디오-구글드라이브 연동**: 대용량 비디오 자산은 Git 저장소 용량 과적을 방지하고 최적의 대역폭 관리를 위해 Google Drive 동기화 폴더로 분리 연동 관리합니다.
- **Drive 경로**: `Orca 자산/manufacturing-ai-week4/videos`
- **동기화 주체**: 로그인 컨텍스트 카드 기준 Google Drive 활성 로그인 단말 (`GQFK` JM_Global / `Google Drive 연동 계정` 등 활성 계정 단말).
- **동기화 원칙 (Zero-Loss Safe Sync)**:
  - **신규 파일 전용 동기화 (New-file-only sync)**: 신규 생성된 영상 파일만 선택적으로 동기화합니다.
  - **무결성 검증 (Verify Size + SHA-256)**: 업로드 전/후 파일 크기 및 체크섬을 전수 교차 검증합니다.
  - **덮어쓰기·삭제·공유권한 변경 금지**: 기존 원본 영상의 덮어쓰기(Overwrite), 삭제(Delete), 또는 공유 권한 변경을 엄격히 금지합니다.

## 2. 매니페스트 관리
- 로컬 비디오 파일 메타데이터 및 동기화 상태는 `drive-manifest.json`에 기록됩니다.
- Git 트래킹 제외 규칙은 `.gitignore`에 정의되어 있으며, `README.md` 및 `drive-manifest.json`만 Git에 커밋됩니다.

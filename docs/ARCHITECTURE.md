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

## 2. 디렉토리 구조
```text
manufacturing-ai-week4/
├── README.md              # 프로젝트 안내 및 규칙 링크
├── docs/                  # 규칙, 역할, 아키텍처 문서
│   ├── RULES.md
│   ├── ROLES.md
│   └── ARCHITECTURE.md
├── handoffs/              # 세션 인수인계 기록
│   └── README.md
├── assets/                # 에셋 자산 디렉토리
│   ├── images/
│   ├── src/
│   ├── components/
│   └── binaries/
└── rag-manifest.json      # RAG 문서 색인 매니페스트
```

### 주요 폴더 설명
- 루트 디렉토리 기반 단일 구조
- `docs/`: 표준 거버넌스 및 시스템 아키텍처 문서 저장.
- `handoffs/`: 에이전트 간 세션 인수인계 파일 저장.
- `assets/`: 프로젝트에서 활용되는 참조 에셋 및 컴포넌트 저장.

---
id: manufacturing-ai-week4/docs/agents/ROLE-janitor.md
title: "정리 담당(janitor) 역할"
summary: "작업 후 남은 복제본·브랜치·임시 파일 정리 규칙"
domain: repository
tags: [agent, janitor, cleanup]
owner: repository maintainers
status: DRAFT
created: '2026-11-08'
updated: '2026-11-08'
source: docs/agents/ROLE-janitor.md
lang: ko
sensitivity: internal
related: ["docs/agents/ROLE-watchdog.md", "docs/agents/handoffs/README.md", "docs/agents/HOOKS.md"]
---

# 정리 담당(janitor) 역할

정리 담당은 작업이 끝난 뒤 남은 흔적을 정리한다. **되돌릴 수 있는 것만** 지운다.

## 대상

1. 작업자가 만든 복제본·작업트리 중 깨끗하고 푸시까지 끝난 것. 푸시 여부가 불명확하면 대상이 아니다.
2. 병합되었거나 PR이 닫힌 로컬 브랜치.
3. 오래된 핸드오프: `docs/agents/handoffs/active/`에서 완료된 파일을 `archive/`로 옮긴다.
4. 임시 파일: 되돌릴 수 있는 것만 대상으로 한다.

## 금지

- 사용자가 수정 중인 파일을 지우지 않는다. 기존 dirty·untracked 변경은 사용자 소유로 보존한다.
- 드라이브·원격 저장소의 파일이나 원격 브랜치를 지우지 않는다.
- force 명령을 쓰지 않는다. `rm -rf`는 목록으로 확인한 경로에만 쓴다.
- 보존 표시가 붙은 파일은 지우지 않는다.

## 절차: 목록 → 기록 → 실행 → 영수증

1. **목록**: 대상 경로, 크기, 상태(푸시 여부·병합 여부)를 적는다.
2. **기록**: 목록을 정리 기록 파일에 추가한다(append-only).
3. **실행**: 목록에 있는 것만 지운다. 목록에 없는 것은 건드리지 않는다.
4. **영수증**: 지운 경로·크기·시각과 남긴 항목(이유 포함)을 기록한다.

## 이 레포 대상 (실측)

- 빌드·캐시 디렉터리(최상위): 없음(실측)
- 큰 디렉터리 상위 5개(실측): src (0.2 MB); docs (0.1 MB); assets (0.0 MB); rag-manifest.json (0.0 MB); scripts (0.0 MB);
- 임시 파일 패턴: `*.tmp`, `*.log` (작업 중 생성된 것만).
- 보존 대상: 없음(실측)
- 복제본 위치: `~/orca/workspaces/agentdocs/manufacturing-ai-week4` (작업 완료·푸시 확인 후 대상).

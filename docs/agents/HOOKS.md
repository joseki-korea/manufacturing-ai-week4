---
id: manufacturing-ai-week4/docs/agents/HOOKS.md
title: "훅 목록(실측)"
summary: "이 레포에 실제로 있는 훅 목록과 추가·안전 규칙"
domain: repository
tags: [agent, hooks]
owner: repository maintainers
status: DRAFT
created: '2026-11-08'
updated: '2026-11-08'
source: docs/agents/HOOKS.md
lang: ko
sensitivity: internal
related: ["docs/agents/ROLE-watchdog.md", "docs/agents/ROLE-janitor.md", "docs/agents/handoffs/README.md"]
---

# 훅 목록 (실측)

기준: 브랜치 `repo-standard-20261107` @4d6bc146, PR #1. 아래 목록은 이 레포 파일을 직접 확인한 결과다.

## 요약

| 종류 | 확인 위치 | 발견 수 |
|---|---|---|
| Claude Code | `.claude/settings*.json` (hooks) | 없음(실측) |
| Codex | `.codex/` | 없음(실측) |
| git | `.githooks/`, `.husky/`, `.pre-commit-config.yaml` | 0개 |
| CI | `.github/workflows/` | 없음(실측) |
| package.json | prepare·precommit 등 훅성 스크립트 | 없음(실측) |

## 항목 상세

### Claude Code (.claude/settings*.json)

없음(실측). 이 레포에는 `.claude/` 폴더가 없다.

### Codex (.codex/)

없음(실측). 이 레포에는 `.codex/` 폴더가 없다.

### git

없음(실측)

### CI (.github/workflows/)

없음(실측). 이 레포에는 워크플로 파일이 없다.

### package.json 스크립트

없음(실측). prepare·precommit 등 훅성 스크립트가 없다. (lint·test·build 같은 일반 스크립트는 훅이 아니다.)

## 추가 방법 (안전하게)

- **Claude Code**: `.claude/settings.json`의 `hooks`에 항목을 추가한다. 명령은 로컬 스크립트 1개로 제한한다.
- **git**: `.githooks/`에 스크립트를 추가하고 각자 `git config core.hooksPath .githooks`를 설정한다. 커밋을 막는 훅이면 실패 시 동작을 이 문서에 적는다.
- **CI**: `.github/workflows/`에 추가하고 권한은 `contents: read`처럼 최소로 둔다.

## 안전 규칙

1. **비밀 금지**: 훅 파일에 토큰·키·계정 정보를 쓰지 않는다.
2. **네트워크 최소**: 훅은 로컬 검사만 한다. 외부 전송이 필요하면 별도 승인을 받는다.
3. **되돌리기**: 훅 제거는 파일 삭제와 `core.hooksPath` 해제로 바로 되돌릴 수 있어야 한다.
4. **기록**: 훅을 추가·변경하면 이 문서를 같은 커밋에서 갱신한다.

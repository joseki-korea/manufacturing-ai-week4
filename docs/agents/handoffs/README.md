---
id: manufacturing-ai-week4/docs/agents/handoffs/README.md
title: "멀티에이전트 핸드오프 규칙"
summary: "세션 사이에 작업을 넘길 때 남기는 기록 규칙"
domain: repository
tags: [agent, handoff]
owner: repository maintainers
status: DRAFT
created: '2026-11-08'
updated: '2026-11-08'
source: docs/agents/handoffs/README.md
lang: ko
sensitivity: internal
related: ["docs/agents/handoffs/TEMPLATE.md", "docs/agents/ROLE-janitor.md", "docs/agents/ROLE-watchdog.md", "RULES.md"]
---

# 멀티에이전트 핸드오프 규칙

이 폴더는 세션(Claude·Codex·Antigravity 등)과 담당 역할(janitor·watchdog) 사이에서 작업을 넘길 때 남기는 기록 공간이다.

## 폴더

- `active/`: 진행 중이거나 받은 쪽이 아직 끝내지 않은 핸드오프.
- `archive/`: 끝난 핸드오프. 옮길 때는 `git mv`를 쓴다.
- `TEMPLATE.md`: 새 핸드오프의 기본 양식.

루트의 `handoffs/` 폴더는 이전 기록이라 이 규칙의 대상이 아니다. 새 핸드오프는 이 폴더에만 쓴다.

## 파일 이름

`YYYYMMDD-HHMM-<from>-to-<to>-<topic>.md`

- 예: `20261108-1430-claude-to-codex-login-fix.md`
- `<from>`, `<to>`: 역할 이름(claude, codex, antigravity, janitor, watchdog, hub).
- `<topic>`: 영문 소문자와 하이픈.
- 시각은 작성 시점의 로컬 시간.

## 규칙

1. **append-only**: 작성 후 기존 줄을 고치거나 지우지 않는다. 정정은 파일 끝에 `정정 (시각): ...`으로 추가한다.
2. **ACK**: 받은 쪽은 파일 끝에 `ACK: <역할> <YYYY-MM-DD HH:MM>` 한 줄만 추가한다.
3. **종료**: 목표가 끝나면 `archive/`로 옮긴다. 보낸 쪽 또는 janitor가 옮긴다.
4. **근거**: `경로#줄 @sha8` 형식으로 쓴다. 예: `docs/agents/HOOKS.md#L12 @4d6bc146`.
5. **금지**: 비밀번호·토큰·키·계정 ID·개인정보를 쓰지 않는다. 필요하면 위치만 적는다(예: "환경변수 이름 X").
6. **범위**: 핸드오프는 작업을 넘기는 기록일 뿐이다. 받은 쪽이 다른 역할의 권한을 대신 행사하지 않는다.

## 절차

1. 보내는 쪽: `TEMPLATE.md`를 복사해 `active/`에 새 파일을 만들고 목표·완료·남은 일·다음 담당을 채운다.
2. 커밋: 작업 브랜치에 커밋한다. 원격에는 기존 PR 브랜치로만 푸시한다.
3. 받는 쪽: 파일을 읽고 `ACK` 줄을 추가한다.
4. 완료: 마지막 항목을 기록하고 `archive/`로 옮긴다.

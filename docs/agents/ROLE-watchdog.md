---
id: manufacturing-ai-week4/docs/agents/ROLE-watchdog.md
title: "감시 담당(watchdog) 역할"
summary: "세션 정체·디스크·맥락·규칙 위반·실패 테스트 감시 규칙"
domain: repository
tags: [agent, watchdog, monitor]
owner: repository maintainers
status: DRAFT
created: '2026-11-08'
updated: '2026-11-08'
source: docs/agents/ROLE-watchdog.md
lang: ko
sensitivity: internal
related: ["docs/agents/ROLE-janitor.md", "docs/agents/handoffs/README.md", "docs/agents/HOOKS.md"]
---

# 감시 담당(watchdog) 역할

감시 담당은 세션 상태를 살피고 문제가 있으면 알린다. 직접 작업하지 않는다.

## 감시 항목과 기준

| 항목 | 기준 | 조치 |
|---|---|---|
| 좌석 정체 | 20분 동안 출력 없음 | 경고 후 재촉 |
| 디스크 | 여유 공간 1.5GB 미만 | 경고 후 janitor에 정리 요청 |
| 맥락 | 사용률 40% 이상 | 핸드오프 준비 요청 |
| 규칙 위반 | 세션 이름 형식 위반, 우회, 허용되지 않은 모델 사용 | 경고 후 재배차 요청 |
| 실패 테스트 | 테스트 명령 실패 | 경고 후 재배차 요청 |

## 주기와 보고

- 점검 주기: 5분.
- 보고: 1줄. 형식은 `YYYY-MM-DD HH:MM | <레포> | <항목> | <값> | <조치 요청>`.
- 문제가 없으면 보고를 생략하거나 `OK`로 줄인다.

## 금지

- 직접 작업, 코드·문서 수정, 파일 삭제를 하지 않는다.
- 조치는 경고·재촉·재배차 요청으로만 한다.
- 비밀 값이나 세션 식별자 전문을 보고에 적지 않는다.

## 이 레포 감시 대상 (실측)

- 실패 테스트 명령: 없음(실측: 테스트 스크립트 없음)
- 디스크 점검 경로: 작업 복제본 위치(`~/orca/workspaces/agentdocs/manufacturing-ai-week4`)와 홈 볼륨.
- 큰 디렉터리 상위 5개(실측, 맥락 점검 참고용): src (0.2 MB); docs (0.1 MB); assets (0.0 MB); rag-manifest.json (0.0 MB); scripts (0.0 MB);

---
id: manufacturing-ai-week4/handoffs/README.md
title: Agent Session Handoff Notes Index
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: handoff
tags:
  - handoff
  - session-notes
status: DRAFT
updated: '2026-11-07'
source_of_truth: handoffs/README.md
---
# Agent Session Handoff Notes — manufacturing-ai-week4

본 디렉토리는 AI 에이전트 세션 간의 인수인계 기록을 보관합니다.

## 1. 운영 원칙
- **추가 전용(Append-only)**: 기존 기록은 수정하거나 삭제하지 않음.
- **기밀 엄금**: API 키, 토큰, 비밀번호, 개인정보 기록 절대 금지.
- **파일 명명 규칙**: `YYYY-MM-DD-<session-id>.md`

## 2. 인수인계 템플릿 Frontmatter
```yaml
---
id: "manufacturing-ai-week4/handoffs/YYYY-MM-DD-session-id.md"
title: Session Handoff YYYY-MM-DD
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: handoff
tags:
  - handoff
status: DRAFT
updated: 'YYYY-MM-DD'
source_of_truth: handoffs/YYYY-MM-DD-<session-id>.md
---
```

---
name: ghcp-meeting-minutes-skill
description: Generate concise, actionable meeting minutes for internal meetings. Includes
  metadata, attendees, agenda, decisions, action items (owner + due date), and follow-up
  steps.
license: MIT
tags:
- general
---

## Verification & Acceptance Criteria for Generated Minutes

A generated minutes document is acceptable if:

- It contains Metadata, Attendance, Decisions, and Action Items sections.
- Every action item has an assigned owner and a due date or a clear timeframe.
- All significant decisions are captured with at least 1-line rationale.
- Attachments or references are listed or explicitly marked `None`.
- The document is factual; uncertain items are labeled `TBD`.

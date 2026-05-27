---
name: ghcp-references-scoring-rubric
description: 'Skill: ghcp-references-scoring-rubric'
license: MIT
tags:
- general
---

## Calibration Tips

- **Cross-check**: If ROI is 10 but Cost is also 10, the Priority formula still rewards it when Ease is high and Risk is low. That's intentional — high-leverage, high-investment work remains visible.
- **Don't anchor Cost on license price alone.** Human-capital time (security triage, onboarding, change management, review burden) dominates most rollouts.
- **Risk ≠ Cost.** A cheap change (toggle enforcement) can carry very high Risk if staged poorly.
- **Ease ≠ ROI.** A one-click change with low ROI still ranks modestly; the formula only pushes it up if Risk is also very low.
- **Estimate explicitly.** When you don't have data or user-confirmed context, score against the anchor and mark the rationale `(estimated)`.
- **Domain mapping.** If your item doesn't match any column, pick the closest analog (scale of blast radius, reversibility, and human-hours is what matters — not the technology).

---
name: rb-ai-rule-set-benchmark-analysis
description: 'Skill: rb-ai-rule-set-benchmark-analysis'
license: MIT
tags:
- general
---

## Key Takeaways from Benchmark (Reflecting Corrections)

*   **Invest in Capable Models:** Still the most critical factor.
*   **Provide Context:** Still crucial. Attaching at least the relevant general rules, and likely having access to memory, is needed.
*   **Minimal Rules Insufficient Alone:** Still holds true.
*   **Rule Spec Choice & Attachment:**
    *   For `gemini-1.5-pro`, using `medium` or `heavy` principles combined with attaching *only* the `general rule file` proved effective and reasonably efficient for performing file update actions.
    *   Using `light` principles required attaching `all files` for a successful answer, but this configuration proved expensive overall, especially for action proposal/execution.
    *   The strategy of "light principles + full context access" is **not** the most token-efficient based on the corrected data; it was expensive for the action proposal step.
    *   `medium-spec` (with general file attached) remains a strong contender for balancing guidance and efficiency for capable models.
*   **Further Investigation Needed:** (Mostly Unchanged)
    *   Verify target file update consistency (`active_context` vs. `task_plan`).
    *   Assess the qualitative correctness of conclusions and file updates.
    *   Confirm the exact files attached in the `heavy-spec` run that cost 33k+150k (was it just general or all?).

---

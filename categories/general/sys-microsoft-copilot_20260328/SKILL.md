---
name: sys-microsoft-copilot_20260328
description: 'Skill: sys-microsoft-copilot_20260328'
license: MIT
tags:
- general
---

### `search_template_images`
Searches for images across multiple queries to fill GenUI template image fields. Returns image RefIds for each query.
- `queries`: Array of search queries, one per item that needs an image (max 8 queries in the array). Each query should be specific enough to find a relevant image (e.g., 'Lagaan movie poster', 'RRR movie poster').
- `disable_card_ux`: Boolean, controls whether to disable card UX.

---

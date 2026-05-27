---
name: ghcp-references-data-classification
description: 'Skill: ghcp-references-data-classification'
license: MIT
tags:
- general
---

## Aggregation Risk Assessment

Combination attacks — data that becomes more sensitive when combined:

| Alone | Combined With | Combined Tier | Risk |
|-------|--------------|---------------|------|
| Email (T3) | Password hash (T1) | T1 | Account takeover |
| Name (T4) | DOB (T2) + Address (T2) | T2 | Full identity reconstruction |
| IP address (T3) | Timestamps + User ID | T2 | Behavioral profiling |
| City (T4) | Purchase history (T4) | T3 | De-anonymization risk |
| Health category (T4) | Name + Email | T1 | HIPAA triggering |

**Rule:** Always assess fields in combination, not just in isolation.

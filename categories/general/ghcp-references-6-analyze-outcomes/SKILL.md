---
name: ghcp-references-6-analyze-outcomes
description: 'Skill: ghcp-references-6-analyze-outcomes'
license: MIT
tags:
- general
---

## Final verification

Before you end your turn, run the Step 6 verifier script that ships beside `setup.sh` in this skill's `resources/` directory against the exact test run directory you analyzed.

Example shape:

```bash
python /path/to/eval-driven-dev/resources/verify_step6_completion.py pixie_qa/results/<test_id>
```

If the verifier reports any error, keep working. Step 6 is not complete until the verifier passes.

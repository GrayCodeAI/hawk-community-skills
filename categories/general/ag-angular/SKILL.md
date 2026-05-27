---
name: ag-angular
description: Modern Angular (v20+) expert with deep knowledge of Signals, Standalone
  Components, Zoneless applications, SSR/Hydration, and reactive patterns.
license: MIT
tags:
- general
risk: safe
source: self
date_added: 2026-02-27
---

## Common Troubleshooting

| Issue                          | Solution                                            |
| ------------------------------ | --------------------------------------------------- |
| Signal not updating UI         | Ensure `OnPush` + call signal as function `count()` |
| Hydration mismatch             | Check server/client content consistency             |
| Circular dependency            | Use `inject()` with `forwardRef`                    |
| Zoneless not detecting changes | Trigger via signal updates, not mutations           |
| SSR fetch fails                | Use `TransferState` or `withFetch()`                |

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

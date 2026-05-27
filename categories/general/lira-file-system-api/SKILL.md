---
name: lira-file-system-api
description: 'Skill: lira-file-system-api'
license: MIT
tags:
- general
---

## Security & Safety

* Never trust file paths from user input; normalize/validate. (Path traversal)
* Do not log sensitive file contents; scrub secrets.
* Avoid `eval` on file contents; parse safely (e.g., `JSON.parse` with try/catch).

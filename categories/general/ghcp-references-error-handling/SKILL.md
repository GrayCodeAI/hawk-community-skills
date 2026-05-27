---
name: ghcp-references-error-handling
description: 'Skill: ghcp-references-error-handling'
license: MIT
tags:
- general
---

## Exit Code Reference

| Tool | Exit Code | Meaning |
|------|-----------|---------|
| az | 0 | Success |
| az | 1 | General error |
| az | 2 | Command not found |
| az | 3 | Required argument missing |
| azd | 0 | Success |
| azd | 1 | Error |
| bicep | 0 | Build succeeded |
| bicep | 1 | Build failed (errors) |
| bicep | 2 | Build succeeded with warnings |

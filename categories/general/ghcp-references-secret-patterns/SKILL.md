---
name: ghcp-references-secret-patterns
description: 'Skill: ghcp-references-secret-patterns'
license: MIT
tags:
- general
---

## Safe Patterns (Do NOT flag)

These are intentional placeholders — recognize and skip:
```
"your-api-key-here"
"<YOUR_API_KEY>"
"${API_KEY}"
"${process.env.API_KEY}"
"os.environ.get('API_KEY')"
"REPLACE_WITH_YOUR_KEY"
"xxx...xxx"
"sk-..." (in documentation/comments)
```

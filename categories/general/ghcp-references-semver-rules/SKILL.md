---
name: ghcp-references-semver-rules
description: 'Skill: ghcp-references-semver-rules'
license: MIT
tags:
- general
---

## Edge cases

| Situation | Recommendation |
|---|---|
| Only internal/private symbols changed | PATCH |
| Type annotation added to previously untyped function | PATCH (non-breaking) |
| Changing default value of optional parameter | Treat as MAJOR if callers might rely on old default |
| Adding a new required config option to an optional block | MINOR if the block itself is optional, otherwise MAJOR |
| Reverting a previous commit entirely | Follow what the net diff shows, not the revert message |

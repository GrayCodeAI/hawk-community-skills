---
name: ghcp-references-connection-references
description: 'Skill: ghcp-references-connection-references'
license: MIT
tags:
- general
---

## Teams Adaptive Card Dual-Connection Requirement

Flows that send adaptive cards **and** post follow-up messages require two
separate Teams connections:

```json
"connectionReferences": {
  "shared_teams": {
    "connectionName": "shared-teams-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "id": "/providers/Microsoft.PowerApps/apis/shared_teams"
  },
  "shared_teams_1": {
    "connectionName": "shared-teams-yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
    "id": "/providers/Microsoft.PowerApps/apis/shared_teams"
  }
}
```

Both can point to the **same underlying Teams account** but must be registered
as two distinct connection references. The webhook (`OpenApiConnectionWebhook`)
uses `shared_teams` and subsequent message actions use `shared_teams_1`.

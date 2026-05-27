---
name: ghcp-references-debug-workflow
description: 'Skill: ghcp-references-debug-workflow'
license: MIT
tags:
- general
---

## Post-Fix Verification Checklist

1. `update_live_flow` returns `error: null` — definition accepted  
2. `resubmit_live_flow_run` confirms new run started  
3. Wait for run completion (poll `get_live_flow_runs` every 15 s)  
4. Confirm new run `status = "Succeeded"`  
5. If flow has downstream consumers (child flows, emails, SharePoint writes),
   spot-check those too

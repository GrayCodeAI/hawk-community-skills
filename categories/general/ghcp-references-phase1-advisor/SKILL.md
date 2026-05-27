---
name: ghcp-references-phase1-advisor
description: 'Skill: ghcp-references-phase1-advisor'
license: MIT
tags:
- general
---

**Next Step: Phase 4 (Azure Deployment)**

The review is complete. The following steps will proceed:
1. **What-if Validation** — Preview planned resources without making actual changes
2. **Preview Diagram** — Architecture visualization based on What-if results (02_arch_diagram_preview.html)
3. **Actual Deployment** — Create resources in Azure after user confirmation

Shall we proceed with deployment? (If you'd like just the code without deployment, let me know)
```

**NEVER do this:**
- Completing Phase 3 and just providing the `az deployment group create` command without further guidance
- Deploying directly without What-if validation, or telling the user to run commands themselves
- Skipping the Phase 4 steps (What-if → Preview Diagram → Deployment)

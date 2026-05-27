---
name: ghcp-references-phase4-deployer
description: 'Skill: ghcp-references-phase4-deployer'
license: MIT
tags:
- general
---

### Handling Architecture Change Requests After Deployment

**When the user requests resource additions/changes/deletions after deployment is complete, do NOT go directly to Bicep/deployment.**
Always return to Phase 1 and update the architecture first.

**Process:**

1. **Confirm user intent** — Ask first whether they want to add to the existing deployed architecture:
   ```
   Would you like to add a VM to the currently deployed architecture?
   Current configuration: [Deployed services summary]
   ```

2. **Return to Phase 1 — Apply Delta Confirmation Rule**
   - Use the existing deployment result (`03_arch_diagram_result.html`) as the current state baseline
   - Verify required fields for new services (SKU, networking, region availability, etc.)
   - Confirm undecided items via ask_user
   - Fact-check (MS Docs fetch + cross-validation)

3. **Generate Updated Architecture Diagram**
   - Combine existing deployed resources + new resources into `04_arch_diagram_update_draft.html`
   - Show to the user and get confirmation:
   ```
   ## Updated Architecture

   [Interactive diagram — 04_arch_diagram_update_draft.html]
   (Previous deployment result: 03_arch_diagram_result.html)

   **Changes:**
   - Added: [New services list]
   - Removed: [Removed services list] (if any)

   Proceed with this configuration?
   ```

4. **After confirmation, proceed through Phase 2 → 3 → 4 in order**
   - Incrementally add new resource modules to existing Bicep
   - Review → What-if → Deploy (incremental deployment)

**Never do the following:**
- Jump directly to Bicep generation without updating the architecture diagram when a change is requested after deployment
- Ignore the existing deployment state and create new resources in isolation
- Proceed without confirming with the user whether to add to the existing architecture

---
name: ghcp-references-production-typescript
description: 'Skill: ghcp-references-production-typescript'
license: MIT
tags:
- general
---

## Production Checklist

- [ ] Batch processing enabled
- [ ] **Shutdown handling:** Call `provider.shutdown()` before exit to flush queued spans
- [ ] **Graceful termination:** Flush spans on SIGTERM/SIGINT signals
- [ ] Data masking configured (`HIDE_INPUTS`/`HIDE_OUTPUTS` if PII)
- [ ] Span filtering for health checks/noisy paths
- [ ] Error handling implemented
- [ ] Graceful degradation if Phoenix unavailable
- [ ] Performance tested
- [ ] Monitoring configured (Phoenix UI checked)

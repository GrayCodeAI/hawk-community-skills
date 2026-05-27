---
name: ghcp-references-azure-dynamic-sources
description: 'Skill: ghcp-references-azure-dynamic-sources'
license: MIT
tags:
- general
---

## Decision Rule: When to Fetch?

| Information Type | Must Fetch? | Rationale |
|-----------------|-------------|-----------|
| API version | **Always fetch** | Changes frequently; incorrect values cause deployment failure |
| Model availability (name, region) | **Always fetch** | Varies by region and changes frequently |
| SKU list | **Always fetch** | Can change per service |
| Region availability | **Always fetch** | Per-service region support changes frequently. Always verify that the user-specified region is available for the service |
| PE groupId & DNS Zone | Can reference `service-gotchas.md` for v1 key services; **must fetch for new services or complex configurations (Monitor, etc.)** | Key service mappings are stable, but new/complex services are risky |
| Required property patterns | Reference files first | Near-immutable (isHnsEnabled, etc.) |

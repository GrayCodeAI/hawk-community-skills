---
name: ghcp-references-security
description: 'Skill: ghcp-references-security'
license: MIT
tags:
- general
---

## Architecture Patterns

### Data Store Separation
Separate operational data (transactional DB) from analytical data (data warehouse).
Apply different retention periods and access controls to each.
The analytics store MUST NOT read directly from production operational tables.

### Dedicated Consent Store
Track consent as an immutable event log in a separate store, not a boolean column on the user table.
This enables: auditable consent history, version tracking, easy withdrawal without data loss.

### Audit Log Segregation
Store audit logs in a separate, append-only store.
The application service account MUST NOT be able to delete audit log entries.
Use a separate DB user with INSERT-only rights on the audit table.

### DSR Queue Pattern
Implement Data Subject Requests as an asynchronous workflow:
`POST /api/v1/me/erasure-request` → enqueue a job → worker scrubs all stores → notify user on completion.
This handles the complexity of multi-store scrubbing reliably and provides a retry mechanism.

### Pseudonymization Gateway
For analytics pipelines, implement a pseudonymization service at the boundary between
operational and analytical systems.
The mapping key (HMAC secret or tokenization vault) never leaves the operational zone.
The analytics zone receives only pseudonymized identifiers.

### Crypto-Shredding (Event Sourcing)
Encrypt personal data in events with a per-user DEK stored in the KMS.
On user erasure: delete the DEK → all historical events for that user are effectively anonymized
without modifying the event log.

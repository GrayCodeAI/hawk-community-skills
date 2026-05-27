---
name: ag-api-fuzzing-bug-bounty
description: Provide comprehensive techniques for testing REST, SOAP, and GraphQL
  APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability
  discovery, authentication bypass, IDOR ...
license: MIT
tags:
- general
risk: offensive
source: community
author: zebbern
date_added: 2026-02-27
---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API returns nothing | Add `X-Requested-With: XMLHttpRequest` header |
| 401 on all endpoints | Try adding `?user_id=1` parameter |
| GraphQL introspection disabled | Use clairvoyance for schema reconstruction |
| Rate limited | Use IP rotation or batch requests |
| Can't find endpoints | Check Swagger, archive.org, JS files |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

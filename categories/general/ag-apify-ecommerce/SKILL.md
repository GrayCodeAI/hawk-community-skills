---
name: ag-apify-ecommerce
description: Extract product data, prices, reviews, and seller information from any
  e-commerce platform using Apify's E-commerce Scraping Tool.
license: MIT
tags:
- general
risk: unknown
source: community
---

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Ensure `~/.claude/.env` contains `APIFY_TOKEN=your_token` |
| `Actor not found` | Verify Actor ID: `apify/e-commerce-scraping-tool` |
| `Run FAILED` | Check Apify console link in error output |
| `Timeout` | Reduce `maxProductResults` or increase `--timeout` |
| `No results` | Verify URLs are valid and accessible |
| `Invalid marketplace` | Check marketplace value matches supported list exactly |

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

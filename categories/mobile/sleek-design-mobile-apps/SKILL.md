---
name: sleek-design-mobile-apps
description: Use when the user wants to design a mobile app, create screens, build
  UI, or interact with their Sleek projects. Covers high-level requests ("design an
  app that does X") and specific ones ("list my...
license: MIT
tags:
- mobile
compatibility: Requires SLEEK_API_KEY environment variable. Network access limited
  to https://sleek.design only.
metadata: None
requires-env: SLEEK_API_KEY
allowed-hosts: https://sleek.design
---

## Common Mistakes

| Mistake                                             | Fix                                                                             |
| --------------------------------------------------- | ------------------------------------------------------------------------------- |
| Sending to `/api/v1` without `Authorization` header | Add `Authorization: Bearer $SLEEK_API_KEY` to every request                              |
| Using wrong scope                                   | Check key's scopes match the endpoint (e.g. `chats:write` for sending messages) |
| Sending next message before run completes           | Poll until `completed`/`failed` before next send                                |
| Using `wait=true` on long generations               | It blocks 300s max; have a fallback to polling for `202` response               |
| HTTP URLs in `imageUrls`                            | Only HTTPS URLs are accepted                                                    |
| Assuming `result` is present on `202`               | `result` is absent until status is `completed`                                  |

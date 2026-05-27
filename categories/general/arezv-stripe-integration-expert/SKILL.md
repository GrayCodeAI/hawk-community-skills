---
name: arezv-stripe-integration-expert
description: Stripe Integration Expert
license: MIT
tags:
- general
---

## Common Pitfalls

- **Webhook delivery order not guaranteed** — always re-fetch from Stripe API, never trust event data alone for DB updates
- **Double-processing webhooks** — Stripe retries on 500; always use idempotency table
- **Trial conversion tracking** — store `hasHadTrial: true` in DB to prevent trial abuse
- **Proration surprises** — always preview proration before upgrade; show user the amount before confirming
- **Customer portal not configured** — must enable features in Stripe dashboard under Billing → Customer portal settings
- **Missing metadata on checkout** — always pass `userId` in metadata; can't link subscription to user without it

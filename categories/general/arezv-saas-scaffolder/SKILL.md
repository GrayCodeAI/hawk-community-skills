---
name: arezv-saas-scaffolder
description: Generates complete, production-ready SaaS project boilerplate including
  authentication, database schemas, billing integration, API routes, and a working
  dashboard using Next.js 14+ App Router, Type...
license: MIT
tags:
- general
---

## Reference Files

For additional guidance, generate the following companion reference files alongside the scaffold:

- **`CUSTOMIZATION.md`** — Auth providers, database options, ORM alternatives, payment providers, UI themes, and billing models (per-seat, flat-rate, usage-based).
- **`PITFALLS.md`** — Common failure modes: missing `NEXTAUTH_SECRET`, webhook secret mismatches, Edge runtime conflicts with Drizzle, unextended session types, and migration strategy differences between dev and prod.
- **`BEST_PRACTICES.md`** — Stripe singleton pattern, server actions for form mutations, idempotent webhook handlers, `Suspense` boundaries for async dashboard data, server-side feature gating via `stripeCurrentPeriodEnd`, and rate limiting on auth routes with Upstash Redis + `@upstash/ratelimit`.

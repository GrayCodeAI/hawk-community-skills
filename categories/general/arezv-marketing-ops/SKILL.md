---
name: arezv-marketing-ops
description: Central router for the marketing skill ecosystem. Use when unsure which
  marketing skill to use, when orchestrating a multi-skill campaign, or when coordinating
  across content, SEO, CRO, channels, a...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: marketing
updated: 2026-03-06
---

## Proactive Triggers

- **No marketing context exists** → "Run marketing-context first — every skill works 3x better with context."
- **Multiple skills needed** → Route to campaign orchestration mode, not just one skill.
- **Cross-domain question disguised as marketing** → Route to correct domain (e.g., "help with pricing" → pricing-strategy, not CRO).
- **Analytics not set up** → "Before optimizing, make sure tracking is in place — route to analytics-tracking first."
- **Content without SEO** → "This content should be SEO-optimized. Run seo-audit or content-production, not just copywriting."

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "What marketing skill should I use?" | Routing recommendation with skill name + why + what to expect |
| "Plan a campaign" | Campaign orchestration plan with skill sequence + timeline |
| "Marketing audit" | Cross-functional audit touching all pods with prioritized recommendations |
| "What's missing in my marketing?" | Gap analysis against full skill ecosystem |

## Communication

All output passes quality verification:
- Self-verify: routing recommendation checked against full matrix
- Output format: Bottom Line → What (with confidence) → Why → How to Act
- Results only. Every finding tagged: 🟢 verified, 🟡 medium, 🔴 assumed.

## Related Skills

- **chief-of-staff** (C-Suite): The C-level router. Marketing-ops is the domain-specific equivalent.
- **marketing-context**: Foundation — run this first if it doesn't exist.
- **cmo-advisor** (C-Suite): Strategic marketing decisions. Marketing-ops handles execution routing.
- **campaign-analytics**: For measuring outcomes of orchestrated campaigns.

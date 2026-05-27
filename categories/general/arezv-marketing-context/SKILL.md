---
name: arezv-marketing-context
description: Create and maintain the marketing context document that all marketing
  skills read before starting. Use when the user mentions 'marketing context,' 'brand
  voice,' 'set up context,' 'target audience,...
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

Surface these without being asked:

- **Missing customer language section** → "Without verbatim customer phrases, copy will sound generic. Can you share 3-5 quotes from customers describing their problem?"
- **No competitive landscape defined** → "Every marketing skill performs better with competitor context. Who are the top 3 alternatives your customers consider?"
- **Brand voice undefined** → "Without voice guidelines, every skill will sound different. Let's define 3-5 adjectives that capture your brand."
- **Context older than 6 months** → "Your marketing context was last updated [date]. Positioning may have shifted — review recommended."
- **No proof points** → "Marketing without proof points is opinion. What metrics, logos, or testimonials can we reference?"

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "Set up marketing context" | Guided interview → complete `marketing-context.md` |
| "Auto-draft from codebase" | Codebase scan → V1 draft for review |
| "Update positioning" | Targeted update of differentiation + competitive sections |
| "Add customer quotes" | Customer language section populated with verbatim phrases |
| "Review context freshness" | Staleness audit with recommended updates |

## Communication

All output passes quality verification:
- Self-verify: source attribution, assumption audit, confidence scoring
- Output format: Bottom Line → What (with confidence) → Why → How to Act
- Results only. Every finding tagged: 🟢 verified, 🟡 medium, 🔴 assumed.

## Related Skills

- **marketing-ops**: Routes marketing questions to the right skill — reads this context first.
- **copywriting**: For landing page and web copy. Reads brand voice + customer language from this context.
- **content-strategy**: For planning what content to create. Reads target keywords + personas from this context.
- **marketing-strategy-pmm**: For positioning and GTM strategy. Reads competitive landscape from this context.
- **cs-onboard** (C-Suite): For company-level context. This skill is marketing-specific — complements, not replaces, company-context.md.

---
name: arezv-campaign-analytics
description: Analyzes campaign performance with multi-touch attribution, funnel conversion
  analysis, and ROI calculation for marketing optimization. Use when analyzing marketing
  campaigns, ad performance, attri...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: marketing
domain: campaign-analytics
updated: 2026-02-06
python-tools: attribution_analyzer.py, funnel_analyzer.py, campaign_roi_calculator.py
tech-stack: marketing-analytics, attribution-modeling
---

## Limitations

- **No statistical significance testing** -- Scripts provide descriptive metrics only; p-value calculations require external tools.
- **Standard library only** -- No advanced statistical libraries. Suitable for most campaign sizes but not optimized for datasets exceeding 100K journeys.
- **Offline analysis** -- Scripts analyze static JSON snapshots; no real-time data connections or API integrations.
- **Single-currency** -- All monetary values assumed to be in the same currency; no currency conversion support.
- **Simplified time-decay** -- Exponential decay based on configurable half-life; does not account for weekday/weekend or seasonal patterns.
- **No cross-device tracking** -- Attribution operates on provided journey data as-is; cross-device identity resolution must be handled upstream.

## Related Skills

- **analytics-tracking**: For setting up tracking. NOT for analyzing data (that's this skill).
- **ab-test-setup**: For designing experiments to test what analytics reveals.
- **marketing-ops**: For routing insights to the right execution skill.
- **paid-ads**: For optimizing ad spend based on analytics findings.

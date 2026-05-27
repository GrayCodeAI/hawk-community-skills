---
name: copilot-doublecheck
description: Three-layer verification pipeline for AI output. Extracts verifiable
  claims, finds supporting or contradicting sources via web search, runs adversarial
  review for hallucination patterns, and produc...
license: MIT
tags:
- general
---

## Domain-Specific Guidance

### Legal Content

Legal content carries elevated hallucination risk because:
- Case names, citations, and holdings are frequently fabricated by models
- Jurisdictional nuances are often flattened or omitted
- Statutory language may be paraphrased in ways that change the legal meaning
- "Majority rule" and "minority rule" distinctions are often lost

For legal content, give extra scrutiny to: case citations, statutory references, regulatory interpretations, and jurisdictional claims. Search legal databases when possible.

### Medical and Scientific Content

- Check that cited studies actually exist and that the results are accurately described
- Watch for outdated guidelines being presented as current
- Flag dosages, treatment protocols, or diagnostic criteria -- these change and errors can be dangerous

### Financial and Regulatory Content

- Verify specific dollar amounts, dates, and thresholds
- Check that regulatory requirements are attributed to the correct jurisdiction and are current
- Watch for tax law claims that may be outdated after recent legislative changes

### Technical and Security Content

- Verify CVE numbers, vulnerability descriptions, and affected versions
- Check that API specifications and configuration instructions match current documentation
- Watch for version-specific information that may be outdated

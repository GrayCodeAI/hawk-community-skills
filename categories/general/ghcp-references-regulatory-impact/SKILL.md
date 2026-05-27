---
name: ghcp-references-regulatory-impact
description: 'Skill: ghcp-references-regulatory-impact'
license: MIT
tags:
- general
---

## Total Breach Cost Estimation Model

**Benchmark source:** IBM Security + Ponemon Institute — "Cost of a Data Breach Report" (annually updated)  
**URL:** https://www.ibm.com/reports/data-breach  
Figures below are from the **2024 edition** (last verified). IBM 2025 shows a 9% decrease — download the current PDF for updated values. **[IBM 2024, p.14]** page references refer to the 2024 edition.

Use this model when generating the Financial Impact Estimate section:

### Direct Costs
```
1. Detection & containment: $1.1M average      [IBM 2024, p.14]
2. Post-breach response:     $1.2M average      [IBM 2024, p.14]
3. Lost business:            $1.5M average      [IBM 2024, p.14]
4. Notification costs:       records × $2–$8 per individual  [industry estimate]
5. Credit monitoring:        records × $5–$20/year if PII    [industry estimate]
6. Legal costs:              $200K–$3M depending on complexity [industry estimate]
7. Forensic investigation:   $50K–$500K                      [industry estimate]
8. PR/crisis communications: $100K–$500K                     [industry estimate]
```

### Regulatory Costs
```
9. Regulatory fines:         [see per-regulation formulas above — all sourced from law text]
10. Settlement costs:        $1M–$100M+ for class actions    [historic case data]
```

### Reputational Multiplier
Apply based on public visibility of the organization:
```
B2C consumer app, consumer brand:     ×1.5 (high reputational damage)
B2B enterprise, low public profile:  ×1.1 (moderate reputational damage)
Healthcare or financial institution:  ×2.0 (trust erosion is severe)
Government or public sector:         ×1.8 (public accountability)
```

### Final Estimate Format
```
Minimum likely cost:   [conservative scenario, good response, small record count]
Probable cost:         [most likely scenario, average response]
Maximum exposure:      [worst case: maximum fines + class action + reputational]
```

---
name: arezv-business-investment-advisor
description: Business investment analysis and capital allocation advisor. Use when
  evaluating whether to invest in equipment, real estate, a new business, hiring,
  technology, or any capital expenditure. Also us...
license: MIT
tags:
- general
---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Using ROI alone without time value of money | ROI ignores when cash flows occur — a 50% ROI over 10 years is worse than 30% over 2 years | Always calculate NPV and IRR alongside ROI for investments over $25K or 12 months |
| Relying on optimistic revenue projections | Founders and sales teams systematically overestimate revenue from new investments | Run the downside case at 50% of projected revenue as the primary decision input |
| Ignoring opportunity cost | Approving an investment in isolation misses what else that capital could do | Always compare the proposed IRR against the best alternative use of the same capital |
| Sunk cost reasoning in go/no-go decisions | Past spend is irrelevant to whether continuing will generate positive returns | Evaluate only the incremental investment required vs. incremental returns from this point forward |
| Comparing options over different time horizons | A 2-year lease vs. a 7-year purchase cannot be compared without normalization | Normalize all options to the same analysis period using annualized metrics |
| Skipping sensitivity analysis | A single-point estimate hides how fragile the investment case is | Run at least three scenarios (base, upside +20%, downside -40%) and identify the break-even assumption |
| Funding negative NPV projects without naming the strategic reason | Destroys value without accountability for the non-financial rationale | If strategic value justifies negative NPV, name the specific strategic reason and set a review date |

## Related Skills

- **cfo-advisor**: Use for startup-specific financial strategy, burn rate, runway, fundraising. NOT for individual investment ROI analysis.
- **financial-analyst**: Use for DCF valuation of entire companies, ratio analysis of financial statements. NOT for single capital expenditure decisions.
- **saas-metrics-coach**: Use for SaaS-specific unit economics (CAC, LTV, churn). NOT for equipment or real estate investments.
- **ceo-advisor**: Use for strategic direction and capital allocation across the entire business. NOT for individual investment math.

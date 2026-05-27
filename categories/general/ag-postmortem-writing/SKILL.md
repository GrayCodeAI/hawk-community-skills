---
name: ag-postmortem-writing
description: Comprehensive guide to writing effective, blameless postmortems that
  drive organizational learning and prevent incident recurrence.
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

### Why #5: Why isn't there a safety net for this type of change?
**Answer**: We lack automated tests that verify connection pool behavior and lack documentation about our connection patterns.

**Evidence**: Test suite has no tests for connection handling; wiki has no article on database connections.

## Root Causes Identified

1. **Primary**: Missing automated tests for infrastructure behavior
2. **Secondary**: Insufficient documentation of architectural patterns
3. **Tertiary**: Code review checklist doesn't include infrastructure considerations

## Systemic Improvements

| Root Cause | Improvement | Type |
|------------|-------------|------|
| Missing tests | Add infrastructure behavior tests | Prevention |
| Missing docs | Document connection patterns | Prevention |
| Review gaps | Update review checklist | Detection |
| No canary | Implement canary deployments | Mitigation |
```

### Template 3: Quick Postmortem (Minor Incidents)

```markdown
# Quick Postmortem: [Brief Title]

**Date**: 2024-01-15 | **Duration**: 12 min | **Severity**: SEV3

## What Happened
API latency spiked to 5s due to cache miss storm after cache flush.

## Timeline
- 10:00 - Cache flush initiated for config update
- 10:02 - Latency alerts fire
- 10:05 - Identified as cache miss storm
- 10:08 - Enabled cache warming
- 10:12 - Latency normalized

## Root Cause
Full cache flush for minor config update caused thundering herd.

## Fix
- Immediate: Enabled cache warming
- Long-term: Implement partial cache invalidation (ENG-999)

## Lessons
Don't full-flush cache in production; use targeted invalidation.
```

## Facilitation Guide

### Running a Postmortem Meeting

```markdown
## Meeting Structure (60 minutes)

### 1. Opening (5 min)
- Remind everyone of blameless culture
- "We're here to learn, not to blame"
- Review meeting norms

### 2. Timeline Review (15 min)
- Walk through events chronologically
- Ask clarifying questions
- Identify gaps in timeline

### 3. Analysis Discussion (20 min)
- What failed?
- Why did it fail?
- What conditions allowed this?
- What would have prevented it?

### 4. Action Items (15 min)
- Brainstorm improvements
- Prioritize by impact and effort
- Assign owners and due dates

### 5. Closing (5 min)
- Summarize key learnings
- Confirm action item owners
- Schedule follow-up if needed

## Facilitation Tips
- Keep discussion on track
- Redirect blame to systems
- Encourage quiet participants
- Document dissenting views
- Time-box tangents
```

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| **Blame game** | Shuts down learning | Focus on systems |
| **Shallow analysis** | Doesn't prevent recurrence | Ask "why" 5 times |
| **No action items** | Waste of time | Always have concrete next steps |
| **Unrealistic actions** | Never completed | Scope to achievable tasks |
| **No follow-up** | Actions forgotten | Track in ticketing system |

## Best Practices

### Do's
- **Start immediately** - Memory fades fast
- **Be specific** - Exact times, exact errors
- **Include graphs** - Visual evidence
- **Assign owners** - No orphan action items
- **Share widely** - Organizational learning

### Don'ts
- **Don't name and shame** - Ever
- **Don't skip small incidents** - They reveal patterns
- **Don't make it a blame doc** - That kills learning
- **Don't create busywork** - Actions should be meaningful
- **Don't skip follow-up** - Verify actions completed

## Resources

- [Google SRE - Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- [Etsy's Blameless Postmortems](https://codeascraft.com/2012/05/22/blameless-postmortems/)
- [PagerDuty Postmortem Guide](https://postmortems.pagerduty.com/)

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

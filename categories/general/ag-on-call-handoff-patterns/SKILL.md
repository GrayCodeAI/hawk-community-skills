---
name: ag-on-call-handoff-patterns
description: Effective patterns for on-call shift transitions, ensuring continuity,
  context transfer, and reliable incident response across shifts.
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

**Incoming on-call (@bob) - Please confirm you have:**
- [ ] Joined #inc-20240122-payment
- [ ] Access to dashboards
- [ ] Understand current state
- [ ] Know escalation path
```

## Handoff Sync Meeting

### Agenda (15 minutes)

```markdown
## Handoff Sync: @alice → @bob

1. **Active Issues** (5 min)
   - Walk through any ongoing incidents
   - Discuss investigation status
   - Transfer context and theories

2. **Recent Changes** (3 min)
   - Deployments to watch
   - Config changes
   - Known regressions

3. **Upcoming Events** (3 min)
   - Maintenance windows
   - Expected traffic changes
   - Releases planned

4. **Questions** (4 min)
   - Clarify anything unclear
   - Confirm access and alerting
   - Exchange contact info
```

## On-Call Best Practices

### Before Your Shift

```markdown
## Pre-Shift Checklist

### Access Verification
- [ ] VPN working
- [ ] kubectl access to all clusters
- [ ] Database read access
- [ ] Log aggregator access (Splunk/Datadog)
- [ ] PagerDuty app installed and logged in

### Alerting Setup
- [ ] PagerDuty schedule shows you as primary
- [ ] Phone notifications enabled
- [ ] Slack notifications for incident channels
- [ ] Test alert received and acknowledged

### Knowledge Refresh
- [ ] Review recent incidents (past 2 weeks)
- [ ] Check service changelog
- [ ] Skim critical runbooks
- [ ] Know escalation contacts

### Environment Ready
- [ ] Laptop charged and accessible
- [ ] Phone charged
- [ ] Quiet space available for calls
- [ ] Secondary contact identified (if traveling)
```

### During Your Shift

```markdown
## Daily On-Call Routine

### Morning (start of day)
- [ ] Check overnight alerts
- [ ] Review dashboards for anomalies
- [ ] Check for any P0/P1 tickets created
- [ ] Skim incident channels for context

### Throughout Day
- [ ] Respond to alerts within SLA
- [ ] Document investigation progress
- [ ] Update team on significant issues
- [ ] Triage incoming pages

### End of Day
- [ ] Hand off any active issues
- [ ] Update investigation docs
- [ ] Note anything for next shift
```

### After Your Shift

```markdown
## Post-Shift Checklist

- [ ] Complete handoff document
- [ ] Sync with incoming on-call
- [ ] Verify PagerDuty routing changed
- [ ] Close/update investigation tickets
- [ ] File postmortems for any incidents
- [ ] Take time off if shift was stressful
```

## Escalation Guidelines

### When to Escalate

```markdown
## Escalation Triggers

### Immediate Escalation
- SEV1 incident declared
- Data breach suspected
- Unable to diagnose within 30 min
- Customer or legal escalation received

### Consider Escalation
- Issue spans multiple teams
- Requires expertise you don't have
- Business impact exceeds threshold
- You're uncertain about next steps

### How to Escalate
1. Page the appropriate escalation path
2. Provide brief context in Slack
3. Stay engaged until escalation acknowledges
4. Hand off cleanly, don't just disappear
```

## Best Practices

### Do's
- **Document everything** - Future you will thank you
- **Escalate early** - Better safe than sorry
- **Take breaks** - Alert fatigue is real
- **Keep handoffs synchronous** - Async loses context
- **Test your setup** - Before incidents, not during

### Don'ts
- **Don't skip handoffs** - Context loss causes incidents
- **Don't hero** - Escalate when needed
- **Don't ignore alerts** - Even if they seem minor
- **Don't work sick** - Swap shifts instead
- **Don't disappear** - Stay reachable during shift

## Resources

- [Google SRE - Being On-Call](https://sre.google/sre-book/being-on-call/)
- [PagerDuty On-Call Guide](https://www.pagerduty.com/resources/learn/on-call-management/)
- [Increment On-Call Issue](https://increment.com/on-call/)

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

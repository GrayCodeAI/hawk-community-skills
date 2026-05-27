---
name: agc-observability
description: 'Skill: agc-observability'
license: MIT
tags:
- general
---

## Production Checklist

### AgentCore Platform
- [ ] Transaction Search enabled
- [ ] ADOT installed (`aws-opentelemetry-distro`)
- [ ] Session tracking enabled
- [ ] Sampling configured (1-10%)

### Essential
- [ ] OpenTelemetry tracing enabled
- [ ] Cost tracking implemented
- [ ] CloudWatch dashboards created
- [ ] Error alerting configured

### Metrics
- [ ] Latency tracked (p50, p90, p99)
- [ ] Token usage monitored
- [ ] Tool success rate tracked
- [ ] Error rate alerts (> 2%)

### Security
- [ ] Sensitive data redacted from traces
- [ ] Access logs enabled
- [ ] Retention policies configured

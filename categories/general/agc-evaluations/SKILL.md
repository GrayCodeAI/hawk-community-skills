---
name: agc-evaluations
description: 'Skill: agc-evaluations'
license: MIT
tags:
- general
---

## Results

**CloudWatch GenAI Dashboard**: CloudWatch → GenAI Observability → Evaluations tab

**CloudWatch Metrics**: `AWS/BedrockAgentCore/Evaluations`

**Alerts**:
```python
import boto3
cw = boto3.client('cloudwatch')

cw.put_metric_alarm(
    AlarmName='AgentQualityDegradation',
    MetricName='Helpfulness',
    Namespace='AWS/BedrockAgentCore/Evaluations',
    Statistic='Average',
    Period=3600,
    EvaluationPeriods=2,
    Threshold=7.0,
    ComparisonOperator='LessThanThreshold'
)
```

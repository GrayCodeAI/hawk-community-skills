---
name: agc-architecture
description: 'Skill: agc-architecture'
license: MIT
tags:
- general
---

## Regional Considerations

**Data Residency**: Bedrock processes data in-region (Australian data sovereignty, etc.)

**Best Practice**:
```python
model = BedrockModel(
    model_id="anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="eu-west-1"  # GDPR-compliant
)
```

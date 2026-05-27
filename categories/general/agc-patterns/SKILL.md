---
name: agc-patterns
description: 'Skill: agc-patterns'
license: MIT
tags:
- general
---

### Integration Testing Agents

```python
from foundation.agent_factory import BaseAgentFactory
from unittest.mock import Mock

def test_agent_with_mocked_tools():
    mock_tool = Mock(return_value={
        "status": "success",
        "content": [{"text": "mocked result"}]
    })

    agent = BaseAgentFactory.create_agent(
        agent_id="test-agent",
        system_prompt="You are a test agent.",
        tools=[mock_tool]
    )

    result = agent("Test query")
    assert mock_tool.called
    assert "mocked result" in str(result.message)
```

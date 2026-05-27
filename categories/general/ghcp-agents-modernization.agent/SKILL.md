---
name: ghcp-agents-modernization.agent
description: Human-in-the-loop modernization assistant for analyzing, documenting,
  and planning complete project modernization with architectural recommendations.
license: MIT
tags:
- general
model: GPT-5
tools: None
---

## Notes for Developers

- This agent creates a paper trail of decisions and analysis
- All documentation is version-controlled in `/docs/`
- Implementation plan can be fed directly to Copilot Coding Agent
- Suitable for regulated industries requiring audit trails
- Works best with repositories containing 1000+ files or complex business logic

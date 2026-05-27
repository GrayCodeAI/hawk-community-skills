---
name: mdc-pydantic-model-rules
description: "Specific rules for creating Pydantic models, focusing on versioning and usage within the project."
license: MIT
tags: [python]
---

- Use type hints for all function signatures. Prefer Pydantic models over raw dictionaries for input validation.
- Use Pydantic v2.
- Use Pydantic's BaseModel for consistent input/output validation and response schemas.
---
name: lt-openapi-spec-generator
description: 'Skill: lt-openapi-spec-generator'
license: MIT
tags:
- testing
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the OpenAPI/Swagger Specification design

Once the OpenAPI/Swagger Specification output is delivered, ask the user:

"Would you like me to generate API test cases for this design? (yes/no)"

If the user says **yes**:
- Check if the API Test Case Generator skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the API Test Case Generator skill
  - Use the specification output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the API Documentation skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

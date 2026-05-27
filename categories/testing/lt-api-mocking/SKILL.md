---
name: lt-api-mocking
description: 'Skill: lt-api-mocking'
license: MIT
tags:
- testing
Triggers on: mock server", "API sandbox", "stub responses", "fixture data", "test
  doubles",
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the API Mocks and Stubs (as requested)

Once the API mocks output is delivered, ask the user:

"Would you like me to help in devising rate limiting strategies for these APIs? (yes/no)"

If the user says **yes**:
- Check if the api-ratelimiting-helper skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the api-ratelimiting-helper skill
  - Use the API information output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the api-ratelimiting-helper skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

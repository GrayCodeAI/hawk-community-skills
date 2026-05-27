---
name: lt-api-ratelimit-helper
description: 'Skill: lt-api-ratelimit-helper'
license: MIT
tags:
- testing
tiered API plans, or concurrency limits. Also triggers on: token bucket, leaky bucket,
  sliding window,
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the API Ratelimit Output

Once the API ratelimit output is delivered, ask the user:

"Would you like me to generate API documentation for this design? (yes/no)"

If the user says **yes**:
- Check if the API Documentation skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the API Documentation skill
  - Use the API rate limiting output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the API Documentation skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

---
name: lt-graphql-grpc-helper
description: 'Skill: lt-graphql-grpc-helper'
license: MIT
tags:
- testing
Triggers on any mention of: schema definition language, SDL, resolvers, N+1 problem,
  federation,
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the API Design

Once the graphql/grpc design output is delivered, ask the user:

"Would you like me to generate API documentation for this design? (yes/no)"

If the user says **yes**:
- Check if the API Documentation skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the API Documentation skill
  - Use the API design output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the API Documentation skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

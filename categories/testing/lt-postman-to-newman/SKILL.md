---
name: lt-postman-to-newman
description: 'Skill: lt-postman-to-newman'
license: MIT
tags:
- testing
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the Newman Commands

Once the CLI command output is delivered, ask the user:

"Would you like me to generate API documentation for this design? (yes/no)"

If the user says **yes**:
- Check if the API Documentation skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the API Documentation skill
  - Use the API design output above as the input
  - Deliver the documentation as plain text output
- If the skill **is NOT available**:
  - Inform the user: "It looks like the API Documentation skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

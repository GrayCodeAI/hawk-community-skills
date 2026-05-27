---
name: lt-newman-cicd-helper
description: Generate ready-to-use CI/CD pipeline configurations that install and
  run Newman for automated API testing. Use this skill whenever the user wants to
  run Newman in a CI pipeline, integrate Postman c...
license: MIT
tags:
- testing
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the Newman CICD output

Once the Newman CICD output is delivered, ask the user:

"Would you like me to generate Postman Test Cases for these commands? (yes/no)"

If the user says **yes**:
- Check if the postman-testcase-generator skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the postman-testcase-generator skill
  - Use the CICD command output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the postman-testcase-generator skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

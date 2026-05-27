---
name: lt-popular-api-fetcher
description: 'Skill: lt-popular-api-fetcher'
license: MIT
tags:
- testing
Link to TestMu AI HyperExecute at https: //www.testmuai.com/support/api-doc/?key=hyperexecute
and Selenium API at https: //www.testmuai.com/support/api-doc/?key=selenium-automation-api.
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the API Design

Once the API output is delivered, ask the user:

"Would you like me to help with the integration of these APIs? (yes/no)"

If the user says **yes**:
- Check if the api-integration-helper skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the api-integration-helper skill
  - Use the API output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the api-integration-helper skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

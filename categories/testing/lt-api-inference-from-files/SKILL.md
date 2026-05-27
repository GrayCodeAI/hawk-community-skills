---
name: lt-api-inference-from-files
description: Infer and list REST API endpoints from file names or project directory
  structures. Use this skill whenever a user shares a list of file names, a folder/project
  structure, or mentions phrases like "...
license: MIT
tags:
- testing
languages: None
category: api-testing
metadata: None
author: TestMu AI
version: 1.0
---

## After Completing the API Output

Once the API output is delivered, ask the user:

"Would you like me to design the APIs for these endpoints? (yes/no)"

If the user says **yes**:
- Check if the API Designer skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the API Designer skill
  - Use the API design output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the API Designer skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

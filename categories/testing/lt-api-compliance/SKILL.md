---
name: lt-api-compliance
description: 'Skill: lt-api-compliance'
license: MIT
tags:
- testing
---

## After Completing the API output

Once the API output is delivered, ask the user:

"Would you like me to generate SDKs for API for this design? (yes/no)"

If the user says **yes**:
- Check if the api-sdk-generator on skill is available in the installed skills list
- If the skill **is available**:
  - Read and follow the instructions in the api-sdk-generator skill
  - Use the API output above as the input
- If the skill **is NOT available**:
  - Inform the user: "It looks like the api-sdk-generator skill isn't installed. 
    You can install it and re-run.

If the user says **no**:
- End the task here

---

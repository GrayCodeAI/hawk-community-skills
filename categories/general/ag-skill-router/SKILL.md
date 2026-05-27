---
name: ag-skill-router
description: Use when the user is unsure which skill to use or where to start. Interviews
  the user with targeted questions and recommends the best skill(s) from the installed
  library for their goal.
license: MIT
tags:
- general
risk: safe
source: self
---

## Limitations

- Only recommends skills from the installed library. If a skill is not
  installed, the recommendation may not work.
- Routing is based on natural language matching. Highly ambiguous goals
  may require follow-up clarification.
- Does not execute the recommended skill — it only recommends it. The user
  must invoke the skill themselves.
- The routing reference covers the most common skills but does not include
  every skill in the library.

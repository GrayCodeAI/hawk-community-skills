---
name: tl-domain-analysis
description: 'Skill: tl-domain-analysis'
license: MIT
tags:
- general
---

## Quick Analysis Template

Use this template when analyzing any codebase:

```markdown
## Codebase: {Name}

### Step 1: Concepts Extracted
- Entities: [list]
- Services: [list]
- Use Cases: [list]
- Controllers: [list]

### Step 2: Language Groups
- Group 1: {name} - terms: [list]
- Group 2: {name} - terms: [list]

### Step 3: Subdomains Identified
1. {Subdomain} (Core/Supporting/Generic)
   - Language: [terms]
   - Concepts: [list]
   - Cohesion: X/10
   - Bounded Context: {Name}Context

### Step 4: Cohesion Matrix
| Domain A | Domain B | Cohesion | Issue |
|----------|----------|----------|-------|
| ... | ... | X/10 | ... |

### Step 5: Issues Found
- Priority High: [list]
- Priority Medium: [list]
- Priority Low: [list]

### Step 6: Recommendations
1. [recommendation]
2. [recommendation]
```

---
name: ghcp-references-action-patterns-core
description: 'Skill: ghcp-references-action-patterns-core'
license: MIT
tags:
- general
---

### Sum an array (XPath trick)

Power Automate has no native `sum()` function. Use XPath on XML instead:

```json
"Prepare_For_Sum": {
  "type": "Compose",
  "runAfter": {},
  "inputs": { "root": { "numbers": "@body('Select_Amounts')" } }
},
"Sum": {
  "type": "Compose",
  "runAfter": { "Prepare_For_Sum": ["Succeeded"] },
  "inputs": "@xpath(xml(outputs('Prepare_For_Sum')), 'sum(/root/numbers)')"
}
```

`Select_Amounts` must output a flat array of numbers (use a **Select** action to extract a single numeric field first). The result is a number you can use directly in conditions or calculations.

> This is the only way to aggregate (sum/min/max) an array without a loop in Power Automate.

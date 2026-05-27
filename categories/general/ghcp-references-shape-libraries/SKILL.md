---
name: ghcp-references-shape-libraries
description: 'Skill: ghcp-references-shape-libraries'
license: MIT
tags:
- general
---

## Custom Shape Library Creation

A custom library is an XML file with `.xml` extension loaded via `File > Open Library`:

```xml
<mxlibrary>
  [
    {
      "xml": "&lt;mxCell value=\"Component\" style=\"rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;\" vertex=\"1\"&gt;&lt;mxGeometry width=\"120\" height=\"60\" as=\"geometry\" /&gt;&lt;/mxCell&gt;",
      "w": 120,
      "h": 60,
      "aspect": "fixed",
      "title": "My Component"
    }
  ]
</mxlibrary>
```

Each shape entry contains:
- `xml`: XML-escaped cell definition
- `w` / `h`: Default width/height
- `aspect`: `"fixed"` to lock ratio
- `title`: Name shown in panel

    }
  ]
</mxlibrary>
```

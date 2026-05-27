---
name: ghcp-references-drawio-xml-schema
description: 'Skill: ghcp-references-drawio-xml-schema'
license: MIT
tags:
- general
---

## Validation Rules

### Must Pass

- [ ] `id="0"` and `id="1"` cells always present as first two children of `<root>`
- [ ] No other cell uses `id="0"` or `id="1"`
- [ ] All `id` values are unique within each `<diagram>`
- [ ] Every `<mxCell>` has exactly one `<mxGeometry>` child
- [ ] `<mxGeometry>` has `as="geometry"` attribute
- [ ] Vertex cells have `vertex="1"`, edge cells have `edge="1"`
- [ ] Edge `source`/`target` IDs reference existing vertex IDs in the same diagram
- [ ] Swimlane children have `parent` set to the swimlane/lane ID, not `"1"`
- [ ] HTML in `value` attributes is XML-escaped

### Recommended

- [ ] Shapes do not overlap unless intentional (use ≥40px gap)
- [ ] Edge labels are short (≤4 words)
- [ ] Layer cells have descriptive `value` names
- [ ] All shapes fit within `pageWidth` × `pageHeight` bounds

---
name: ghcp-draw-io-diagram-generator-skill
description: Use when creating, editing, or generating draw.io diagram files (.drawio,
  .drawio.svg, .drawio.png). Covers mxGraph XML authoring, shape libraries, style
  strings, flowcharts, system architecture, s...
license: MIT
tags:
- general
---

## 11. References

All companion files are in `.github/skills/draw-io-diagram-generator/`:

| File | Contents |
|---|---|
| `references/drawio-xml-schema.md` | Complete mxfile / mxGraphModel / mxCell attribute reference, coordinate system, reserved cells, validation rules |
| `references/style-reference.md` | All style keys with allowed values, vertex and edge style keys, shape catalog, semantic color palette |
| `references/shape-libraries.md` | All shape library categories (General, Flowchart, UML, ER, Network, BPMN, Mockup, K8s) with style strings |
| `assets/templates/flowchart.drawio` | Ready-to-use flowchart template |
| `assets/templates/architecture.drawio` | 4-tier system architecture template |
| `assets/templates/sequence.drawio` | 3-actor sequence diagram template |
| `assets/templates/er-diagram.drawio` | 3-table ER diagram with crow's foot relationships |
| `assets/templates/uml-class.drawio` | Interface + 2 classes + enum with relationship arrows |
| `scripts/validate-drawio.py` | Python script to validate XML structure of any .drawio file |
| `scripts/add-shape.py` | Python CLI to add a new shape to an existing diagram |
| `scripts/README.md` | How to use the scripts with examples |

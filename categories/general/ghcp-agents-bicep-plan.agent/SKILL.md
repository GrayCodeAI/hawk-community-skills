---
name: ghcp-agents-bicep-plan.agent
description: Act as implementation planner for your Azure Bicep Infrastructure as
  Code task.
license: MIT
tags:
- general
tools: None
---

# Introduction

[1–3 sentences summarizing the plan and its purpose]

## Resources

<!-- Repeat this block for each resource -->

### {resourceName}

```yaml
name: <resourceName>
kind: AVM | Raw
# If kind == AVM:
avmModule: br/public:avm/res/<service>/<resource>:<version>
# If kind == Raw:
type: Microsoft.<provider>/<type>@<apiVersion>

purpose: <one-line purpose>
dependsOn: [<resourceName>, ...]

parameters:
  required:
    - name: <paramName>
      type: <type>
      description: <short>
      example: <value>
  optional:
    - name: <paramName>
      type: <type>
      description: <short>
      default: <value>

outputs:
- name: <outputName>
  type: <type>
  description: <short>

references:
docs: {URL to Microsoft Docs}
avm: {module repo URL or commit} # if applicable
```

# Implementation Plan

{Brief summary of overall approach and key dependencies}

## Phase 1 — {Phase Name}

**Objective:** {objective and expected outcomes}

{Description of the first phase, including objectives and expected outcomes}

<!-- Repeat Phase blocks as needed: Phase 1, Phase 2, Phase 3, … -->

- IMPLEMENT-GOAL-001: {Describe the goal of this phase, e.g., "Implement feature X", "Refactor module Y", etc.}

| Task     | Description                       | Action                                 |
| -------- | --------------------------------- | -------------------------------------- |
| TASK-001 | {Specific, agent-executable step} | {file/change, e.g., resources section} |
| TASK-002 | {...}                             | {...}                                  |

## High-level design

{High-level design description}
````

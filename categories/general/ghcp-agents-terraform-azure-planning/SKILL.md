---
name: ghcp-agents-terraform-azure-planning
description: Act as implementation planner for your Azure Terraform Infrastructure
  as Code task.
license: MIT
tags:
- general
tools:
- edit/editFiles
- fetch
- todos
- azureterraformbestpractices
- cloudarchitect
- documentation
- get_bestpractices
- microsoft-docs
---

# Introduction

[1–3 sentences summarizing the plan and its purpose]

## WAF Alignment

[Brief summary of how the WAF assessment shapes this implementation plan]

### Cost Optimization Implications

- [How budget constraints influence resource selection, e.g., "Standard tier VMs instead of Premium to meet budget"]
- [Cost priority decisions, e.g., "Reserved instances for long-term savings"]

### Reliability Implications

- [Availability targets affecting redundancy, e.g., "Zone-redundant storage for 99.9% availability"]
- [DR strategy impacting multi-region setup, e.g., "Geo-redundant backups for disaster recovery"]

### Security Implications

- [Data classification driving encryption, e.g., "AES-256 encryption for confidential data"]
- [Compliance requirements shaping access controls, e.g., "RBAC and private endpoints for restricted data"]

### Performance Implications

- [Performance tier selections, e.g., "Premium SKU for high-throughput requirements"]
- [Scaling decisions, e.g., "Auto-scaling groups based on CPU utilization"]

### Operational Excellence Implications

- [Monitoring level determining tools, e.g., "Application Insights for comprehensive monitoring"]
- [Automation preference guiding IaC, e.g., "Fully automated deployments via Terraform"]

## Resources

<!-- Repeat this block for each resource -->

### {resourceName}

```yaml
name: <resourceName>
kind: AVM | Raw
# If kind == AVM:
avmModule: registry.terraform.io/Azure/avm-res-<service>-<resource>/<provider>
version: <version>
# If kind == Raw:
resource: azurerm_<resource_type>
provider: azurerm
version: <provider_version>

purpose: <one-line purpose>
dependsOn: [<resourceName>, ...]

variables:
  required:
    - name: <var_name>
      type: <type>
      description: <short>
      example: <value>
  optional:
    - name: <var_name>
      type: <type>
      description: <short>
      default: <value>

outputs:
- name: <output_name>
  type: <type>
  description: <short>

references:
docs: {URL to Microsoft Docs}
avm: {module repo URL or commit} # if applicable
```

# Implementation Plan

{Brief summary of overall approach and key dependencies}

## Phase 1 — {Phase Name}

**Objective:**

{Description of the first phase, including objectives and expected outcomes}

- IMPLEMENT-GOAL-001: {Describe the goal of this phase, e.g., "Implement feature X", "Refactor module Y", etc.}

| Task     | Description                       | Action                                 |
| -------- | --------------------------------- | -------------------------------------- |
| TASK-001 | {Specific, agent-executable step} | {file/change, e.g., resources section} |
| TASK-002 | {...}                             | {...}                                  |

<!-- Repeat Phase blocks as needed: Phase 1, Phase 2, Phase 3, … -->
````

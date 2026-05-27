---
name: copilot-salesforce-component-standards
description: Quality standards for Salesforce Lightning Web Components (LWC), Aura
  components, and Visualforce pages. Covers SLDS 2 compliance, accessibility (WCAG
  2.1 AA), data access pattern selection, compon...
license: MIT
tags:
- general
---

## Quick Reference — Component Anti-Patterns Summary

| Anti-pattern | Technology | Risk | Fix |
|---|---|---|---|
| `innerHTML` with user data | LWC | XSS | Use template bindings `{expression}` |
| Hardcoded hex colours | LWC/Aura | Dark-mode / SLDS 2 break | Use SLDS CSS custom properties |
| Missing `aria-label` on icon buttons | LWC/Aura/VF | Accessibility failure | Add `alternative-text` or `aria-label` |
| No guard in `renderedCallback` | LWC | Infinite rerender loop | Add `hasRendered` boolean guard |
| Application event for parent-child | Aura | Unnecessary broadcast scope | Use component event instead |
| `escape="false"` on user data | Visualforce | XSS | Remove — use default escaping |
| Raw `<form>` postback | Visualforce | CSRF vulnerability | Use `<apex:form>` |
| No `with sharing` on custom controller | VF / Apex | Data exposure | Add `with sharing` declaration |
| FLS not checked in custom controller | VF / Apex | Privilege escalation | Add `Schema.sObjectType` checks |
| SOQL concatenated with URL param | VF / Apex | SOQL injection | Use bind variables |

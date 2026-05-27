---
name: mdc-dto-conventions
description: "Sets standards for Data Transfer Objects (DTOs), typically records, including parameter validation in compact canonical constructors."
license: MIT
tags: [cursor-rules]
---

- Must be of type record, unless specified in a prompt otherwise.
- Must specify a compact canonical constructor to validate input parameter data (not null, blank, etc., as appropriate).
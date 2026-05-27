---
name: arezv-email-template-builder
description: Email Template Builder
license: MIT
tags:
- general
---

## Common Pitfalls

- **Inline styles required** — most email clients strip `<head>` styles; React Email handles this
- **Max width 600px** — anything wider breaks on Gmail mobile
- **No flexbox/grid** — use `<Row>` and `<Column>` from react-email, not CSS grid
- **Dark mode media queries** — must use `!important` to override inline styles
- **Missing plain text** — all major providers have a plain text field; always populate it
- **Transactional vs marketing** — use separate sending domains/IPs to protect deliverability

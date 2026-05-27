---
name: tl-web-best-practices
description: Apply modern web development best practices for security, compatibility,
  and code quality. Use when asked to "apply best practices", "security audit", "modernize
  code", "code quality review", or "c...
license: MIT
tags:
- general
metadata: None
author: web-quality-skills
version: 1.0
---

## Audit checklist

### Security (critical)

- [ ] HTTPS enabled, no mixed content
- [ ] No vulnerable dependencies (`npm audit`)
- [ ] CSP headers configured
- [ ] Security headers present
- [ ] No exposed source maps

### Compatibility

- [ ] Valid HTML5 doctype
- [ ] Charset declared first in head
- [ ] Viewport meta tag present
- [ ] No deprecated APIs used
- [ ] Passive event listeners for scroll/touch

### Code quality

- [ ] No console errors
- [ ] Valid HTML (no duplicate IDs)
- [ ] Semantic HTML elements used
- [ ] Proper error handling
- [ ] Memory cleanup in components

### UX

- [ ] No intrusive interstitials
- [ ] Permission requests in context
- [ ] Clear error messages
- [ ] Appropriate image aspect ratios

## Tools

| Tool                                               | Purpose                    |
| -------------------------------------------------- | -------------------------- |
| `npm audit`                                        | Dependency vulnerabilities |
| [SecurityHeaders.com](https://securityheaders.com) | Header analysis            |
| [W3C Validator](https://validator.w3.org)          | HTML validation            |
| Lighthouse                                         | Best practices audit       |
| [Observatory](https://observatory.mozilla.org)     | Security scan              |

## References

- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Quality Audit](../web-quality-audit/SKILL.md)

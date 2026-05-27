---
name: ghcp-instructions-security-and-owasp.instruction
description: 'Skill: ghcp-instructions-security-and-owasp.instruction'
license: MIT
tags:
- general
---

## Security Checklist

### Authentication and Sessions
- [ ] Passwords hashed with Argon2id or bcrypt (cost >= 12)
- [ ] JWT signed with RS256/ES256, algorithm enforced on verify
- [ ] Access tokens expire in <= 15 minutes
- [ ] Refresh tokens: one-time use, rotated, stored in httpOnly cookie
- [ ] Rate limiting on login, registration, and password reset
- [ ] Session regenerated after authentication
- [ ] MFA available for privileged accounts

### Authorization
- [ ] Every API endpoint has auth middleware
- [ ] Ownership checks on all resource access (prevent IDOR)
- [ ] Server-side authorization (frontend guards are UX only)
- [ ] Mass assignment prevented (explicit field selection)
- [ ] Re-authentication required for sensitive operations

### Input and Output
- [ ] All user input validated server-side (zod/joi/class-validator)
- [ ] Parameterized queries for all database operations
- [ ] HTML output sanitized (DOMPurify) when rendering user content
- [ ] Error responses do not expose stack traces in production

### Secrets
- [ ] No hardcoded secrets in source code
- [ ] `.env` files in `.gitignore`
- [ ] Server secrets not exposed to client (no NEXT_PUBLIC_ on secrets)
- [ ] Environment variables validated at startup

### Headers
- [ ] Content-Security-Policy configured (nonce-based preferred)
- [ ] Strict-Transport-Security with preload
- [ ] X-Content-Type-Options: nosniff
- [ ] X-Frame-Options: DENY
- [ ] Referrer-Policy: strict-origin-when-cross-origin
- [ ] Permissions-Policy restricting unused APIs
- [ ] CORS restricted to known origins

### Dependencies
- [ ] `npm audit` (or equivalent) passing in CI
- [ ] Lockfile committed and verified with `npm ci`
- [ ] New dependencies reviewed for typosquatting and postinstall scripts
- [ ] No wildcard or "latest" versions in production

### Logging
- [ ] Security events logged (auth failures, access denied, rate limits)
- [ ] No sensitive data in logs (passwords, tokens, PII)
- [ ] Structured logging with correlation IDs
- [ ] Alerts configured for anomalous patterns

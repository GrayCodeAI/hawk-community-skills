---
name: arezv-senior-fullstack
description: Fullstack development toolkit with project scaffolding for Next.js, FastAPI,
  MERN, and Django stacks, code quality analysis with security and complexity scoring,
  and stack selection guidance. Use w...
license: MIT
tags:
- general
---

## Quick Reference

### Stack Decision Matrix

| Requirement | Recommendation |
|-------------|---------------|
| SEO-critical site | Next.js with SSR |
| Internal dashboard | React + Vite |
| API-first backend | FastAPI or Fastify |
| Enterprise scale | NestJS + PostgreSQL |
| Rapid prototype | Next.js API routes |
| Document-heavy data | MongoDB |
| Complex queries | PostgreSQL |

### Common Issues

| Issue | Solution |
|-------|----------|
| N+1 queries | Use DataLoader or eager loading |
| Slow builds | Check bundle size, lazy load |
| Auth complexity | Use Auth.js or Clerk |
| Type errors | Enable strict mode in tsconfig |
| CORS issues | Configure middleware properly |

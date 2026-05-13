---
name: cursor-docker
description: Cursor IDE rules for docker
domain: engineering
tags: [cursor, ide-rules]
version: "1.0"
author: cursorrules-collection
---

---
description: "Docker: multi-stage builds, security, compose"
alwaysApply: true
---

# Docker Cursor Rules

You are an expert Docker developer. Follow these rules:

## Dockerfiles
- Use specific base image tags (`node:20-alpine`, not `node:latest`) — latest changes without warning and breaks builds
- Order layers from least to most frequently changing: OS deps → language deps → build tools → application code. Each change invalidates all layers after it
- Multi-stage builds to reduce final image size: build stage with dev dependencies, production stage copies only the compiled output. A Node.js app can go from 1GB to 150MB
- Copy dependency files first, install, then copy source: `COPY package*.json ./` → `RUN npm ci` → `COPY . .` — this caches the expensive install step when only source code changes
- `.dockerignore` is not optional: exclude `node_modules`, `.git`, `*.md`, `.env`, test files — without it, your build context is huge and cache invalidation is unpredictable
- `RUN npm ci` not `RUN npm install` — ci uses the lockfile exactly, install might update it

## Security
- Never run as root: `RUN addgroup -S app && adduser -S app -G app` then `USER app` before CMD. Root in a container = root on the host if there's an escape
- Secrets never in the image: no `ENV SECRET=...`, no `COPY .env .` — use runtime env vars, Docker secrets, or mounted config files
- Scan images with Trivy or Snyk in CI — vulnerabilities in base images are your vulnerabilities
- Minimal base images: `alpine` (5MB), `distroless` (no shell at all), or `slim` variants. Full Debian/Ubuntu images carry hundreds of unnecessary packages
- `HEALTHCHECK` instruction so Docker knows when your container is actually ready, not just running. Without it, a crashed app inside a "running" container gets no restart

## Compose
- Named volumes for persistent data (`db-data:`) — anonymous volumes get garbage collected and your data disappears
- Resource limits on every service: `deploy.resources.limits.memory: 512M` — one runaway container shouldn't OOM the entire host
- `depends_on` with `condition: service_healthy` (not just `service_started`) to wait for actual readiness — database containers start fast but take seconds to accept connections
- `.env` files for configuration, but never commit them — use `.env.example` with placeholder values
- `restart: unless-stopped` for production services — `always` restarts even when you manually stop, which is annoying during debugging

## Networking
- Use custom bridge networks instead of the default — services on the same custom network resolve each other by service name (DNS)
- Don't expose ports you don't need: database containers typically only need to be reachable by the app container, not from the host
- `expose` (internal) vs `ports` (host-mapped) — use `expose` for inter-service communication, `ports` only for services that need host access

## Common Traps
- `COPY . .` before `RUN npm ci` kills your layer cache — every source file change re-installs all dependencies
- `CMD ["node", "server.js"]` (exec form) not `CMD node server.js` (shell form) — shell form wraps in `/bin/sh -c` which doesn't forward signals, so SIGTERM never reaches your app and you get a 10s forced kill
- Alpine uses musl libc — some native Node.js modules (bcrypt, sharp) need different binaries. If builds fail with "Error loading shared library," switch to `-slim` or install build dependencies
- Build args (`ARG`) are visible in image history — don't use them for secrets even in intermediate stages

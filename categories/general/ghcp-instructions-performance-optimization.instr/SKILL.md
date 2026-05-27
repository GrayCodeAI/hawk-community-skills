---
name: ghcp-instructions-performance-optimization.instr
description: 'Skill: ghcp-instructions-performance-optimization.instr'
license: MIT
tags:
- general
---

## Performance Checklist (CWV)

### LCP (< 2.5s)
- [ ] LCP image has `fetchpriority="high"` or `priority` prop
- [ ] LCP image preloaded if not in HTML source
- [ ] No `loading="lazy"` on above-fold images
- [ ] Critical CSS inlined or extracted
- [ ] No render-blocking scripts (use `defer` or `async`)
- [ ] Preconnect to critical third-party origins
- [ ] Main content server-rendered (not client-side fetched)
- [ ] Images in modern format (WebP/AVIF) with responsive `srcset`
- [ ] Compression enabled (Brotli preferred)
- [ ] Fonts preloaded with `font-display: swap` or `optional`

### INP (< 200ms)
- [ ] Event handlers complete in < 50ms
- [ ] Long tasks broken into smaller chunks
- [ ] Route-based code splitting implemented
- [ ] Heavy computation moved to Web Workers
- [ ] Lists with > 100 items virtualized
- [ ] No barrel file imports (direct component imports)
- [ ] ESM imports used (not CommonJS `require`)
- [ ] `"use client"` only on components that need interactivity
- [ ] Layout-triggering CSS properties not animated
- [ ] Effect cleanup implemented (no leaking listeners/timers)

### CLS (< 0.1)
- [ ] All images have `width` and `height` attributes
- [ ] Fonts use `font-display: swap` or `optional`
- [ ] No content injected above existing content dynamically
- [ ] Ads/embeds have reserved space
- [ ] No hydration mismatches
- [ ] `content-visibility: auto` has `contain-intrinsic-size`

---
name: ghcp-references-gsap
description: 'Skill: ghcp-references-gsap'
license: MIT
tags:
- general
---

## Common Copilot Pitfalls

**Forgot registerPlugin:** Copilot often omits `gsap.registerPlugin(ScrollTrigger)`.
Always add it before any ScrollTrigger usage.

**Wrong ease for scrub:** Copilot defaults to `power2.out` even on scrub animations.
Always use `ease: 'none'` when `scrub: true` or `scrub: number`.

**useEffect instead of useGSAP in React:** Copilot generates `useEffect` — always swap to `useGSAP`.

**Static end value for horizontal scroll:** Copilot writes `end: "+=" + container.offsetWidth`.
Correct: `end: () => "+=" + container.offsetWidth` (function form recalculates on resize).

**markers left in production:** Copilot adds `markers: true` and leaves it. Always remove.

**Scrub without pin on long animations:** Scrubbing a long timeline without pinning means
the element scrolls out of view. Add `pin: true` or shorten the scroll distance.

---
name: ghcp-references-framer
description: 'Skill: ghcp-references-framer'
license: MIT
tags:
- general
---

## Common Copilot Pitfalls

**Missing 'use client':** Copilot forgets to add this for Next.js App Router files.
Every file using `useScroll`, `useTransform`, `motion.*`, or any hook needs `'use client'` at the top.

**Using style prop on a plain div:** Copilot sometimes writes `<div style={{ y }}>` where `y` is a MotionValue.
This silently does nothing. Must be `<motion.div style={{ y }}>`.

**Old import path:** Copilot still generates `from 'framer-motion'` (valid, but legacy).
Current canonical: `from 'motion/react'`.

**Forgetting offset on useScroll:** Without `offset`, `scrollYProgress` tracks the full page
from 0 to 1 — not the element's position. Always pass `target` + `offset` for element-level tracking.

**Missing ref on target:** Copilot sometimes writes `target: ref` but forgets to attach `ref` to the DOM element.
```tsx
const ref = useRef(null);
const { scrollYProgress } = useScroll({ target: ref }); // ← ref passed
return <div ref={ref}>...</div>;                          // ← ref attached
```

**Using animate prop for scroll-linked values:** Scroll-linked values must use `style`, not `animate`.
`animate` runs on mount/unmount, not on scroll.
```tsx
// ❌ Wrong
<motion.div animate={{ opacity }} />

// ✅ Correct
<motion.div style={{ opacity }} />
```

**Not smoothing scroll progress:** Raw `scrollYProgress` can feel mechanical on fine motion.
Wrap in `useSpring` for progress bars and UI elements that need a polished feel.

---
name: agc-critique
description: 'Skill: agc-critique'
license: MIT
tags:
- general
---

## Self-review pass for drafted output

Before delivering drafted prose to the user, run this short pass:

- [ ] Through-line still holds across the whole piece
- [ ] Hook is specific and lands within the first paragraph (or first 60 seconds)
- [ ] Turn is explicit and concrete
- [ ] Stakes are named, not only implied
- [ ] Resolution is concrete (specific new state or action)
- [ ] No closing summary paragraph
- [ ] No slop adjectives, filler verbs, AI sentence openers
- [ ] Sentence length varies
- [ ] Concrete nouns / specific examples present
- [ ] Voice matches what the user signalled / sounds human

Fix anything that fails before returning the output. If a structural issue surfaces (turn missing, through-line drifting), surface it to the user rather than silently rewriting - they may have a reason for the choice.

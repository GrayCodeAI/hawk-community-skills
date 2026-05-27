---
name: agc-sub_agent_prompt
description: 'Skill: agc-sub_agent_prompt'
license: MIT
tags:
- general
---

# <Title>

<Body using source_text_paragraphs verbatim, woven into the layout from the rendered JPG. Preserve columns, panels, callouts, ordering.>

<Where an embedded image sits in the layout, insert at that position:>

> **Image: <short label>**
> <Description of what's shown. Length depends on the image:
>   - Decorative or repeating visuals (icons, brand motifs, generic graphics, repeated bricks/shapes): ONE sentence.
>   - Screenshots, diagrams, code blocks, content-bearing visuals: 2-4 sentences with specifics so a reader without the image still grasps WHY it's on the slide.>
> Source: `{EMBEDDED_DIR_RELATIVE}<image filename>`

## Speaker notes

<Verbatim notes, or "_(none)_" if empty.>

## External links

<Bulleted list ONLY for links that appear on the slide but are NOT already in the body content above. Omit the section entirely if all links are already in the body, or if there are none.>

Rules:
- Use source_text_paragraphs as authoritative wording. Do not paraphrase.
- The rendered JPG is for layout, ordering, and reading text the XML missed (e.g. SmartArt, grouped shapes). Include such text inline.
- Australian English. No emojis. No marketing fluff. Plain hyphens, plain quotes, no em-dashes.
{DECK_SPECIFIC_NOTES}

Reply with one short line confirming the path written and the inferred title. Nothing else.
```

## Why each rule matters

- **Three inputs in one agent.** Source text alone loses image context. Image
  captions alone lose layout context. Giving the agent text + rendered slide
  + standalone PNGs lets it use each input for what it's best at: source
  text as ground truth, rendered slide for layout and any text the XML
  missed (SmartArt, grouped shapes), individual PNGs for high-res image
  description.

- **Length-tuned image descriptions.** Without this rule, agents write the
  same 2-4 sentence description for every visual, including decorative
  brand icons that appear on every slide. The "one sentence for decorative,
  2-4 for content-bearing" rule was added after a pilot showed repetitive
  descriptions of identical lego-brick icons.

- **External links de-duplication.** Agents tend to copy URLs both inline
  in the body (where they appear on the slide) and into a dedicated
  External links section. The rule keeps each URL in one place.

- **Single-line reply.** Each agent returns only a confirmation line so the
  orchestrator's context stays clean across many parallel runs.

## Optional deck-specific notes

When the source deck has terminology that should not be modernised during
extraction (e.g. references to a deprecated tool that the user wants kept
verbatim until a later content-uplift pass), append a line like:

```
- The deck references "Cline" (an older agent) in places - keep verbatim; do not modernise.
```

Add it via `{DECK_SPECIFIC_NOTES}` rather than rewriting the template.

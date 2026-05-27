---
name: ghcp-references-writing-mathematical-expressio
description: 'Skill: ghcp-references-writing-mathematical-expressio'
license: MIT
tags:
- general
---

## Dollar Sign Inline with Mathematical Expression

### Markdown

```markdown
This expression uses `\$` to display a dollar sign: $`\sqrt{\$4}`$
```

### Parsed HTML

```html
<p>This expression uses
 <code>\$</code> to display a dollar sign:
 <math-renderer>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
   <msqrt>
    <mi>$</mi>
    <mn>4</mn>
   </msqrt>
  </math>
 </math-renderer>
</p>
```

### Markdown

```markdown
To split <span>$</span>100 in half, we calculate $100/2$
```

### Parsed HTML

```html
<p>To split
 <span>$</span>100 in half, we calculate
 <math-renderer>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
   <mn>100</mn>
   <mrow data-mjx-texclass="ORD">
    <mo>/</mo>
   </mrow>
   <mn>2</mn>
  </math>
 </math-renderer>
</p>
```

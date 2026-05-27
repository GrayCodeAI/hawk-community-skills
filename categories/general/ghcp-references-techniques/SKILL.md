---
name: ghcp-references-techniques
description: 'Skill: ghcp-references-techniques'
license: MIT
tags:
- general
---

## Crisp Pixel Art Look

**Source:** [MDN - Crisp Pixel Art Look](https://developer.mozilla.org/en-US/docs/Games/Techniques/Crisp_pixel_art_look)

### What It Is

A technique for rendering pixel art without blurriness on high-resolution displays by mapping individual image pixels to blocks of screen pixels without smoothing interpolation. Retro pixel art requires preserving hard edges during scaling, but modern browsers default to smoothing algorithms that blend colors and create blur.

### How It Works

The CSS `image-rendering` property controls how browsers scale images. Setting it to `pixelated` enforces nearest-neighbor scaling, which preserves the crisp, blocky look of pixel art instead of applying bilinear or bicubic smoothing.

**Key CSS values:**
- `pixelated` -- preserves crisp edges for pixel art.
- `crisp-edges` -- alternative supported on some browsers.

### When to Use It

- Retro-style games with pixel art assets.
- Any game where you want a deliberately blocky, pixelated visual style.
- When scaling small sprite images to larger display sizes.

### Technique 1: Scaling `<img>` Elements with CSS

```html
<img
  src="character.png"
  alt="pixel art character, upscaled with CSS, appearing crisp" />
```

```css
img {
  width: 48px;
  height: 136px;
  image-rendering: pixelated;
}
```

### Technique 2: Crisp Pixel Art in Canvas

Set the canvas `width`/`height` attributes to the original pixel art resolution, then use CSS `width`/`height` for scaling (e.g., 4x scale: 128 pixels to 512px CSS width).

```html
<canvas id="game" width="128" height="128">A cat</canvas>
```

```css
canvas {
  width: 512px;
  height: 512px;
  image-rendering: pixelated;
}
```

```javascript
const ctx = document.getElementById("game").getContext("2d");

const image = new Image();
image.onload = () => {
  ctx.drawImage(image, 0, 0);
};
image.src = "cat.png";
```

### Technique 3: Arbitrary Canvas Scaling with Correction

For non-integer scale factors, image pixels must align to canvas pixels at integer multiples:

```javascript
const ctx = document.getElementById("game").getContext("2d");
ctx.scale(0.8, 0.8);

const image = new Image();
image.onload = () => {
  // Correct formula: dWidth = sWidth / xScale * n (where n is an integer)
  ctx.drawImage(image, 0, 0, 128, 128, 0, 0, 128 / 0.8, 128 / 0.8);
};
image.src = "cat.png";
```

When using `drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)`:
- `dWidth` must equal `sWidth / xScale * n`
- `dHeight` must equal `sHeight / yScale * m`
- Where `n` and `m` are positive integers (1, 2, 3, etc.)

### Known Limitations

**devicePixelRatio misalignment:** When `devicePixelRatio` is not an integer (e.g., at 110% browser zoom), pixels may render unevenly because CSS pixels cannot perfectly map to device pixels. This creates a non-uniform appearance without an easy solution.

### Best Practices

1. Use integer scale factors (2x, 3x, 4x) whenever possible.
2. Preserve the aspect ratio -- scale width and height equally.
3. Test across different browser zoom levels.
4. Avoid fractional canvas scale factors or drawImage dimensions.
5. Include descriptive `aria-label` attributes on canvas elements for accessibility.

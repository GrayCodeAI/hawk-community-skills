---
name: pptx
description: 'Use this skill any time a .pptx file is involved in any way — as input,
  output, or both. This includes: creating slide decks, pitch decks, or presentations;
  reading, parsing, or extracting text fro...'
license: Proprietary. LICENSE.txt has complete terms
tags:
- general
---

## Dependencies

- `pip install "markitdown[pptx]"` - text extraction
- `pip install Pillow` - thumbnail grids
- `npm install -g pptxgenjs` - creating from scratch
- LibreOffice (`soffice`) - PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- Poppler (`pdftoppm`) - PDF to images

---
name: sci-docx
description: 'Use this skill whenever the user wants to create, read, edit, or manipulate
  Word documents (.docx files). Triggers include: any mention of ''Word doc'', ''word
  document'', ''.docx'', or requests to produ...'
license: Proprietary. LICENSE.txt has complete terms
tags:
- scientific
---

## Dependencies

- **pandoc**: Text extraction
- **docx**: `npm install -g docx` (new documents)
- **LibreOffice**: PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- **Poppler**: `pdftoppm` for images

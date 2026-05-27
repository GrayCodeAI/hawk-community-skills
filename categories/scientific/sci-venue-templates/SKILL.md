---
name: sci-venue-templates
description: Access comprehensive LaTeX templates, formatting requirements, and submission
  guidelines for major scientific publication venues (Nature, Science, PLOS, IEEE,
  ACM), academic conferences (NeurIPS, I...
license: MIT license
tags:
- scientific
allowed-tools: Read Write Edit Bash
metadata: None
skill-author: K-Dense Inc.
---

## Resources

### Bundled Resources

**Writing Style Guides** (in `references/`):
- `venue_writing_styles.md`: Master style overview and comparison
- `nature_science_style.md`: Nature/Science writing conventions
- `cell_press_style.md`: Cell Press journal style
- `medical_journal_styles.md`: Medical journal writing guide
- `ml_conference_style.md`: ML conference writing conventions
- `cs_conference_style.md`: CS conference writing guide
- `reviewer_expectations.md`: What reviewers look for by venue

**Formatting Requirements** (in `references/`):
- `journals_formatting.md`: Comprehensive journal formatting requirements
- `conferences_formatting.md`: Conference paper specifications
- `posters_guidelines.md`: Research poster design and sizing
- `grants_requirements.md`: Grant proposal requirements by agency

**Writing Examples** (in `assets/examples/`):
- `nature_abstract_examples.md`: High-impact journal abstract examples
- `neurips_introduction_example.md`: ML conference introduction format
- `cell_summary_example.md`: Cell Press Summary/Highlights/eTOC
- `medical_structured_abstract.md`: NEJM/Lancet/JAMA abstract format

**Templates** (in `assets/`):
- `journals/`: Journal article LaTeX templates
- `posters/`: Research poster templates
- `grants/`: Grant proposal templates

**Scripts** (in `scripts/`):
- `query_template.py`: Search and retrieve templates
- `customize_template.py`: Customize with author info
- `validate_format.py`: Check compliance with requirements

### External Resources

**Journal Author Guidelines**:
- Nature: https://www.nature.com/nature/for-authors
- Science: https://www.science.org/content/page/instructions-authors
- PLOS: https://plos.org/resources/for-authors/
- Cell Press: https://www.cell.com/author-guidelines

**Conference Formatting**:
- NeurIPS: https://neurips.cc/Conferences/2024/CallForPapers
- ICML: https://icml.cc/Conferences/2024/StyleAuthorInstructions
- CVPR: https://cvpr.thecvf.com/Conferences/2024/AuthorGuidelines

**Grant Resources**:
- NSF PAPPG: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg
- NIH Forms: https://grants.nih.gov/grants/how-to-apply-application-guide.html
- DOE Funding: https://science.osti.gov/grants

## Example Usage

### Example 1: Nature Article Submission

```markdown
User: "I need to prepare a manuscript for Nature"

Response:
1. Load Nature formatting requirements (references/journals_formatting.md)
2. Retrieve Nature template (assets/journals/nature_article.tex)
3. Key requirements:
   - Length: ~3000 words, ~5 pages
   - Format: Single column, 12pt font
   - Citations: Numbered superscript (Nature style)
   - Figures: 300+ dpi, RGB color
4. Customize template with your title, authors, affiliations
5. Compile and validate against requirements
```

### Example 2: NeurIPS Conference Paper

```markdown
User: "What are the formatting requirements for NeurIPS?"

Response:
From references/conferences_formatting.md:
- Page limit: 8 pages main text + unlimited references/appendix
- Format: Two-column, 10pt font
- Template: neurips_2024.sty (official style file)
- Anonymization: Required for initial submission
- Citations: Numbered (brackets)
- Figures: High resolution, colorblind-safe recommended
```

### Example 3: NSF Proposal

```markdown
User: "Help me format an NSF proposal"

Response:
NSF requirements (from references/grants_requirements.md):
- Project Description: 15 pages maximum
- Project Summary: 1 page (Overview, Intellectual Merit, Broader Impacts)
- Budget Justification: 3-5 pages
- Biographical Sketch: 3 pages per senior personnel
- Font: Minimum 10pt, Times Roman or similar
- Margins: 1 inch all sides
Template: assets/grants/nsf_proposal_template.tex
```

### Example 4: Conference Poster

```markdown
User: "I need to create a poster for ISMB"

Response:
ISMB poster specifications:
- Size: Typically A0 portrait (33.1 × 46.8 inches)
- Recommended template: beamerposter or tikzposter
- Font sizes: Title 60-85pt, Headers 36-48pt, Body 24-32pt
- Include: QR code for paper/supplementary materials
Available templates:
- assets/posters/beamerposter_academic.tex
```

## Updates and Maintenance

**Template Currency**:
- Templates updated annually or when venues release new guidelines
- Last updated: 2024
- Check official venue sites for most current requirements

**Reporting Issues**:
- Template compilation errors
- Outdated formatting requirements
- Missing venue templates
- Incorrect specifications

## Summary

The venue-templates skill provides comprehensive access to:

1. **50+ publication venue templates** across disciplines
2. **Detailed formatting requirements** for journals, conferences, posters, grants
3. **Helper scripts** for template discovery, customization, and validation
4. **Integration** with other scientific writing skills
5. **Best practices** for successful academic submissions

Use this skill whenever you need venue-specific formatting guidance or templates for academic publishing.

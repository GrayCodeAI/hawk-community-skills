---
name: ag-hugging-face-paper-publisher
description: Publish and manage research papers on Hugging Face Hub. Supports creating
  paper pages, linking papers to models/datasets, claiming authorship, and generating
  professional markdown-based research ar...
license: MIT
tags:
- general
source: https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher
risk: unknown
---

# Dataset Name

Dataset introduced in [Our Paper](https://arxiv.org/abs/2301.12345).

For more details, see the [paper page](https://huggingface.co/papers/2301.12345).
```

The Hub automatically extracts arXiv IDs from these links and creates `arxiv:2301.12345` tags.

### Integration Examples

**Workflow 1: Publish New Research**
```bash
# 1. Create research article
uv run scripts/paper_manager.py create \
  --template "modern" \
  --title "Novel Fine-Tuning Approach" \
  --output "paper.md"

# 2. Edit paper.md with your content

# 3. Submit to arXiv (external process)
# Upload to arxiv.org, get arXiv ID

# 4. Index on Hugging Face
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"

# 5. Link to your model
uv run scripts/paper_manager.py link \
  --repo-id "your-username/your-model" \
  --repo-type "model" \
  --arxiv-id "2301.12345"

# 6. Claim authorship
uv run scripts/paper_manager.py claim \
  --arxiv-id "2301.12345" \
  --email "your.email@edu"
```

**Workflow 2: Link Existing Paper**
```bash
# 1. Check if paper exists
uv run scripts/paper_manager.py check --arxiv-id "2301.12345"

# 2. Index if needed
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"

# 3. Link to multiple repositories
uv run scripts/paper_manager.py link \
  --repo-id "username/model-v1" \
  --repo-type "model" \
  --arxiv-id "2301.12345"

uv run scripts/paper_manager.py link \
  --repo-id "username/training-data" \
  --repo-type "dataset" \
  --arxiv-id "2301.12345"

uv run scripts/paper_manager.py link \
  --repo-id "username/demo-space" \
  --repo-type "space" \
  --arxiv-id "2301.12345"
```

**Workflow 3: Update Model with Paper Reference**
```bash
# 1. Get current README
hf download username/model-name README.md

# 2. Add paper link
uv run scripts/paper_manager.py link \
  --repo-id "username/model-name" \
  --repo-type "model" \
  --arxiv-id "2301.12345" \
  --citation "Full citation for the paper"

# The script will:
# - Add YAML metadata if missing
# - Insert arXiv link in README
# - Add formatted citation
# - Preserve existing content
```

### Best Practices

1. **Paper Indexing**
   - Index papers as soon as they're published on arXiv
   - Include full citation information in model/dataset cards
   - Use consistent paper references across related repositories

2. **Metadata Management**
   - Add YAML frontmatter to all model/dataset cards
   - Include proper licensing information
   - Tag with relevant task categories and domains

3. **Authorship**
   - Claim authorship on papers where you're listed as author
   - Use institutional email addresses for verification
   - Keep paper visibility settings updated

4. **Repository Linking**
   - Link papers to all relevant models, datasets, and Spaces
   - Include paper context in README descriptions
   - Add BibTeX citations for easy reference

5. **Research Articles**
   - Use templates consistently within projects
   - Include code and data links in papers
   - Generate web-friendly HTML versions for sharing

### Advanced Usage

**Batch Link Papers:**
```bash
# Link multiple papers to one repository
for arxiv_id in "2301.12345" "2302.67890" "2303.11111"; do
  uv run scripts/paper_manager.py link \
    --repo-id "username/model-name" \
    --repo-type "model" \
    --arxiv-id "$arxiv_id"
done
```

**Extract Paper Info:**
```bash
# Get paper metadata from arXiv
uv run scripts/paper_manager.py info \
  --arxiv-id "2301.12345" \
  --format "json"
```

**Generate Citation:**
```bash
# Create BibTeX citation
uv run scripts/paper_manager.py citation \
  --arxiv-id "2301.12345" \
  --format "bibtex"
```

**Validate Links:**
```bash
# Check all paper links in a repository
uv run scripts/paper_manager.py validate \
  --repo-id "username/model-name" \
  --repo-type "model"
```

### Error Handling

- **Paper Not Found**: arXiv ID doesn't exist or isn't indexed yet
- **Permission Denied**: HF_TOKEN lacks write access to repository
- **Invalid YAML**: Malformed metadata in README frontmatter
- **Authorship Failed**: Email doesn't match paper author records
- **Already Claimed**: Another user has claimed authorship
- **Rate Limiting**: Too many API requests in short time

### Troubleshooting

**Issue**: "Paper not found on Hugging Face"
- **Solution**: Visit `hf.co/papers/{arxiv-id}` to trigger indexing

**Issue**: "Authorship claim not verified"
- **Solution**: Wait for admin review or contact HF support with proof

**Issue**: "arXiv tag not appearing"
- **Solution**: Ensure README includes proper arXiv URL format

**Issue**: "Cannot link to repository"
- **Solution**: Verify HF_TOKEN has write permissions

**Issue**: "Template rendering errors"
- **Solution**: Check markdown syntax and YAML frontmatter format

### Resources and References

- **Hugging Face Paper Pages**: [hf.co/papers](https://huggingface.co/papers)
- **Model Cards Guide**: [hf.co/docs/hub/model-cards](https://huggingface.co/docs/hub/en/model-cards)
- **Dataset Cards Guide**: [hf.co/docs/hub/datasets-cards](https://huggingface.co/docs/hub/en/datasets-cards)
- **Research Article Template**: [tfrere/research-article-template](https://huggingface.co/spaces/tfrere/research-article-template)
- **arXiv Format Guide**: [arxiv.org/help/submit](https://arxiv.org/help/submit)

### Integration with tfrere's Research Template

This skill complements [tfrere's research article template](https://huggingface.co/spaces/tfrere/research-article-template) by providing:

- Automated paper indexing workflows
- Repository linking capabilities
- Metadata management tools
- Citation generation utilities

You can use tfrere's template for writing, then use this skill to publish and link the paper on Hugging Face Hub.

### Common Patterns

**Pattern 1: New Paper Publication**
```bash
# Write → Publish → Index → Link
uv run scripts/paper_manager.py create --template modern --output paper.md
# (Submit to arXiv)
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"
uv run scripts/paper_manager.py link --repo-id "user/model" --arxiv-id "2301.12345"
```

**Pattern 2: Existing Paper Discovery**
```bash
# Search → Check → Link
uv run scripts/paper_manager.py search --query "transformers"
uv run scripts/paper_manager.py check --arxiv-id "2301.12345"
uv run scripts/paper_manager.py link --repo-id "user/model" --arxiv-id "2301.12345"
```

**Pattern 3: Author Portfolio Management**
```bash
# Claim → Verify → Organize
uv run scripts/paper_manager.py claim --arxiv-id "2301.12345"
uv run scripts/paper_manager.py list-my-papers
uv run scripts/paper_manager.py toggle-visibility --arxiv-id "2301.12345" --show true
```

### API Integration

**Python Script Example:**
```python
from scripts.paper_manager import PaperManager

pm = PaperManager(hf_token="your_token")

# Index paper
pm.index_paper("2301.12345")

# Link to model
pm.link_paper(
    repo_id="username/model",
    repo_type="model",
    arxiv_id="2301.12345",
    citation="Full citation text"
)

# Check status
status = pm.check_paper("2301.12345")
print(status)
```

### Future Enhancements

Planned features for future versions:
- Support for non-arXiv papers (conference proceedings, journals)
- Automatic citation formatting from DOI
- Paper comparison and versioning tools
- Collaborative paper writing features
- Integration with LaTeX workflows
- Automated figure and table extraction
- Paper metrics and impact tracking

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

---
name: ag-hugging-face-datasets
description: Create and manage datasets on Hugging Face Hub. Supports initializing
  repos, defining configs/system prompts, streaming row updates, and SQL-based dataset
  querying/transformation. Designed to work ...
license: MIT
tags:
- general
risk: unknown
source: community
---

# Combined Workflow Examples

## Example 1: Create Training Subset from Existing Dataset
```bash
# 1. Explore the source dataset
uv run scripts/sql_manager.py describe --dataset "cais/mmlu"
uv run scripts/sql_manager.py histogram --dataset "cais/mmlu" --column "subject"

# 2. Query and create subset
uv run scripts/sql_manager.py query \
  --dataset "cais/mmlu" \
  --sql "SELECT * FROM data WHERE subject IN ('nutrition', 'anatomy', 'clinical_knowledge')" \
  --push-to "username/mmlu-medical-subset" \
  --private
```

## Example 2: Transform and Reshape Data
```bash
# Transform MMLU to QA format with correct answers extracted
uv run scripts/sql_manager.py query \
  --dataset "cais/mmlu" \
  --sql "SELECT question, choices[answer] as correct_answer, subject FROM data" \
  --push-to "username/mmlu-qa-format"
```

## Example 3: Merge Multiple Dataset Splits
```bash
# Export multiple splits and combine
uv run scripts/sql_manager.py export \
  --dataset "cais/mmlu" \
  --split "*" \
  --output "mmlu_all.parquet"
```

## Example 4: Quality Filtering
```bash
# Filter for high-quality examples
uv run scripts/sql_manager.py query \
  --dataset "squad" \
  --sql "SELECT * FROM data WHERE LENGTH(context) > 500 AND LENGTH(question) > 20" \
  --push-to "username/squad-filtered"
```

## Example 5: Create Custom Training Dataset
```bash
# 1. Query source data
uv run scripts/sql_manager.py export \
  --dataset "cais/mmlu" \
  --sql "SELECT question, subject FROM data WHERE subject='nutrition'" \
  --output "nutrition_source.jsonl" \
  --format jsonl

# 2. Process with your pipeline (add answers, format, etc.)

# 3. Push processed data
uv run scripts/dataset_manager.py init --repo_id "username/nutrition-training"
uv run scripts/dataset_manager.py add_rows \
  --repo_id "username/nutrition-training" \
  --template qa \
  --rows_json "$(cat processed_data.json)"
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

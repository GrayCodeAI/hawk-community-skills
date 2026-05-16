.PHONY: lint format validate test help

lint: ## Run ruff linter on tool scripts
	ruff check tools/

format: ## Format tool scripts
	ruff format tools/

validate: ## Validate all skills in the registry
	python tools/validate_skill.py

test: lint validate ## Run all checks

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

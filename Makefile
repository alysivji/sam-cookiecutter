.PHONY: help

help: ## help
	@echo "Makefile for managing SAM Cookiecutter:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

##############
# Dependencies
##############

install:  ## install requirements
	pip install -r requirements_dev.txt

requirements:  ## generate requirements.txt
	pip-compile --output-file=requirements.txt requirements.in

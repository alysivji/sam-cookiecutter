.PHONY: help

help: ## help
	@echo "Makefile for managing {{ cookiecutter.project_name }} project:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

##############
# Dependencies
##############

requirements:  ## generate requirements.txt
	pip-compile --output-file=requirements.txt requirements.in
	pip-compile --output-file=app/requirements.txt app/requirements.in

install:  ## install requirements
	pip install -r requirements_dev.txt
	pip install -r app/requirements.txt

###################
# Local Development
###################
up:  ## bring up local development environment
	docker-compose up -d

down:  ## take down local development environment
	docker-compose down

shell:  ## open ipython shell
	ipython

test:  ## run tests
	pytest

logs:  ## see localstack logs
	docker-compose logs $(args) localstack

logs-f:  ## see localstack logs and follow tail
	docker-compose logs -f localstack

dynamodb-admin:
	DYNAMO_ENDPOINT=http://localhost:4566 dynamodb-admin

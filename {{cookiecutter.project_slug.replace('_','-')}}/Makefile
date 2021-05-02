.PHONY: help

help: ## help
	@echo "Makefile for managing {{ cookiecutter.project_name }} project:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:
	sam build --use-container

deploy: build
	sam deploy --config-env default

##############
# Dependencies
##############
install:  ## install all requirements (including dev) into venv
	pip install -r requirements_dev.txt
	pip install -r app/requirements.txt

install-lambda:  ## install lambda requirements in venv
	pip install -r app/requirements.txt

requirements:  ## make project requirements file
	pip-compile --output-file=requirements.txt requirements.in

requirements-lambda:  ## make lambda requirements file
	pip-compile --output-file=app/requirements.txt app/requirements.in

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
	PYTHONPATH=`pwd`/app pytest $(args)

test-cov:  ## run tests with coverage
	PYTHONPATH=`pwd`/app pytest --cov app/ $(args)

logs:  ## see localstack logs
	docker-compose logs $(args) localstack

logs-f:  ## see localstack logs and follow tail
	docker-compose logs -f localstack

dynamodb-admin:
	DYNAMO_ENDPOINT=http://localhost:4566 dynamodb-admin

# {{ cookiecutter.project_name.title() }}

{{ cookiecutter.project_description }}

## Contributing

This section contains information about how to work in this repository.

### Creating Local Development Environment

1. Clone repo
1. Create and activate virtual environment for Python 3.8.x
1. `pip install pre-commit==2.9.3`
1. `pre-commit install`
1. `make install`
1. `make up` to bring up [LocalStack](https://github.com/localstack/localstack)
1. `make deploy-local` to deploy project resources to LocalStack container

# data-collector

## Pre-requisite
- Python 3.12
- Poetry (Used for dependency management), [How to install Poetry](https://python-poetry.org/docs/#installation)

## How To Install This Project
- Configure Virtual Environment inside project
```sh
poetry config virtualenvs.in-project true
```
- Install Required Dependency
```sh
poetry install
```
- Generate Report
```sh
poetry run python -m gunicorn --bind 0.0.0.0:8080 runner:app
```

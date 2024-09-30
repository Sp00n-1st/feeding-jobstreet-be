# feeding-jobstreet-be

## Pre-requisite

- Preferred use WSL for Development Environment
- Python 3.12
- Poetry (Used for dependency management), [How to install Poetry](https://python-poetry.org/docs/#installation)

## How To Install This Project

- Poetry use python3.12

```sh
poetry env use python3.12
```

- Configure Virtual Environment inside project

```sh
poetry config virtualenvs.in-project true
```

- Install Required Dependency

```sh
poetry install
```

- Run project

```sh
poetry run python -m gunicorn --log-level=info runner:app
```

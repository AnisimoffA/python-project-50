lint: 
	poetry run flake8 gendiff

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --gendiff --cov-report xml


selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

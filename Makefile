lint: 
	poetry run flake8 gendiff

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov-report xml


selfcheck:
	poetry check

check: selfcheck lint test 

build: check
	poetry build

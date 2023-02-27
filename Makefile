lint: 
	poetry run flake8 gendiff tests

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml


selfcheck:
	poetry check

check: selfcheck lint test 

build: check
	poetry build

push:
	python3 -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall
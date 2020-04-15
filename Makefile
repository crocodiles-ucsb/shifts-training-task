CODE = src
TESTS = tests

ALL = $(CODE) $(TESTS)

VENV ?= .venv

venv:
	python -m venv $(VENV)
	.venv\Scripts\activate
	python -m pip install --upgrade pip
	python -m pip install poetry
	poetry install
	.venv\Scripts\activate

test:
	pytest -v tests

lint:
	flake8 --jobs 4 --statistics --show-source $(ALL)
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	black --skip-string-normalization --check $(ALL)

format:
	isort --apply --recursive $(ALL)
	black --skip-string-normalization $(ALL)
	autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
	unify --in-place --recursive $(ALL)

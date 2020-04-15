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
	$(VENV)/bin/flake8 --jobs 4 --statistics --show-source $(ALL)
	$(VENV)/bin/pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	$(VENV)/bin/black --skip-string-normalization --check $(ALL)

format:
	$(VENV)/bin/isort --apply --recursive $(ALL)
	$(VENV)/bin/black --skip-string-normalization $(ALL)
	$(VENV)/bin/autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
	$(VENV)/bin/unify --in-place --recursive $(ALL)

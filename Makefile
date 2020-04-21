CODE = src
TESTS = tests

ALL = $(CODE) $(TESTS)

VENV ?= .venv

venv:
	python -m venv $(VENV)
	.venv\Lib\site-packages python -m pip install --upgrade pip
	.venv\Lib\site-packages python -m pip install poetry
	.venv\Lib\site-packages poetry install
	.venv\Scripts\activate
#	python3 -m venv $(VENV)
#	$(VENV)/bin/python -m pip install --upgrade pip
#	$(VENV)/bin/python -m pip install poetry
#	$(VENV)/bin/poetry install



test:
	pytest -v tests
	#$(VENV)/bin/pytest -v tests

lint:
	flake8 --jobs 4 --statistics --show-source $(ALL)
	pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	black --skip-string-normalization --check $(ALL)
#	$(VENV)/bin/flake8 --jobs 4 --statistics --show-source $(ALL)
#	$(VENV)/bin/pylint --jobs 4 --rcfile=setup.cfg $(CODE)
#	$(VENV)/bin/black --skip-string-normalization --check $(ALL)



format:
	isort --apply --recursive $(ALL)
	black --skip-string-normalization $(ALL)
	autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
	unify --in-place --recursive $(ALL)

#	$(VENV)/bin/isort --apply --recursive $(ALL)
#	$(VENV)/bin/black --skip-string-normalization $(ALL)
#	$(VENV)/bin/autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
#	$(VENV)/bin/unify --in-place --recursive $(ALL)



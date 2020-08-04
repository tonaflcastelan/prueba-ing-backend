SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests


setup:
	@( \
		if [ ! -f .env ] ; then cp .env.mock .env ; fi; \
		make install; \
	)

install:
	@( \
		if [ ! -d .venv ] ; then python3 -m venv --copies .venv; fi; \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements-dev.txt; \
		pip install -r requirements.txt; \
	)

black:
	@black . --exclude '.venv|build|target|dist' --check;

isort:
	@isort --recursive --skip .venv --check-only; \

autoflake:
	@autoflake --recursive --exclude .venv --check --remove-all-unused-imports --remove-unused-variables ./; \

lint: black isort

lint-fix:
	@( \
		black . --exclude '.venv|build|target|dist'; \
		isort --recursive --apply --skip .venv; \
		autoflake --recursive --exclude venv --in-place --remove-all-unused-imports ./; \
	)

tests:
	@python -m pytest --cov=src --color=yes \
			--cov-report term \
			--cov-report html:coverage \
			--junit-xml=junit.xml \
			--rootdir=. $${TEST};

invoke-local:
	@( \
		if ! npm ls -g serverless; then npm install -g serverless; fi; \
		sls plugin install -n serverless-python-requirements@5.0.0; \
		sls invoke local -f prueba-ing-backend -p tests/event.local.json; \
	)

.PHONY: tests docs
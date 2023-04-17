all: test-watch


test:
	poetry run python -m pytest tests/

test-watch:
	find . -name \*.py | entr poetry run python -m pytest -k tests


build:
	poetry build

coverage:
	poetry run coverage run --source ekumenlabs_config --module pytest tests/
	poetry run coverage xml
	poetry run coverage html
	poetry run coverage report

coverage-watch:
	find . -name \*.py | entr make coverage

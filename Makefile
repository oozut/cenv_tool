SHELL='/bin/bash'

PYTHON_VERSION=`cat .python-version`


.PHONY: docs package env clean tests activate all


# Delete all temporary files like built docs, pycache, etc.
clean:
	rm -rf docs/build ; \
	rm -rf **/__pycache__ ; \
	rm -rf htmlcov; \
	rm -rf .pytest_cache; \
	rm -rf cenv_tool.egg-info; \
	rm -rf dist

# Create the documentation for the project using sphinx.
docs:
	dephell deps install --env=docs --python=$(PYTHON_VERSION); \
	dephell venv run --env=docs sphinx-apidoc -f -o docs cenv_tool; \
	dephell venv run --env=docs sphinx-build -W docs docs/build

# Create / update the projects development environment
env:
	dephell deps install --python=$(PYTHON_VERSION); \
	dephell deps sync --python=$(PYTHON_VERSION)

# Create pip package.
package:
	dephell project build

# Run pytest.
tests:
	dephell deps install --env=pytest --python=$(PYTHON_VERSION); \
	dephell project test --env=pytest; \
	dephell venv run --env=pytest coverage-badge -f -o docs/_static/coverage.svg

all: clean checks tests docs

# Show this help prompt.
help:
	@ echo 'Helpers for development using dephell and poetry.'
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '    make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' $(MAKEFILE_LIST) | column -t -s ':' | sort
	@ echo ''
	@ echo '  Flags:'
	@ echo ''
	@ awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' $(MAKEFILE_LIST) | column -t -s '?=' | sort
	@ echo ''
	@ echo ''
	@ echo '  Note:'
	@ echo '      This workflow requires the following programs / tools to be installed:'
	@ echo '      - conda (miniconda)'
	@ echo '      - cenv'
	@ echo '      - pre-commit'

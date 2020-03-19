.PHONY: build test

PYTHON = python
PIP = pip3


deps:
	$(PIP) install pandas graphviz

install: deps build
	$(PYTHON) setup.py install --record files.txt --user

uninstall:
	cat files.txt | xargs rm -rf

test_deps:
	$(PIP) install pytest

test: build test_deps
	$(PYTHON) -m pytest -x ./tests

build_deps:
	$(PIP) install wheel setuptools twine numpy pandas cython

build: build_deps
	$(PYTHON) setup.py build_ext --inplace

dist: build
	$(PYTHON) setup.py sdist

dist_wheel: build
	$(PYTHON) setup.py bdist_wheel --universal

upload:
	twine check dist/*
	twine upload dist/*  -u $(USERNAME) -p $(PASSWORD)

clean:
	@rm -rf build/ dist/ *.egg-info/

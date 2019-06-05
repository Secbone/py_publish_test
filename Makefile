.PHONY: build test

PYTHON = python3
PIP = pip3


install:
	$(PYTHON) setup.py install --record files.txt

uninstall:
	cat files.txt | xargs rm -rf

test:
	$(PYTHON) -m pytest -x ./tests

build_deps:
	$(PIP) install wheel setuptools twine

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

default: test

test: install
	python -m unittest tests/**/*.py

install: build
	pip install -e ".[tests]"

build: clean src/cyhilbert/cyhilbert.c
	python setup.py sdist bdist_wheel

src/cyhilbert/cyhilbert.c:
	cythonize -3 src/cyhilbert/cyhilbert.pyx

clean:
	rm -rf build dist *.egg-info cyhilbert.*.so src/cyhilbert/cyhilbert.c

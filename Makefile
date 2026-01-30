PYTHON := python3

MAIN := amazing.py

.PHONY: install run debug clean lint lint-strict

install:
	@echo "Installing project dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	@echo "Running the maze project..."
	$(PYTHON) $(MAIN) config.txt

debug:
	@echo "Running the maze project in debug mode..."
	$(PYTHON) -m pdb $(MAIN)

clean:
	@echo "Cleaning temporary files..."
	rm -rf __pycache__ .mypy_cache *.pyc

lint:
	@echo "Running lint checks..."
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@echo "Running strict lint checks..."
	flake8 .
	mypy . --strict

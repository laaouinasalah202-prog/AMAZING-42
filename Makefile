PYTHON := python3

MAIN := a_maze_ing.py

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
	$(PYTHON) -m cleanpy .

lint:
	@echo "Running lint checks..."
	-flake8 .
	-python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

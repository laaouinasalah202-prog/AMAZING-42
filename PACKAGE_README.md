# pyproject.toml Documentation

## What This File Does

This `pyproject.toml` configures your project to build **only the `maze_gen` package** as a reusable library.

## What Gets Built

✅ **Included in package:**
```
maze_gen/
├── __init__.py
├── maze.py
└── algorithms.py
```

❌ **Excluded (stays in repo):**
- `a_maze_ing.py`, `display_maze.py`, `menu.py`, `parssing.py`
- `config.txt`, `Makefile`, `requirements.txt`

## Key Sections Explained

### Package Discovery
```toml
[tool.setuptools.packages.find]
include = ["maze_gen*"]  # Only build maze_gen folder
```

### Dependencies
```toml
dependencies = []  # Library has no runtime dependencies

[project.optional-dependencies]
dev = ["mypy>=1.19.1", "flake8>=7.3.0", "cleanpy>=0.5.1"]
```

## Usage

### For Library Users
```bash
pip install .
```
```python
from maze_gen import MazeGenerator, prims_algo, shortest_path
maze = MazeGenerator(10, 10, (0,0), (9,9), "out.txt", True, None)
```

### For Developers (You)
```bash
# Continue using as normal
make install
make run
python3 a_maze_ing.py config.txt
```

## Building the Package

```bash
pip install build
python -m build
# Creates: dist/maze_gen-0.1.0-py3-none-any.whl
```

## Testing the Build

```bash
# Verify contents
tar -tzf dist/maze_gen-0.1.0.tar.gz

# Test in clean environment
python -m venv test_env
source test_env/bin/activate
pip install dist/maze_gen-0.1.0-py3-none-any.whl
deactivate
```
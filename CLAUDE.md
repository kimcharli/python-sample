# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project called "python_sample" for AI-assisted coding, managed with uv and configured for PyPI publishing. The project follows modern Python packaging standards with comprehensive development tooling.

## Development Commands

### Environment Setup
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install
```

### Development Workflow
```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Format code
uv run ruff format

# Lint code
uv run ruff check src/ tests/

# Type checking
uv run mypy src/

# Run all quality checks
uv run ruff check src/ tests/ && uv run mypy src/ && uv run pytest
```

### Building and Publishing
```bash
# Build package
uv build

# Install package locally for testing
uv pip install -e .

# Publish to PyPI (requires authentication)
uv publish
```

### Adding Dependencies
```bash
# Add runtime dependency
uv add package-name

# Add development dependency
uv add --dev package-name
```

## Project Structure

```
src/
├── python_sample/       # Main package
│   └── __init__.py     # Version and package info
tests/                  # Test files
├── __init__.py
└── test_*.py          # Test modules
docs/                  # Documentation
pyproject.toml         # Project configuration
.pre-commit-config.yaml # Pre-commit hooks
.gitignore            # Git ignore patterns
```

## Code Quality Standards

- **Formatting**: Black (88 char line length)
- **Import sorting**: isort (black-compatible)
- **Linting**: Ruff with comprehensive rule set
- **Type checking**: mypy with strict settings
- **Testing**: pytest with coverage reporting
- **Pre-commit**: Automated quality checks on commit

## Key Configuration

- Python 3.9+ required
- Uses hatchling build backend
- Configured for PyPI publishing
- Comprehensive test coverage expected
- Type hints required for all public APIs
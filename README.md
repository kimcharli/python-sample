# python-sample

A sample Python project demonstrating modern Python development practices with:

- **uv** for fast package management
- **ruff** for linting and formatting
- **pytest** for testing with coverage
- **mypy** for type checking
- **pre-commit** hooks for code quality
- **PyPI** publishing ready

## Quick Start

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Format and lint
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/

# Type check
uv run mypy src/
```
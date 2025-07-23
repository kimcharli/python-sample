# Python Sample

[![CI](https://github.com/kimcharli/python-sample/workflows/CI/badge.svg)](https://github.com/kimcharli/python-sample/actions)
[![Coverage](https://codecov.io/gh/kimcharli/python-sample/branch/main/graph/badge.svg)](https://codecov.io/gh/kimcharli/python-sample)
[![PyPI version](https://badge.fury.io/py/python-sample.svg)](https://badge.fury.io/py/python-sample)
[![Python versions](https://img.shields.io/pypi/pyversions/python-sample.svg)](https://pypi.org/project/python-sample/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern Python package template demonstrating best practices for Python development with:

- **uv** for fast package management
- **ruff** for linting and formatting  
- **pytest** for testing with coverage
- **mypy** for type checking
- **pre-commit** hooks for code quality
- **GitHub Actions** for CI/CD
- **PyPI** publishing ready

## Installation

```bash
pip install python-sample
```

## Usage

```python
import python_sample

print(python_sample.__version__)
# Output: 0.1.0
```

## Development

### Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

```bash
# Clone the repository
git clone https://github.com/kimcharli/python-sample.git
cd python-sample

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install
```

### Development Commands

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Format code
uv run ruff format

# Lint code
uv run ruff check --fix

# Type check
uv run mypy src/

# Run all quality checks
uv run ruff check src/ tests/ && uv run mypy src/ && uv run pytest
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Security

Please see [SECURITY.md](SECURITY.md) for information on reporting security vulnerabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Features

This template includes:

- **Modern Python packaging** with `pyproject.toml`
- **Fast dependency management** with `uv`
- **Code quality tools**: Ruff, Black, isort, mypy
- **Testing**: pytest with coverage reporting
- **Pre-commit hooks** for automated quality checks
- **GitHub Actions** for CI/CD
- **Security scanning** with Bandit
- **Dependency updates** with Dependabot
- **Documentation** templates
- **PyPI publishing** workflow

## Project Structure

```text
python-sample/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── publish.yml
│   └── dependabot.yml
├── src/
│   └── python_sample/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_init.py
├── pyproject.toml
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
└── CLAUDE.md
```
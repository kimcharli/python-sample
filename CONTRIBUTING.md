# Contributing to Python Sample

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) for package management

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kimcharli/python-sample.git
   cd python-sample
   ```

2. **Install uv** (if not already installed)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**
   ```bash
   uv sync --dev
   ```

4. **Install pre-commit hooks**
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

### Code Quality

Before submitting changes, ensure your code passes all quality checks:

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check --fix

# Type check
uv run mypy src/

# Run tests
uv run pytest

# Run all quality checks
uv run ruff check src/ tests/ && uv run mypy src/ && uv run pytest
```

### Testing

- Write tests for new functionality
- Ensure existing tests pass
- Maintain or improve code coverage
- Use descriptive test names

```bash
# Run tests with coverage
uv run pytest --cov

# Run specific tests
uv run pytest tests/test_specific.py

# Run tests with verbose output
uv run pytest -v
```

### Pre-commit Hooks

Pre-commit hooks will automatically run on every commit to ensure code quality:

- Code formatting (Ruff)
- Linting (Ruff)
- Type checking (mypy)
- Security scanning (Bandit)
- YAML/TOML validation

## Submitting Changes

### Pull Request Process

1. **Fork the repository** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for new functionality

4. **Run the full test suite** to ensure nothing is broken

5. **Commit your changes** with a clear commit message
   ```bash
   git commit -m "Add feature: clear description of what you added"
   ```

6. **Push to your fork** and submit a pull request

### Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add user authentication feature

- Implement JWT token authentication
- Add login/logout endpoints
- Include comprehensive tests
- Update documentation

Fixes #123
```

### Pull Request Guidelines

- Keep pull requests focused and atomic
- Include a clear description of the changes
- Reference relevant issues
- Add screenshots for UI changes
- Ensure CI passes

## Code Style

This project follows these style guidelines:

- **Formatting**: Ruff (88 character line length)
- **Import sorting**: Ruff (compatible with Black)
- **Linting**: Ruff with comprehensive rule set
- **Type hints**: Required for all public APIs
- **Docstrings**: Google style for functions and classes

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- Clear steps to reproduce
- Expected vs actual behavior
- Error messages (if any)
- Minimal code example

### Feature Requests

For feature requests, please:

- Explain the use case
- Describe the proposed solution
- Consider alternative solutions
- Be willing to implement the feature

## Security

Please review our [Security Policy](SECURITY.md) for reporting security vulnerabilities.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue with the "question" label if you need help or clarification on anything.
# Contributing to Codemood

Thank you for your interest in contributing to Codemood! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and clone the repository**
```bash
git clone https://github.com/yourusername/codemood.git
cd codemood
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies**
```bash
pip install -e .
pip install pytest flake8 black
```

## Code Style

- Follow PEP 8 guidelines
- Use `black` for code formatting: `black codemood/`
- Use `flake8` for linting: `flake8 codemood --max-line-length=88`
- Add type hints where appropriate

## Testing

- Write tests for new functionality in the `tests/` directory
- Run tests with: `pytest tests/ -v`
- Ensure all tests pass before submitting PR

## Submitting Changes

1. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**
- Write clean, documented code
- Add tests for new functionality
- Update documentation if needed

3. **Test your changes**
```bash
pytest tests/
flake8 codemood
black --check codemood
```

4. **Commit and push**
```bash
git add .
git commit -m "Add: brief description of changes"
git push origin feature/your-feature-name
```

5. **Create a Pull Request**
- Use the PR template
- Provide clear description of changes
- Link related issues

## Areas for Contribution

- **New language support**: Add AST parsing for JavaScript, Java, C++
- **Additional analyzers**: Security patterns, performance metrics
- **Machine learning**: Improve mood classification accuracy
- **Documentation**: Examples, tutorials, API docs
- **Testing**: Edge cases, integration tests

## Questions?

Open an issue for questions or join discussions in existing issues.
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
# Run tests
pytest tests/ -v

# Check code style
flake8 codemood --max-line-length=88 --ignore=E203,W503
black --check codemood

# Run comprehensive analysis example
python examples/advanced_usage.py
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

### High Priority
- **JavaScript/TypeScript AST support**: Extend analysis beyond Python
- **Java bytecode analysis**: Enterprise language support
- **C++ static analysis**: Systems programming support

### Medium Priority
- **Enhanced security patterns**: More vulnerability detection
- **Performance profiling**: Runtime analysis integration
- **Machine learning models**: Custom code-trained sentiment models

### Documentation & Testing
- **API documentation**: Comprehensive examples and tutorials
- **Integration guides**: CI/CD, IDE plugins
- **Edge case testing**: Complex code scenarios

## Questions?

Open an issue for questions or join discussions in existing issues.
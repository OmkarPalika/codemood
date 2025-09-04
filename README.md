# Codemood

[![PyPI version](https://img.shields.io/pypi/v/codemood.svg?color=blue)](https://pypi.org/project/codemood/)
[![PyPI downloads](https://img.shields.io/pypi/dm/codemood.svg?color=green)](https://pypi.org/project/codemood/)
[![License](https://img.shields.io/github/license/OmkarPalika/codemood.svg?color=yellow)](https://github.com/OmkarPalika/codemood/blob/main/LICENSE)
[![Build](https://img.shields.io/github/actions/workflow/status/OmkarPalika/codemood/python-package.yml?branch=main)](https://github.com/OmkarPalika/codemood/actions)

**Advanced code analysis platform that combines AI sentiment analysis with comprehensive code quality assessment.**

Codemood provides multi-dimensional code analysis including mood detection, security vulnerability scanning, performance bottleneck identification, and code quality metrics. Built for developers who want actionable insights into their codebase.

## Key Features

### 🧠 **Multi-Dimensional Mood Analysis**
- **6 distinct code moods**: Elegant, Chaotic, Optimistic, Anxious, Confident, Confused
- **AST-based analysis** for deep code structure understanding
- **Complexity metrics**: Cyclomatic, cognitive complexity, nesting depth

### 🔒 **Security Vulnerability Detection**
- **Pattern-based scanning** for common security issues
- **Severity classification**: Critical, High, Medium, Low
- **Detects**: SQL injection, hardcoded secrets, shell injection, weak randomization

### ⚡ **Performance Analysis**
- **Anti-pattern detection**: Nested loops, inefficient string operations
- **Complexity assessment**: O(n²) detection, linear search identification
- **Actionable recommendations** for optimization

### 📊 **Comprehensive Scoring**
- **Quality Score**: Code maintainability and structure assessment
- **Security Score**: Vulnerability risk evaluation
- **Performance Score**: Efficiency and optimization analysis
- **Overall Score**: Weighted combination of all metrics

## Installation

```bash
pip install codemood
```

## Quick Start

### Basic Sentiment Analysis
```python
from codemood import analyze_code

result = analyze_code("for i in range(10): print(i)")
print(f"Mood: {result['label']}, Score: {result['score']:.2f}")
# Output: Mood: POSITIVE, Score: 0.98
```

### Comprehensive Analysis
```python
from codemood import analyze_comprehensive

code = '''
def process_data(items):
    password = "admin123"  # Security issue
    result = ""
    for i in range(len(items)):
        for j in range(len(items)):  # Performance issue
            result += str(items[i] + items[j])
    return result
'''

analysis = analyze_comprehensive(code)
print(f"Mood: {analysis.mood_analysis.primary_mood.value}")
print(f"Overall Score: {analysis.overall_score:.2f}")
print(f"Security Issues: {len(analysis.security_issues)}")
print(f"Performance Issues: {len(analysis.performance_issues)}")
print(f"Summary: {analysis.summary}")
```

## Advanced Usage

### Individual Analyzers
```python
from codemood import (
    AdvancedCodeAnalyzer,
    SecurityAnalyzer,
    PerformanceAnalyzer
)

# Specialized analysis
security = SecurityAnalyzer()
issues = security.analyze(code)

performance = PerformanceAnalyzer()
bottlenecks = performance.analyze(code)

advanced = AdvancedCodeAnalyzer()
mood_result = advanced.analyze(code)
```

### Custom Model Configuration
```python
from codemood import CodeMoodAnalyzer

# Use custom Hugging Face model
analyzer = CodeMoodAnalyzer(model="your-custom-model")
result = analyzer.analyze(code)
```

## Configuration

### Hugging Face Integration
Codemood works offline by default. For cloud inference:

```bash
export HF_TOKEN="your_hugging_face_token"
```

### Language Support
- **Python**: Full AST analysis with comprehensive metrics
- **Other languages**: Pattern-based analysis with generic scoring

## API Reference

### Core Functions
- `analyze_code(snippet, model)` - Basic sentiment analysis
- `analyze_comprehensive(snippet, language)` - Full analysis suite
- `reset_analyzers()` - Clear cached models

### Analysis Results
```python
@dataclass
class ComprehensiveAnalysis:
    mood_analysis: AdvancedMoodResult
    security_issues: List[SecurityIssue]
    performance_issues: List[PerformanceIssue]
    security_score: float
    performance_score: float
    overall_score: float
    sentiment: Dict[str, Any]
    summary: str
```

## Use Cases

- **Code Reviews**: Automated quality assessment and issue detection
- **CI/CD Integration**: Quality gates and security scanning
- **Developer Education**: Learning code quality principles
- **Technical Debt Analysis**: Identifying areas for refactoring
- **Security Audits**: Vulnerability detection and risk assessment

## Contributing

Contributions welcome! Please read our contributing guidelines and submit pull requests for improvements.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Roadmap

### v0.3.0 - Language Expansion
- [ ] JavaScript/TypeScript AST support
- [ ] Java bytecode analysis
- [ ] Go static analysis

### v0.4.0 - Advanced Features
- [ ] Machine learning-based quality prediction
- [ ] Real-time code analysis
- [ ] Custom rule definitions

### v1.0.0 - Production Ready
- [ ] IDE plugins (VS Code, IntelliJ)
- [ ] Team analytics dashboard
- [ ] Enterprise integrations
- [ ] Performance benchmarking
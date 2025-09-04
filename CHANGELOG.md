# Changelog

## [0.2.0] - 2025-09-04

### Added
- **Multi-dimensional mood analysis** with 6 distinct code moods (Elegant, Chaotic, Optimistic, Anxious, Confident, Confused)
- **AST-based code analysis** for Python with structural understanding
- **Security vulnerability detection** with pattern matching for common issues
- **Performance analysis** identifying bottlenecks and anti-patterns
- **Comprehensive scoring system** combining quality, security, and performance metrics
- **Unified analysis API** with `analyze_comprehensive()` function
- **Individual specialized analyzers** (AdvancedCodeAnalyzer, SecurityAnalyzer, PerformanceAnalyzer)
- **Complexity metrics** including cyclomatic and cognitive complexity
- **Code smell detection** for maintainability assessment
- **Professional data structures** with type safety and JSON serialization

### Enhanced
- **Improved explanations** with context-aware reasoning
- **Better error handling** and graceful fallbacks
- **Extended test coverage** with comprehensive test suite
- **Professional documentation** with clear API reference

### Technical
- Added AST parsing for Python code structure analysis
- Implemented weighted scoring algorithms
- Created extensible architecture for new analyzers
- Added dataclass-based result structures

## [0.1.1] - Previous Release

### Features
- Basic sentiment analysis using Hugging Face transformers
- Simple positive/negative mood detection
- Funny explanations for code sentiment
- Offline and cloud inference support
- Lightweight pip installation
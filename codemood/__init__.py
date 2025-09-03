"""
codemood
========
A fun Code Mood Analyzer that assigns 'moods' to code snippets using AI.

Example
-------
>>> from codemood import analyze_code, CodeMoodAnalyzer
>>> mood = analyze_code("for i in range(10): print(i)")
>>> print(mood)
{'label': 'POSITIVE', 'score': 0.98, 'reason': "Model got happy because it saw 'print'"}
"""

from typing import Optional
from .code_mood_analyzer import CodeMoodAnalyzer

# Internal singleton instance (lazy init)
_analyzer: Optional[CodeMoodAnalyzer] = None


def _get_analyzer() -> CodeMoodAnalyzer:
    """Return the singleton CodeMoodAnalyzer, initializing if needed."""
    global _analyzer
    if _analyzer is None:
        _analyzer = CodeMoodAnalyzer()
    return _analyzer


def analyze_code(snippet: str) -> dict:
    """
    Analyze the mood of a code snippet quickly.

    Parameters
    ----------
    snippet : str
        The code snippet to analyze.

    Returns
    -------
    dict
        Dictionary containing:
        - label: "POSITIVE" or "NEGATIVE"
        - score: confidence score (float)
        - reason: funny reason for the sentiment
    """
    analyzer = _get_analyzer()
    return analyzer.explain_sentiment(snippet)


# Public API
__all__ = [
    "CodeMoodAnalyzer",
    "analyze_code",
]

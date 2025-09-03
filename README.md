# CodeMood 😎💻

A fun package that tells you the *mood* of your code snippets.  
Uses AI (Hugging Face + Transformers) to give a sentiment label with funny explanations.  

## Installation
```bash
pip install codemood
```

## Usage
```python
from codemood import CodeMoodAnalyzer

analyzer = CodeMoodAnalyzer()
result = analyzer.analyze("for i in range(10): print(i)")
print(result)
```

## Features
- Sentiment analysis of code (positive/negative/neutral)
- Funny reasoning (like why your loop looks "sad")
- Fallback system (local model → Hugging Face API → safe neutral result)
- Ready for extensions like code optimization scoring

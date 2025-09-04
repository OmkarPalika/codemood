from typing import Dict, Any, List
from dataclasses import dataclass, asdict
from .advanced_analyzer import AdvancedCodeAnalyzer, AdvancedMoodResult
from .security_analyzer import SecurityAnalyzer, SecurityIssue
from .performance_analyzer import PerformanceAnalyzer, PerformanceIssue
from .code_mood_analyzer import CodeMoodAnalyzer


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


class UnifiedCodeAnalyzer:
    def __init__(self):
        self.advanced_analyzer = AdvancedCodeAnalyzer()
        self.security_analyzer = SecurityAnalyzer()
        self.performance_analyzer = PerformanceAnalyzer()
        self.sentiment_analyzer = CodeMoodAnalyzer()

    def analyze_comprehensive(self, code: str, language: str = "python") -> ComprehensiveAnalysis:
        # Advanced mood analysis
        mood_result = self.advanced_analyzer.analyze(code, language)
        
        # Security analysis
        security_issues = self.security_analyzer.analyze(code)
        security_score = self.security_analyzer.get_security_score(security_issues)
        
        # Performance analysis
        performance_issues = self.performance_analyzer.analyze(code)
        performance_score = self.performance_analyzer.get_performance_score(performance_issues)
        
        # Original sentiment analysis
        sentiment = self.sentiment_analyzer.analyze(code)
        
        # Calculate overall score
        overall_score = (
            mood_result.quality_score * 0.4 +
            security_score / 100 * 0.35 +
            performance_score / 100 * 0.25
        )
        
        # Generate summary
        summary = self._generate_summary(mood_result, security_issues, performance_issues, overall_score)
        
        return ComprehensiveAnalysis(
            mood_analysis=mood_result,
            security_issues=security_issues,
            performance_issues=performance_issues,
            security_score=security_score,
            performance_score=performance_score,
            overall_score=overall_score,
            sentiment=sentiment,
            summary=summary
        )

    def _generate_summary(self, mood: AdvancedMoodResult, security: List, performance: List, score: float) -> str:
        if score > 0.8:
            return f"Excellent code! {mood.primary_mood.value.title()} vibes with minimal issues"
        elif score > 0.6:
            return f"Good code with {mood.primary_mood.value} mood, but {len(security + performance)} issues to address"
        elif score > 0.4:
            return f"Code needs attention - {len(security)} security & {len(performance)} performance issues"
        else:
            return f"Code requires significant improvement - multiple critical issues detected"

    def to_dict(self, analysis: ComprehensiveAnalysis) -> Dict[str, Any]:
        result = asdict(analysis)
        # Convert enums to strings for JSON serialization
        result['mood_analysis']['primary_mood'] = analysis.mood_analysis.primary_mood.value
        return result
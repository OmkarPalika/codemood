#!/usr/bin/env python3
"""
Comprehensive Analysis Demo
Demonstrates all codemood features including sentiment, security, and performance.
"""

from codemood import analyze_sentiment_advanced, analyze_comprehensive, get_optimization_suggestions

# Test code with optimization opportunities
test_code = '''
def process_data(items):
    result = []
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j]:
                result.append(items[i])
    return result

# String concatenation issue
output = ""
for item in ["a", "b", "c"]:
    output += item
'''

print("=== SENTIMENT ANALYSIS ===")
sentiment_result = analyze_sentiment_advanced(test_code)
print(f"Score: {sentiment_result.overall_score:.2f}")
print(f"Tone: {sentiment_result.emotional_tone}")
print(f"Confidence: {sentiment_result.confidence:.2f}")
print("Reasoning:")
for reason in sentiment_result.reasoning[:3]:
    print(f"  • {reason}")

print("\n=== COMPREHENSIVE ANALYSIS ===")
comp_result = analyze_comprehensive(test_code)
print(f"Overall Score: {comp_result.overall_score:.2f}")
print(f"Security Score: {comp_result.security_score:.1f}/100")
print(f"Performance Score: {comp_result.performance_score:.1f}/100")
print(f"Security Issues: {len(comp_result.security_issues)}")
print(f"Performance Issues: {len(comp_result.performance_issues)}")

print("\n=== OPTIMIZATION SUGGESTIONS ===")
optimizations = get_optimization_suggestions(test_code)
for opt in optimizations:
    print(f"Issue: {opt.issue_type}")
    print(f"  Fix: {opt.suggested_fix}")
    print(f"  Impact: {opt.impact}")

print("\n=== SUMMARY ===")
print(f"Summary: {comp_result.summary}")

print("\n=== CLI COMMANDS TO TRY ===")
print("codemood --analyze examples/ai_enhanced_demo.py")
print("codemood --version")
print("codemood --check")
print("codemood --info")
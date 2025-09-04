from codemood import analyze_code, analyze_comprehensive

# Test basic functionality
print("=== Basic Test ===")
basic = analyze_code("print('hello world')")
print(f"Label: {basic['label']}, Score: {basic['score']:.2f}")

# Test comprehensive analysis
print("\n=== Comprehensive Test ===")
code = '''
def vulnerable_func():
    password = "admin123"
    for i in range(10):
        for j in range(10):
            print(i * j)
'''

result = analyze_comprehensive(code)
print(f"Mood: {result.mood_analysis.primary_mood.value}")
print(f"Overall Score: {result.overall_score:.2f}")
print(f"Security Issues: {len(result.security_issues)}")
print(f"Performance Issues: {len(result.performance_issues)}")
print(f"Summary: {result.summary}")
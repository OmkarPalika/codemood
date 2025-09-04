#!/usr/bin/env python3
"""
Advanced Codemood Usage Examples
Demonstrates comprehensive analysis including security and performance.
"""

from codemood import analyze_comprehensive, SecurityAnalyzer, PerformanceAnalyzer

# Example 1: Security Issues
vulnerable_code = '''
import os
password = "admin123"  # Hardcoded password
user_input = input("Enter command: ")
os.system(user_input)  # Shell injection risk

# SQL injection vulnerability
query = f"SELECT * FROM users WHERE name = '{user_input}'"
'''

print("=== COMPREHENSIVE SECURITY ANALYSIS ===")
result = analyze_comprehensive(vulnerable_code)
print(f"Overall Score: {result.overall_score:.2f}")
print(f"Security Score: {result.security_score:.1f}/100")
print(f"Security Issues Found: {len(result.security_issues)}")
for issue in result.security_issues:
    print(f"  - {issue.severity}: {issue.description}")

# Example 2: Performance Issues
slow_code = '''
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):  # Nested loops O(n²)
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates

# String concatenation in loop
result = ""
for i in range(1000):
    result += str(i)  # Inefficient

# Linear search
def search_item(target, items):
    for item in items:
        if item == target:
            return True
    return False
'''

print("\n=== COMPREHENSIVE PERFORMANCE ANALYSIS ===")
result = analyze_comprehensive(slow_code)
print(f"Overall Score: {result.overall_score:.2f}")
print(f"Performance Score: {result.performance_score:.1f}/100")
print(f"Performance Issues Found: {len(result.performance_issues)}")
for issue in result.performance_issues:
    print(f"  - {issue.type}: {issue.description}")

# Example 3: Individual Analyzers
print("\n=== INDIVIDUAL ANALYZER USAGE ===")

# Security analyzer
security = SecurityAnalyzer()
sec_issues = security.analyze(vulnerable_code)
print(f"Security Issues: {len(sec_issues)}")

# Performance analyzer
performance = PerformanceAnalyzer()
perf_issues = performance.analyze(slow_code)
print(f"Performance Issues: {len(perf_issues)}")

# Example 4: High Quality Code
elegant_code = '''
def fibonacci_generator(n: int):
    """Generate fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Efficient set operations
def find_duplicates_efficient(items):
    """Find duplicates using set operations - O(n)."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Proper string handling
def join_strings(items):
    """Efficient string joining."""
    return ''.join(str(item) for item in items)
'''

print("\n=== HIGH QUALITY CODE ANALYSIS ===")
result = analyze_comprehensive(elegant_code)
print(f"Overall Score: {result.overall_score:.2f}")
print(f"Security Score: {result.security_score:.1f}/100")
print(f"Performance Score: {result.performance_score:.1f}/100")
print(f"Summary: {result.summary}")

print("\n=== CLI USAGE EXAMPLES ===")
print("Save code to a file and analyze:")
print("  codemood --analyze my_code.py")
print("  codemood --check  # Check for updates")
print("  codemood --info   # Package information")
#!/usr/bin/env python3
"""
CLI Demo - Example code for testing codemood CLI commands
"""

from typing import List, Any

def fibonacci_generator(n: int):
    """Generate fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Some problematic code for analysis
def find_duplicates(items: List[Any]) -> List[Any]:
    duplicates: List[Any] = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):  # O(n²) nested loops
            if items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates

# String concatenation issue
result = ""
for i in range(100):
    result += str(i)  # Inefficient string building

# Security issue
password = "admin123"  # Hardcoded password

# Good practices
with open(__file__, 'r') as f:
    content = f.read()

# Type hints and documentation
def process_data(items: List[str]) -> List[str]:
    """Process a list of items efficiently."""
    return [item.strip().lower() for item in items if item]

if __name__ == "__main__":
    print("CLI Demo File")
    print("Test with: codemood --analyze examples/cli_demo.py")
    
    # Generate some fibonacci numbers
    fib_gen = fibonacci_generator(10)
    fib_numbers = list(fib_gen)
    print(f"Fibonacci: {fib_numbers}")
    
    # Test duplicate finding (inefficient)
    test_items = [1, 2, 3, 2, 4, 3, 5]
    dupes = find_duplicates(test_items)
    print(f"Duplicates: {dupes}")

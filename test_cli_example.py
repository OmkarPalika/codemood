#!/usr/bin/env python3
"""
Test CLI functionality locally.
"""

def fibonacci_generator(n: int):
    """Generate fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test the CLI with: python -m codemood.cli --analyze test_cli_example.py
#!/usr/bin/env python3
"""Simple version bumping script for codemood."""

import re
import sys

def bump_version(bump_type: str = "patch"):
    """Bump version in pyproject.toml"""
    with open("pyproject.toml", "r") as f:
        content = f.read()
    
    # Find current version
    match = re.search(r'version = "(\d+)\.(\d+)\.(\d+)"', content)
    if not match:
        print("Version not found in pyproject.toml")
        return
    
    major, minor, patch = map(int, match.groups())
    
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    else:  # patch
        patch += 1
    
    new_version = f"{major}.{minor}.{patch}"
    new_content = re.sub(r'version = "\d+\.\d+\.\d+"', f'version = "{new_version}"', content)
    
    with open("pyproject.toml", "w") as f:
        f.write(new_content)
    
    print(f"Version bumped to {new_version}")
    return new_version

if __name__ == "__main__":
    bump_type = sys.argv[1] if len(sys.argv) > 1 else "patch"
    bump_version(bump_type)
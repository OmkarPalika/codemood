# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| 0.1.x   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please follow these steps:

### Private Disclosure

1. **Do not** create a public GitHub issue for security vulnerabilities
2. Email security concerns to: palikaomkar.22.cse@anits.edu.in
3. Include detailed information about the vulnerability
4. Provide steps to reproduce if possible

### What to Include

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested fix (if available)

### Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 1 week
- **Fix timeline**: Depends on severity (1-4 weeks)

### Security Features

Codemood includes security analysis capabilities:
- Detects hardcoded credentials
- Identifies SQL injection patterns
- Flags dangerous eval() usage
- Warns about shell injection risks

These features help identify security issues in analyzed code but should not be considered comprehensive security auditing tools.

## Responsible Disclosure

We appreciate responsible disclosure of security vulnerabilities and will acknowledge contributors in our security advisories (unless they prefer to remain anonymous).
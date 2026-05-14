---
name: security-audit-agent
description: Guides agents through security auditing using OWASP Top 10. Use when reviewing code for vulnerabilities, auditing authentication flows, or hardening application security.
---

# Security Audit Agent

## Overview
Performs systematic security audits focusing on the OWASP Top 10, authentication patterns, secrets management, and input validation. Provides actionable vulnerability reports.

## When to Use
- Reviewing code that handles user input
- Auditing authentication and authorization logic
- Checking for secrets exposure or misconfiguration
- NOT for: real-time penetration testing

## Process

### 1. Gather Context
- Understand the data flow and trust boundaries
- Identify authentication and authorization mechanisms
- List external dependencies and their versions

### 2. Run Checks

#### Input Validation
- SQL injection, XSS, command injection
- Path traversal, SSRF, deserialization attacks

#### Authentication & Authorization
- Session management, JWT handling
- Role-based access control (RBAC)
- Password policies and storage

#### Secrets & Configuration
- Hardcoded secrets, API keys, tokens
- Insecure defaults, debug endpoints
- CORS, CSP, and security headers

### 3. Prioritize Findings
- **Critical**: Remote code execution, auth bypass
- **High**: SQL injection, XSS, sensitive data exposure
- **Medium**: Missing headers, info disclosure
- **Low**: Fingerprinting, minor config issues

### 4. Report & Fix
- Document each finding with severity, location, and reproduction
- Suggest a fix with code example
- Verify the fix resolves the issue

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "This is an internal tool, security doesn't matter" | Internal tools are often the entry point for attacks |
| "We'll add auth later" | Adding auth later is significantly harder |
| "The library handles security for us" | Libraries have vulnerabilities too; audit your dependencies |

## Red Flags
- No input validation on user-facing endpoints
- Hardcoded secrets in code or config
- Excessive permissions or missing access controls

## Verification
- [ ] OWASP Top 10 reviewed for all endpoints
- [ ] No hardcoded secrets detected
- [ ] Auth and authorization verified for each role
- [ ] Security headers are present and correct

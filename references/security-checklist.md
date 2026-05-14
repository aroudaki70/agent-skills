# Security Checklist

## Pre-Commit
- [ ] No hardcoded secrets, API keys, or tokens
- [ ] Input validation on all user-facing endpoints
- [ ] Parameterized queries (no raw SQL concatenation)
- [ ] CSRF tokens on state-changing requests

## Auth
- [ ] Password hashing (bcrypt/argon2)
- [ ] JWT with short expiry and secure signing
- [ ] Rate limiting on login endpoints

## Headers
- [ ] Content-Security-Policy
- [ ] X-Content-Type-Options: nosniff
- [ ] Strict-Transport-Security
- [ ] X-Frame-Options: DENY

## CORS
- [ ] Origin whitelist, not wildcard
- [ ] Credentials only when needed
- [ ] Methods restricted to required set

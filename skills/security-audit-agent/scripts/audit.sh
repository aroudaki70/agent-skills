#!/bin/bash
set -e

echo "Running security audit..." >&2

# Check for common vulnerability patterns
echo "Checking dependencies..." >&2
if [ -f "package.json" ]; then
  npm audit 2>&1 || true
elif [ -f "requirements.txt" ]; then
  pip audit 2>&1 || true
elif [ -f "Cargo.lock" ]; then
  cargo audit 2>&1 || true
fi

# Check for secrets in code
echo "Checking for hardcoded secrets..." >&2
grep -rn --include="*.py" --include="*.js" --include="*.ts" --include="*.java" \
  -E '(api[_-]?key|secret|password|token|credential)\s*[:=]\s*["'"'"']' . 2>/dev/null || \
  echo "No obvious hardcoded secrets found."

echo "Security audit complete." >&2

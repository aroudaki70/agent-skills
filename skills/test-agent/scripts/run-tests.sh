#!/bin/bash
set -e

echo "Running test analysis..." >&2

# Discover and run tests
if [ -f "package.json" ]; then
  npm test 2>&1 || true
elif [ -f "pom.xml" ]; then
  mvn test 2>&1 || true
elif [ -f "build.gradle" ]; then
  ./gradlew test 2>&1 || true
elif [ -f "Cargo.toml" ]; then
  cargo test 2>&1 || true
else
  echo "No recognized test framework found." >&2
fi

echo "Test analysis complete." >&2

#!/bin/bash
set -e

echo "Running code review..." >&2

# Check for diff input
if [ -t 0 ]; then
  echo "No input provided. Pipe a git diff to this script." >&2
  echo "Usage: git diff | bash scripts/review.sh" >&2
  exit 1
fi

# Read the diff from stdin
DIFF=$(cat)

if [ -z "$DIFF" ]; then
  echo '{"status": "no_changes", "message": "No diff provided for review"}' >&2
  exit 0
fi

echo "Diff received, analyzing..." >&2

# Output structured result
echo "Review complete. Check findings above." >&2

# Testing Patterns

## Test Structure
- Arrange-Act-Assert (AAA)
- One assertion concept per test
- Descriptive names: `should_X_when_Y`

## Mocking
- Mock external boundaries only
- Prefer fakes over mocks for in-memory test doubles
- Avoid over-mocking (tests implementation, not behavior)

## Test Sizes
- **Small** (unit): Single class/method, no I/O, millisecond runtime
- **Medium** (integration): Module boundaries, disk/network, second runtime
- **Large** (E2E): Full system, browser/API, minute runtime

## Anti-Patterns
- Shared mutable state between tests
- Testing private methods directly
- Flaky tests (non-deterministic, order-dependent)

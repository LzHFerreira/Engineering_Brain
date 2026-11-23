# Testing

This policy applies to every language. `scripts/verify fast|pr|deep` dispatches to native tools and fails closed when no gate applies. CI runs it independently on the exact candidate revision; agent-reported results are not evidence.

## Constitution

1. A behavioral change requires independently established expected behavior and regression evidence.
2. Every change passes its applicable static, behavioral, contract, and architecture checks.
3. Risk-specific obligations are additive; the implementing agent cannot waive them.
4. Changes to critical tests or verification policy require separate authorization.
5. Missing evidence blocks acceptance.
6. Verification runs independently against the exact candidate revision.
7. The actual diff is checked against authorized scope.
8. Passing tests show observed compliance with tested properties, never universal correctness.

## Gate states

Each required gate is `PASS`, `FAIL`, `UNAVAILABLE`, or `NOT_APPLICABLE` with a policy-permitted reason. Only `PASS` and justified `NOT_APPLICABLE` are mergeable. No gate is silently skipped.

## Stages

- `fast`: focused tests, build, lint, and types during implementation.
- `pr`: all baseline and risk-triggered gates, integration, architecture, and scope. Required to merge.
- `deep`: full regression, fuzzing, mutation, and concurrency stress. Required for high-risk changes and release.

## Tools

- C: strict Clang/GCC warnings, clang-format, clang-tidy, Clang Static Analyzer, ASan+UBSan, TSan for concurrent code, libFuzzer for untrusted input, CTest with Ninja.
- Python: uv, Ruff, mypy `--strict`, Pyright, pytest `--strict-markers -o strict_xfail=true`, Hypothesis, Import Linter, mutmut, pip-audit.

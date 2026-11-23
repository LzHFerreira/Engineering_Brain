# kv contract

- `parse(text) -> (key, value)` splits at the first `=`. No side effects or dependencies.
- Fails with `ValueError` when `=` is missing or the key is empty.
- Invariant: `parse(f"{k}={v}") == (k, v)` for every non-empty key without `=`.
- Verification: Ruff, mypy `--strict`, Pyright, pytest with Hypothesis. Architecture: `NOT_APPLICABLE` (no dependencies).

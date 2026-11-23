# kvc contract

- `kv_key_len(text)` returns the length of the key before the first `=`, or `-1` if `=` is missing or the key is empty.
- Requires a non-NULL, NUL-terminated `text`. No allocation, side effects, or dependencies.
- Verification: strict warnings, clang-format, clang-tidy with Clang Static Analyzer checks, CTest, ASan+UBSan. Concurrency and fuzzing: `NOT_APPLICABLE` (pure, no untrusted input yet).

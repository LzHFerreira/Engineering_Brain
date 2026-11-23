"""Parse `key=value` pairs."""


def parse(text: str) -> tuple[str, str]:
    """Split text at the first `=`; reject a missing `=` or an empty key."""
    key, sep, value = text.partition("=")
    if not sep or not key:
        raise ValueError(f"invalid pair: {text!r}")
    return key, value

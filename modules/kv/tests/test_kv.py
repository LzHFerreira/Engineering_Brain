import pytest
from hypothesis import given
from hypothesis import strategies as st
from kv import parse

keys = st.text(min_size=1).filter(lambda k: "=" not in k)


@given(keys, st.text())
def test_round_trip(key: str, value: str) -> None:
    assert parse(f"{key}={value}") == (key, value)


@pytest.mark.parametrize("text", ["", "novalue", "=value"])
def test_rejects_invalid(text: str) -> None:
    with pytest.raises(ValueError):
        parse(text)

from typing import TypeVarTuple
from typedre import Pattern
import pytest

Ts = TypeVarTuple("Ts")


def assert_pattern(pattern: Pattern[*Ts], s: str, n: int):
    assert pattern._pat.pattern == s
    assert len(pattern._conv) == n


def assert_match(r: Pattern[*Ts], s: str, *expected: *Ts):
    m = r.fullmatch(s)
    assert m is not None
    assert m.groups() == expected


def assert_nomatch(r: Pattern[*Ts], s: str):
    m = r.fullmatch(s)
    assert m is None


def assert_invalid(r: Pattern[*Ts], s: str):
    with pytest.raises(ValueError):
        r.match(s)

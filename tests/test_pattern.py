from tests.assertions import assert_match, assert_nomatch
from typedre import Pattern, c
import pytest


def test_groups():
    with pytest.raises(RuntimeError):
        Pattern("no groups", c(str))
    with pytest.raises(RuntimeError):
        Pattern("(too)(many)(groups)", c(str))
    Pattern("just(enough)groups", c(str))


def test_nogroups():
    pat = Pattern(r"hello")
    assert_match(pat, "hello")
    assert_nomatch(pat, "goodbye")


def test_hello_person():
    pat = Pattern(r"hello, (\w+)", c(str))
    assert_match(pat, "hello, Dominic", "Dominic")
    assert_match(pat, "hello, Peter", "Peter")
    assert_nomatch(pat, "Hello, Dominic")
    assert_nomatch(pat, "Hello, 1")


def test_rgb():
    pat = Pattern(
        r"rgb\((\d+),(\d+),(\d+)\)",
        c(int, int, int),
    )
    assert_match(pat, "rgb(50,120,47)", 50, 120, 47)


def test_huge():
    pat = Pattern(
        r"(1)(2)(a)(3.0)(b)(c)(4)(5)(d)(e)",
        c(int, int, str, float, str, str, int, int, str, str),
    )
    assert_match(
        pat,
        "12a3.0bc45de",
        1,
        2,
        "a",
        3.0,
        "b",
        "c",
        4,
        5,
        "d",
        "e",
    )

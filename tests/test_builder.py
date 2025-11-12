from tests.assertions import (
    assert_invalid,
    assert_match,
    assert_pattern,
    assert_nomatch,
)
from typedre import new


def test_build_literal():
    pat = new().lit("no").lit("groups").compile()
    assert_pattern(pat, "nogroups", 0)

    pat = new("a").lit("b").lit("c").lit("d").compile()
    assert_pattern(pat, "abcd", 0)


def test_build_capturing():
    pat = new().str("asdf").lit(r"\+").int(r"\d+").compile()
    assert_pattern(pat, r"(asdf)\+(\d+)", 2)


def test_str():
    pat = new().str("g..d").compile()
    assert_match(pat, "good", "good")
    assert_nomatch(pat, "hood")


def test_int():
    pat = new().int("12.4").compile()
    assert_match(pat, "1234", 1234)
    assert_nomatch(pat, "2234")
    assert_invalid(pat, "12m4")


def test_val():
    pat = new().val(r".\.23", float).compile()
    assert_match(pat, "1.23", 1.23)
    assert_nomatch(pat, "1.34")
    assert_invalid(pat, "m.23")


def test_float():
    pat = new().float(True).compile()
    assert_match(pat, "3.2E1", 3.2e1)
    assert_match(pat, "1.23", 1.23)
    assert_nomatch(pat, "j1")
    pat = new().float(False).compile()
    assert_nomatch(pat, "3.2E1")
    assert_match(pat, "1.23", 1.23)
    assert_nomatch(pat, "j1")


def test_dec():
    pat = new().dec(True).compile()
    assert_match(pat, "5", 5)
    assert_match(pat, "+3", 3)
    assert_match(pat, "-9", -9)
    assert_nomatch(pat, "a")
    pat = new().dec(False).compile()
    assert_match(pat, "5", 5)
    assert_nomatch(pat, "+3")
    assert_nomatch(pat, "-9")
    assert_nomatch(pat, "a")


def test_hex():
    pat = new().hex().compile()
    assert_match(pat, "16", 0x16)
    assert_match(pat, "4a", 0x4A)
    assert_match(pat, "12345", 0x12345)
    assert_nomatch(pat, "4g")
    pat = new().hex(6).compile()
    assert_match(pat, "4a4a4a", 0x4A4A4A)
    assert_nomatch(pat, "4a4a4")
    assert_nomatch(pat, "4a4a4a4")


def test_alpha():
    pat = new().alpha().compile()
    assert_match(pat, "abcDEF", "abcDEF")
    assert_nomatch(pat, "2bc")
    pat = new().alpha(3).compile()
    assert_match(pat, "AbC", "AbC")
    assert_nomatch(pat, "AbCd")


def test_alphanum():
    pat = new().alphanum().compile()
    assert_match(pat, "abcDEF", "abcDEF")
    assert_match(pat, "2bc", "2bc")
    assert_nomatch(pat, "hi!!")
    pat = new().alphanum(3).compile()
    assert_match(pat, "A2C", "A2C")
    assert_nomatch(pat, "AbCd")


def test_ws():
    pat = new().ws(True).compile()
    assert_match(pat, " ")
    assert_match(pat, "  \t ")
    assert_nomatch(pat, "")
    assert_nomatch(pat, "a")
    pat = new().ws(False).compile()
    assert_match(pat, "  ")
    assert_match(pat, "")
    assert_nomatch(pat, "a")


def test_bool():
    pat = new().bool().compile()
    assert_match(pat, "true", True)
    assert_match(pat, "1", True)
    assert_match(pat, "f", False)
    assert_match(pat, "off", False)
    assert_nomatch(pat, "asdf")
    pat = new().bool(["ack"], ["nack"]).compile()
    assert_match(pat, "ack", True)
    assert_match(pat, "nack", False)
    assert_nomatch(pat, "true")
    assert_nomatch(pat, "0")

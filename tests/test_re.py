from typedre import match, fullmatch, search, finditer


def test_match():
    m = match(
        r"(hello|hi), (\w+)! You're (\d+) years old.",
        "hi, dom! You're 12 years old. Let's just ignore the rest of this sentence",
        (str, str, int),
    )
    assert m is not None
    assert m[0] == "hi, dom! You're 12 years old."
    assert m[1] == "hi"
    assert m[2] == "dom"
    assert m[3] == 12


def test_fullmatch():
    m = fullmatch(
        r"(hello|hi), (\w+)! You're (\d+) years old.",
        "hi, dom! You're 12 years old. Let's just ignore the rest of this sentence",
        (str, str, int),
    )
    assert m is None

    m = fullmatch(
        r"(hello|hi), (\w+)! You're (\d+) years old.",
        "hi, dom! You're 12 years old.",
        (str, str, int),
    )
    assert m is not None
    assert m[0] == "hi, dom! You're 12 years old."
    assert m[1] == "hi"
    assert m[2] == "dom"
    assert m[3] == 12


def test_search():
    m = search(r"(3.141\d+)", "the value of pi is 3.141592653...", (float,))
    assert m is not None
    assert m[0] == "3.141592653"
    assert m[1] == 3.141592653


def test_finditer():
    ms = list(finditer(r"([A-Z])(\d)", "A3 B8 G1", (str, int)))
    assert len(ms)
    assert ms[0][0] == "A3"
    assert ms[0][1] == "A"
    assert ms[0][2] == 3

    assert ms[1][0] == "B8"
    assert ms[1][1] == "B"
    assert ms[1][2] == 8

    assert ms[2][0] == "G1"
    assert ms[2][1] == "G"
    assert ms[2][2] == 1

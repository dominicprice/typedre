from typing import TYPE_CHECKING, Any, Callable, Generator

if TYPE_CHECKING:
    import re

from typedre.builder import PatternBuilder as _PatternBuilder
from typedre.match import Match as Match
from typedre.pattern import Pattern as Pattern

__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__author__ = "Dominic Price"


def new(prefix: str = "") -> _PatternBuilder[()]:
    "returns a new pattern builder with the given non-capturing prefix"
    return _PatternBuilder(prefix)


def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], Any], ...],
    flags: "re._FlagsType" = 0,
) -> Match | None:
    """
    If zero or more characters at the beginning of string match the
    regular expression pattern, return a corresponding Match. Return
    None if the string does not match the pattern
    """
    return Pattern(pattern, converters, flags=flags).match(string)  # type: ignore


def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], Any], ...],
    flags: "re._FlagsType" = 0,
) -> Match | None:
    """
    If the whole string matches the regular expression pattern, return
    a corresponding Match. Return None if the string does not match
    the pattern
    """
    return Pattern(pattern, converters, flags=flags).fullmatch(string)  # type: ignore


def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], Any], ...],
    flags: "re._FlagsType" = 0,
) -> Match | None:
    """
    Scan through string looking for the first location where the
    regular expression pattern produces a match, and return a
    corresponding Match. Return None if no position in the string
    matches the pattern
    """
    return Pattern(pattern, converters, flags=flags).search(string)  # type: ignore


def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], Any], ...],
    flags: "re._FlagsType" = 0,
) -> Generator[Match, None, None]:
    """Return an iterator yielding Match objects over all
    non-overlapping matches for the RE pattern in string. The string
    is scanned left-to-right, and matches are returned in the order
    found. Empty matches are included in the result.
    """
    yield from Pattern(pattern, converters, flags=flags).finditer(string)  # type: ignore

from re import ASCII as ASCII
from re import DEBUG as DEBUG
from re import DOTALL as DOTALL
from re import IGNORECASE as IGNORECASE
from re import LOCALE as LOCALE
from re import MULTILINE as MULTILINE
from re import VERBOSE as VERBOSE
from re import A as A
from re import I as I
from re import L as L
from re import M as M
from re import S as S
from re import X as X
from typing import TYPE_CHECKING, Generator, TypeVarTuple

from typedre.builder import PatternBuilder as _PatternBuilder
from typedre.converterlist import ConverterList as c
from typedre.match import Match as Match
from typedre.pattern import Pattern as Pattern

if TYPE_CHECKING:
    import re


__version__ = "0.1.0"
__version_info__ = (0, 1, 0)
__author__ = "Dominic Price"


def new(prefix: str = "") -> _PatternBuilder[()]:
    return _PatternBuilder(prefix)


Ts = TypeVarTuple("Ts")


def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: c[*Ts],
    flags: "re._FlagsType" = 0,
) -> Match[*Ts] | None:
    return Pattern(pattern, converters, flags=flags).match(string)


def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: c[*Ts],
    flags: "re._FlagsType" = 0,
) -> Match[*Ts] | None:
    return Pattern(pattern, converters, flags=flags).fullmatch(string)


def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: c[*Ts],
    flags: "re._FlagsType" = 0,
) -> Match[*Ts] | None:
    return Pattern(pattern, converters, flags=flags).search(string)


def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: c[*Ts],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[*Ts], None, None]:
    yield from Pattern(pattern, converters, flags=flags).finditer(string)

import re
import sys
from typing import Generator, Generic, TypeVarTuple, overload

from typedre.match import Match
from typedre.converterlist import ConverterList

Ts = TypeVarTuple("Ts")


class Pattern(Generic[*Ts]):
    def __init__(
        self,
        pattern: str | re.Pattern[str],
        converters: ConverterList[*Ts] | None = None,
        *,
        flags: "re._FlagsType" = 0,
    ):
        self._pat = re.compile(pattern, flags)
        self._conv = converters if converters is not None else ConverterList()
        if self._pat.groups != len(self._conv):
            msg = "number of converters does not equal number of capturing groups"
            raise RuntimeError(msg)

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None:
        m = self._pat.match(string, pos, endpos)
        if m is None:
            return None
        return Match(m, self)

    def fullmatch(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None:
        m = self._pat.fullmatch(string, pos, endpos)
        if m is None:
            return None
        return Match(m, self)

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None:
        m = self._pat.search(string, pos, endpos)
        if m is None:
            return None
        return Match(m, self)

    def finditer(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Generator[Match[*Ts], None, None]:
        for m in self._pat.finditer(string, pos, endpos):
            yield Match(m, self)

    # because the converters argument is optional, we need to overload
    # new to get the correct return type
    @overload
    def __new__(
        cls, pattern: str | re.Pattern[str], *, flags: "re._FlagsType" = 0
    ) -> "Pattern[()]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: ConverterList[*Ts],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[*Ts]": ...
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: ConverterList[*Ts] | None = None,
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[()] | Pattern[*Ts]":
        return super().__new__(cls)

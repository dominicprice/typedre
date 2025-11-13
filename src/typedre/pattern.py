import re
import sys
from typing import Any, Callable, Generator, Generic, TypeVarTuple

from typedre.match import Match

Ts = TypeVarTuple("Ts")


class Pattern(Generic[*Ts]):
    def __init__(
        self,
        pattern: str | re.Pattern[str],
        converters: tuple[Callable[[str], Any], ...] = (),
        flags: "re._FlagsType" = 0,
    ):
        self._pat = re.compile(pattern, flags)
        self._conv = tuple(converters)
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
        return Match(m, self)  # type: ignore

    def fullmatch(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None:
        m = self._pat.fullmatch(string, pos, endpos)
        if m is None:
            return None
        return Match(m, self)  # type: ignore

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None:
        m = self._pat.search(string, pos, endpos)
        if m is None:
            return None
        return Match(m, self)  # type: ignore

    def finditer(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Generator[Match[*Ts], None, None]:
        for m in self._pat.finditer(string, pos, endpos):
            yield Match(m, self)  # type: ignore

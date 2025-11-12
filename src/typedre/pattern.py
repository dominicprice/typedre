import re
import sys
from typing import (
    Any,
    Callable,
    Generator,
    Generic,
    TypeVar,
    TypeVarTuple,
    overload,
)

from typedre.match import Match

# currently there is no way in python of mapping a TypeVarTuple onto
# another type, e.g. having a function which accepts a tuple of
# callable with specific return types and having the function generic
# on those return types. As the Pattern class accepts a list of
# converters and the Match objects need to know the return types of
# those converters, the only way to properly(?) type the constructor
# so that we have access to the return types is to overload it for all
# possible numbers of converters. As this file can't be infinitely
# long, the constructor is overloaded for up to 9 converters, after
# which type hints will no longer be available
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")
Ts = TypeVarTuple("Ts")
C = Callable[[str], T1]


class Pattern(Generic[*Ts]):
    def __init__(
        self,
        pattern: str | re.Pattern[str],
        *converters: Callable[[str], Any],
        flags: "re._FlagsType" = 0,
    ):
        self._pat = re.compile(pattern, flags)
        self._conv = converters
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

    # here come the typing overloads --- instead of cluttering up the
    # __init__ definition with loads of overloads, we just annotate
    # the __new__ method as LSPs generally don't display these
    # signatures, so this just silently ensures that the type of the
    # callables matches the deduced generic type of Pattern
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[()]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        c6: C[T6],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5, T6]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        c6: C[T6],
        c7: C[T7],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5, T6, T7]": ...

    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        c6: C[T6],
        c7: C[T7],
        c8: C[T8],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5, T6, T7, T8]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        c6: C[T6],
        c7: C[T7],
        c8: C[T8],
        c9: C[T9],
        *,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5, T6, T7, T8, T9]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        c1: C[T1],
        c2: C[T2],
        c3: C[T3],
        c4: C[T4],
        c5: C[T5],
        c6: C[T6],
        c7: C[T7],
        c8: C[T8],
        c9: C[T9],
        *cs: C,
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[T1, T2, T3, T4, T5, T6, T7, T8, T9, *Ts]": ...
    def __new__(cls, *args, **kwargs):  # type: ignore
        return super().__new__(cls)

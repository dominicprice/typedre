import re
import sys
from typing import Any, Callable, Generator, Generic, TypeVarTuple, overload, TypeVar

from typedre.match import Match

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")
Ts = TypeVarTuple("Ts")


class Pattern(Generic[*Ts]):
    _pat: "re.Pattern"
    _conv: tuple[Callable[[str], Any]]

    def __init__(
        self,
        pattern: str | re.Pattern[str],
        converters: tuple[Callable[[str], Any], ...] = (),
        flags: "re._FlagsType" = 0,
    ): ...

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None: ...

    def fullmatch(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None: ...

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Match[*Ts] | None: ...

    def finditer(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> Generator[Match[*Ts], None, None]: ...

    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[()]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[Callable[[str], _T1]],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2]": ...

    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
            Callable[[str], _T6],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5, _T6]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
            Callable[[str], _T6],
            Callable[[str], _T7],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5, _T6, _T7]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
            Callable[[str], _T6],
            Callable[[str], _T7],
            Callable[[str], _T8],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
            Callable[[str], _T6],
            Callable[[str], _T7],
            Callable[[str], _T8],
            Callable[[str], _T9],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]": ...
    @overload
    def __new__(
        cls,
        pattern: str | re.Pattern[str],
        converters: tuple[
            Callable[[str], _T1],
            Callable[[str], _T2],
            Callable[[str], _T3],
            Callable[[str], _T4],
            Callable[[str], _T5],
            Callable[[str], _T6],
            Callable[[str], _T7],
            Callable[[str], _T8],
            Callable[[str], _T9],
            *tuple[Callable[[str], Any], ...],
        ],
        flags: "re._FlagsType" = 0,
    ) -> "Pattern[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, *tuple[Any, ...]]": ...

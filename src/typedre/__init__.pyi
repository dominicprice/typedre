import re
from typing import (
    Callable,
    Final,
    TypeVarTuple,
    overload,
    Any,
    TypeVar,
    Generator,
)

from typedre.builder import PatternBuilder as _PatternBuilder
from typedre.match import Match as Match
from typedre.pattern import Pattern as Pattern

__version__: Final[str]
__version_info__: Final[tuple[int, int, int]]
__author__: Final[str]


def new(prefix: str = "") -> _PatternBuilder[()]: ...


_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")
_Ts = TypeVarTuple("_Ts")


@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    flags: "re._FlagsType" = 0,
) -> Match[()] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], _T1]],
    flags: "re._FlagsType" = 0,
) -> Match[_T1] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
        Callable[[str], _T6],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9] | None: ...
@overload
def match(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, *tuple[Any, ...]] | None: ...


@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    flags: "re._FlagsType" = 0,
) -> Match[()] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], _T1]],
    flags: "re._FlagsType" = 0,
) -> Match[_T1] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
        Callable[[str], _T6],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9] | None: ...
@overload
def fullmatch(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, *tuple[Any, ...]] | None: ...


@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    flags: "re._FlagsType" = 0,
) -> Match[()] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], _T1]],
    flags: "re._FlagsType" = 0,
) -> Match[_T1] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
        Callable[[str], _T6],
    ],
    flags: "re._FlagsType" = 0,
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9] | None: ...
@overload
def search(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, *tuple[Any, ...]] | None: ...


@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    flags: "re._FlagsType" = 0,
) -> Generator[Match[()], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[Callable[[str], _T1]],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
    ],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1, _T2], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
    ],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1, _T2, _T3], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
    ],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1, _T2, _T3, _T4], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
    ],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1, _T2, _T3, _T4, _T5], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
    converters: tuple[
        Callable[[str], _T1],
        Callable[[str], _T2],
        Callable[[str], _T3],
        Callable[[str], _T4],
        Callable[[str], _T5],
        Callable[[str], _T6],
    ],
    flags: "re._FlagsType" = 0,
) -> Generator[Match[_T1, _T2, _T3, _T4, _T5, _T6], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Generator[Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Generator[Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Generator[Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9], None, None]: ...
@overload
def finditer(
    pattern: "str | re.Pattern[str]",
    string: str,
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
) -> Generator[
    Match[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, *tuple[Any, ...]], None, None
]: ...

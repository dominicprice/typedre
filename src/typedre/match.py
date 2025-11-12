import re
from typing import TYPE_CHECKING, TypeVarTuple, overload

if TYPE_CHECKING:
    from typedre.pattern import Pattern

Ts = TypeVarTuple("Ts")


class Match(tuple[str, *Ts]):
    def __new__(cls, m: re.Match[str], pattern: "Pattern"):
        groups = pattern._conv(m.groups())
        return super().__new__(cls, (m[0], *groups))

    def __init__(self, m: re.Match[str], pattern: "Pattern"):
        self._m = m
        self.re = pattern

    def group(self, *indices: int):
        if len(indices) == 0:
            return None
        elif len(indices) == 1:
            return self[indices[0]]
        return tuple(self[i] for i in indices)

    def groups(self) -> tuple[*Ts]:
        return self[1:]

    @overload
    def start(self) -> int: ...
    @overload
    def start(self, group: int) -> int: ...
    def start(self, group: int = 0):
        return self._m.start(group)

    @overload
    def end(self) -> int: ...
    @overload
    def end(self, group: int) -> int: ...
    def end(self, group: int = 0):
        return self._m.end(group)

    @overload
    def span(self) -> int: ...
    @overload
    def span(self, group: int) -> int: ...
    def span(self, group: int = 0):
        return self._m.end(group)

    @property
    def pos(self) -> int:
        return self._m.pos

    @property
    def endpos(self) -> int:
        return self._m.endpos

    @property
    def lastindex(self) -> int | None:
        return self._m.lastindex

    @property
    def lastgroup(self) -> int | str | None:
        return self._m.lastgroup

    @property
    def string(self) -> str:
        return self._m.string

import builtins as b
import re
from typing import Any, Callable, Generic, Iterable, TypeVar, TypeVarTuple

from typedre.pattern import Pattern

T = TypeVar("T")
Ts = TypeVarTuple("Ts")


class PatternBuilder(Generic[*Ts]):
    def __init__(self, prefix: str = ""):
        self.pattern = prefix
        self.converters: list[Callable[[str], Any]] = []

    def compile(self) -> Pattern[*Ts]:
        "returns a Pattern from the current state of the builder"
        pattern = re.compile(self.pattern)
        return Pattern(pattern, *self.converters)  # type: ignore

    def lit(self, pattern: b.str) -> "PatternBuilder[*Ts]":
        "adds an arbitrary non-matching pattern"
        self.pattern += pattern
        return self

    def str(self, pattern: b.str) -> "PatternBuilder[*Ts, b.str]":
        "adds an arbitrary string capturing group"
        return self.val(pattern, str)

    def int(self, pattern: b.str, base: b.int = 10) -> "PatternBuilder[*Ts, b.int]":
        "adds an arbitrary integer capturing group"
        return self.val(pattern, lambda s: int(s, base))

    def val(
        self,
        pattern: b.str,
        converter: Callable[[b.str], T],
    ) -> "PatternBuilder[*Ts, T]":
        "adds an arbitrary capturing group using the given converter"
        self.pattern += "(" + pattern + ")"
        self.converters.append(converter)
        return self  # type: ignore

    def float(self, allow_exp: bool = True) -> "PatternBuilder[*Ts, b.float]":
        """
        adds a capturing group which matches and converts to a float.

        if allow_exp is True, then an exponential suffix (e.g. E4) is
        allowed at the end of the number.
        """
        pat = r"[-+]?(?:\d+\.\d*|\.\d+|\d+)"
        if allow_exp:
            pat += r"(?:[eE][-+]?\d+)?"
        return self.val(pat, float)

    def dec(self, allow_sign: bool = True) -> "PatternBuilder[*Ts, b.int]":
        """
        adds a capturing group which matches and converts to a
        decimal integer.

        if allow_sign is true, a leading + or - sign is allowed.
        """
        pat = r"[+-]?" if allow_sign else r""
        pat += r"\d+"
        return self.val(pat, int)

    def hex(self, length: b.int | None = None) -> "PatternBuilder[*Ts, b.int]":
        """
        adds a capturing group which matches and converts to a
        hexadecimal integer.

        if length is provided, then only matches hex string of exactly
        length characters
        """
        modifier = "+" if length is None else f"{{{length}}}"
        return self.val(f"[0-9a-fA-F]{modifier}", lambda s: int(s, 16))

    def alpha(self, length: b.int | None = None) -> "PatternBuilder[*Ts, b.str]":
        """
        adds a capturing group which matches the characters a-Z and A-Z.

        if length is provided, then only matches strings of exactly
        length characters
        """
        modifier = "+" if length is None else f"{{{length}}}"
        return self.val(f"[a-zA-Z]{modifier}", str)

    def alphanum(self, length: b.int | None = None) -> "PatternBuilder[*Ts, b.str]":
        """
        adds a capturing group which matches the characters a-z, A-Z and
        0-9.

        if length is provided, then only matches strings of exactly
        length characters
        """
        modifier = "+" if length is None else f"{{{length}}}"
        return self.val(f"[a-zA-Z0-9]{modifier}", str)

    def ws(self, required: bool = True) -> "PatternBuilder[*Ts]":
        """
        adds a non-capturing group which matches whitespace.

        if required is True, then ensures at least one whitespace
        character is matched
        """
        modifier = "+" if required else "*"
        return self.lit(r"\s" + modifier)

    def bool(
        self,
        true_values: Iterable[b.str] | None = None,
        false_values: Iterable[b.str] | None = None,
    ) -> "PatternBuilder[*Ts, b.bool]":
        "adds a capturing group which matches and converts boolean values"
        t = (
            {"t", "true", "1", "on", "yes", "y"}
            if true_values is None
            else set(true_values)
        )
        f = (
            {"f", "false", "0", "off", "no", "n"}
            if false_values is None
            else set(false_values)
        )

        def tobool(s: str) -> bool:
            if s in t:
                return True
            if s in f:
                return False
            raise ValueError

        pat = "|".join(t.union(f))

        return self.val(pat, tobool)

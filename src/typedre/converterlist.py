from typing import Any, Callable, Iterable, TypeVar, TypeVarTuple, overload

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


class ConverterList(tuple[*Ts]):
    """
    This class is required solely to ensure that the types of groups
    in the Match class returned from a Pattern are typed correctly.

    The TypeVarTuple is essential for us to be able to type all of
    this correctly, as it allows us to store the intended types which
    matched groups are converted to, but we have a problem when
    constructing a Pattern, as we accept a list of conversion
    functions (whose return types are the types which should be
    assigned to each group in the returned Match), but there is no way
    of mapping a TypeVarTuple, see
    https://github.com/python/typing/issues/1216.

    The only way I could think to do this was to overload the
    constructor for a reasonable number of generic arguments, manually
    writing in the correctly transformed return type and then
    silencing the type check warning on the actual
    implementation. This works, allowing an arbitrary number of
    correctly typed overloads but makes the constructor's signature
    very messy. It also requires adding these overloads for every
    function which accepts a list of converters.

    The solution to minimise the noise is this class, which provides
    some benefits to us:
    * It is overloaded so that the generic underlying types are
      correctly deduced when constructed from a list of callables
      with different return types
    * The overloads are attached to the __new__ function instead of
      the __init__function, which means that the constructor signature
      remains simple as LSPs generally don't display overloads of
      __new__
    * It is a subclass of tuple, so when correctly typed it will
      automatically give us the exact type when elements are selected
      using __getitem__

    The downside is that instead of being able to accept any Iterable of
    callables, we must always use this class.
    """

    def __init__(self, *converters: Callable[[str], Any]):
        self.converters = converters

    def __call__(self, vals: Iterable[str]) -> tuple[*Ts]:
        return [c(v) for c, v in zip(self.converters, vals)]  # type: ignore

    def join(self, converter: Callable[[str], T1]) -> "ConverterList[*Ts, T1]":
        return ConverterList(*self, converter)  # type: ignore

    @overload
    def __new__(cls) -> "ConverterList[()]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
    ) -> "ConverterList[T1]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
    ) -> "ConverterList[T1, T2]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
    ) -> "ConverterList[T1, T2, T3]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
    ) -> "ConverterList[T1, T2, T3, T4]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
    ) -> "ConverterList[T1, T2, T3, T4, T5]": ...
    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
        c6: Callable[[str], T6],
    ) -> "ConverterList[T1, T2, T3, T4, T5, T6]": ...
    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
        c6: Callable[[str], T6],
        c7: Callable[[str], T7],
    ) -> "ConverterList[T1, T2, T3, T4, T5, T6, T7]": ...

    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
        c6: Callable[[str], T6],
        c7: Callable[[str], T7],
        c8: Callable[[str], T8],
    ) -> "ConverterList[T1, T2, T3, T4, T5, T6, T7, T8]": ...
    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
        c6: Callable[[str], T6],
        c7: Callable[[str], T7],
        c8: Callable[[str], T8],
        c9: Callable[[str], T9],
    ) -> "ConverterList[T1, T2, T3, T4, T5, T6, T7, T8, T9]": ...
    @overload
    def __new__(
        cls,
        c1: Callable[[str], T1],
        c2: Callable[[str], T2],
        c3: Callable[[str], T3],
        c4: Callable[[str], T4],
        c5: Callable[[str], T5],
        c6: Callable[[str], T6],
        c7: Callable[[str], T7],
        c8: Callable[[str], T8],
        c9: Callable[[str], T9],
        *cs: Callable[[str], Any],
    ) -> "ConverterList[T1, T2, T3, T4, T5, T6, T7, T8, T9, *Ts]": ...
    def __new__(cls, *converters):  # type: ignore
        return super().__new__(cls, converters)

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

from typedre.builder import PatternBuilder as _PatternBuilder
from typedre.match import Match as Match
from typedre.pattern import Pattern as Pattern

__version__ = "0.1.0"
__version_info__ = (0, 1, 0)
__author__ = "Dominic Price"


def new(prefix: str = "") -> _PatternBuilder[()]:
    return _PatternBuilder(prefix)

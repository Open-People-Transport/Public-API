from inspect import getdoc
from typing import Any, Callable, Iterable, TypeVar


def description(obj: Any) -> str:
    """Get description of a class, attained from docstrings"""
    return getdoc(obj) or ""


_T = TypeVar("_T")


def multifilter(functions: Iterable[Callable[[_T], bool]], iterable: Iterable[_T]):
    return filter(lambda val: all(f(val) for f in functions), iterable)

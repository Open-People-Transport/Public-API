from inspect import getdoc
from typing import Any


def description(obj: Any) -> str:
    """Get description of a class, attained from docstrings"""
    return getdoc(obj) or ""

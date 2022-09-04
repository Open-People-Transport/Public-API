from inspect import cleandoc, isclass
from typing import Any, Callable, Iterable, TypeVar


class ModelInfo:
    __slots__ = ("title", "description")

    def __init__(self, obj: Any) -> None:
        try:
            schema = obj.schema()
        except Exception:
            cls = obj if isclass(obj) else type(obj)
            self.title = cls.__name__
            self.description = None if cls.__doc__ is None else cleandoc(cls.__doc__)
        else:
            self.title = schema["title"]
            self.description = schema.get("description", None)

    @property
    def gqldescription(self) -> str:
        # Strawberry only accepts strings as descriptions, but None should be used.
        return self.description  # type: ignore


_T = TypeVar("_T")


def multifilter(functions: Iterable[Callable[[_T], bool]], iterable: Iterable[_T]):
    return filter(lambda val: all(f(val) for f in functions), iterable)

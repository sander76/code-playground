from inspect import signature
from typing import Any, Literal


def foo(snap: int, crackle: str = "hello", pop: float = 3.14) -> None:
    pass


valid_values = list(signature(foo).parameters)
FooArgname = Literal[*valid_values]

assert FooArgname == Literal["snap", "crackle", "pop"]

# example usage: making a type for valid kwargs for foo
ValidFooKwargs = dict[FooArgname, Any]

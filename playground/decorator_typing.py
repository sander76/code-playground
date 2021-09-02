import logging
from typing import Any, Callable, TypeVar

_LOGGER = logging.getLogger(__name__)

Wrapped = TypeVar("Wrapped")


def add_doc(doc_string: str) -> Callable[..., Any]:
    def _dec(func):
        func.__doc__ = doc_string
        return func

    return _dec


def a_decorator(func: Callable[..., str]) -> Callable[..., str]:
    def _wrapper(*args, **kwargs):
        value = func()
        return f"a_value {value}"

    return _wrapper


@a_decorator
def go():
    return "wrapped value"


@a_decorator
def go_forth():
    print("Yes")


@add_doc("This is the doc")
def do_with_args(val: int, go: str = "yes") -> None:
    print(val, go)


print(go())

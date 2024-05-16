import asyncio
from functools import wraps
from typing import Awaitable, Callable, ParamSpec, TypeVar, reveal_type

P = ParamSpec("P")
R = TypeVar("R")


def rec(name: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def _rec(func: Callable[P, R]) -> Callable[P, R]:
        """Decorate a function which returns a value which is to be recorded.

        Supports both async and non-async calls.
        """

        @wraps(func)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)

            print(name, result)
            return result

        return _wrapper

    reveal_type(_rec)
    return _rec


@rec("myname")
def go(val: int) -> int:
    return val * 10


@rec("some name")
def another_go(val: int, op: str) -> tuple[int, str]:
    return val * 10, op


val = go(10)

result = another_go(10, "adder")

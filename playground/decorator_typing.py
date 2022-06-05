from __future__ import annotations
from typing import Any, Callable, Concatenate, TypeVar
from typing_extensions import ParamSpec

# using paramspec
# this works by default in python v3.10.
# install typing-extensions if you're running a lower version.

P = ParamSpec("P")
R = TypeVar("R")


def a_decorator(func: Callable[P, R]) -> Callable[P, R]:
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("wrapped")
        return await func(*args, **kwargs)

    return _wrapper


@a_decorator
async def just_a_function(value1: int, value2: str) -> bool:
    print(f"{value1}-{value2}")
    return True


import asyncio

asyncio.run(just_a_function(10, "10"))

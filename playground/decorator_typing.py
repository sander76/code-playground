from typing import Awaitable, Callable, ParamSpec, TypeVar
import asyncio

P = ParamSpec("P")
R = TypeVar("R")


def a_decorator(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("wrapped")
        return await func(*args, **kwargs)

    return _wrapper


@a_decorator
async def just_a_function(value1: int) -> bool:
    print(value1)
    return isinstance(value1, int)


async def go(value1: int) -> bool:
    return await just_a_function(value1)


# mypy raises an error here:
# Argument 1 to "run" has incompatible type "Awaitable[bool]"; expected "Coroutine[Any, Any, <nothing>]"  [arg-type]mypy
asyncio.run(just_a_function(10))


asyncio.run(go(10))

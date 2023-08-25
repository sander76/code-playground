from typing import Awaitable, Callable


async def go(some_val: int) -> int:
    return some_val * 2


async def wrap(function: Callable[[int], Awaitable[int]]) -> int:
    return await function(6)


if __name__ == "__main__":
    wrap(go)

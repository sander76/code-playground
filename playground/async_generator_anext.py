from typing import AsyncGenerator
import asyncio


async def a_generator() -> AsyncGenerator[str, None]:
    for i in range(10):
        yield str(i)


async def iter_over(async_generator: AsyncGenerator[str, None]):
    val0 = await anext(async_generator)

    print(f"this is val0 {val0}")

    async for other in async_generator:
        print(f"other {other}")


asyncio.run(iter_over(a_generator()))

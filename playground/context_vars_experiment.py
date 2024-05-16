from contextvars import ContextVar
import asyncio

my_list: ContextVar[list[int]] = ContextVar("my_list")


async def list_adder(loops: int):
    new_context = my_list.get([])

    for i in range(loops):
        new_context.append(i)
        await asyncio.sleep(0.1)
    return new_context


async def workers():
    result = await asyncio.gather(list_adder(10), list_adder(5))
    for res in result:
        print(res)


asyncio.run(workers())

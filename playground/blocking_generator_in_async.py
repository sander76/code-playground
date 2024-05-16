import asyncio
import time


def blocking():
    for i in range(100):
        time.sleep(0.5)

        yield i


async def get_blocking():
    async for value in asyncio.to_thread(blocking):
        print(value)


async def printer():
    for i in range(100):
        await asyncio.sleep(0.4)
        print(f"async slept {i}")


async def go():
    tsk = asyncio.create_task(printer())
    await get_blocking()
    await tsk


if __name__ == "__main__":
    asyncio.run(go())

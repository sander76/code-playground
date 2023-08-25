import asyncio


class Looper:
    def __init__(self) -> None:
        self._queue = asyncio.Queue()

    @property
    def queue(self):
        return self._queue

    def __aiter__(self):
        return self

    async def __anext__(self):
        item = await self._queue.get()
        if item == 8:
            raise StopAsyncIteration
        return item


async def putter(looper):
    for i in range(10):
        await asyncio.sleep(0.5)

        await looper.queue.put(i)


async def listener(looper):
    async for item in looper:
        print(item)


async def go():
    looper = Looper()
    await asyncio.gather(putter(looper), listener(looper))


asyncio.run(go())

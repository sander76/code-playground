import asyncio

from async_timeout import timeout


async def collection_with_timeout(queue: asyncio.Queue) -> dict:
    async with timeout(1):
        new_data = None
        data = {}
        try:
            while True:
                new_data = await queue.get()
                data.update(new_data)
        finally:
            if new_data:
                print("updating last item")
                data.update(new_data)
            return data


async def queue_filler(queue: asyncio.Queue):
    for i in range(20):
        await queue.put({f"value_{i}": i})
        await asyncio.sleep(0.1)


async def run():
    queue = asyncio.Queue()

    asyncio.create_task(queue_filler(queue))

    for i in range(2):
        result = await collection_with_timeout(queue)
        print(result)


asyncio.run(run())

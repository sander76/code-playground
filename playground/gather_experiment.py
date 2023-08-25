import asyncio


async def task1():
    while 1:
        await asyncio.sleep(1)

        raise Exception("just stop.")


async def task2():
    while 1:
        await asyncio.sleep(0.2)
        print("not stopping")


async def go():
    all = [asyncio.ensure_future(task1()), asyncio.ensure_future(task2())]
    try:
        await asyncio.gather(*all)
    except Exception:
        print("caught exception")
        for task in all:
            task.cancel()

        await asyncio.gather(*all, return_exceptions=True)

    await asyncio.sleep(2)


asyncio.run(go())

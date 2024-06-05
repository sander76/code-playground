import asyncio


async def tasker():
    print("mytask")


async def do_stuff():
    tsk = asyncio.create_task(tasker())
    print("going to sleep")
    await asyncio.sleep(1)
    print("waking up")

    return tsk


async def run():
    tsk = await do_stuff()
    await tsk


asyncio.run(run())

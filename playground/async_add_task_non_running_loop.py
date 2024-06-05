import asyncio


async def tsk_1():
    print("executed.")


async def tsk_2():
    for i in range(10):
        await asyncio.sleep(1)
        print(f"loop nr {i}")


loop = asyncio.get_event_loop()
loop.create_task(tsk_1())
asyncio.run(tsk_2())

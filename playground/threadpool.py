import time
import asyncio
import concurrent.futures


def wait_in_thread():
    print("Running inside other thread and wait for 5 seconds.")
    time.sleep(5)
    return "thread finished."


async def printer():
    for i in range(10):
        await asyncio.sleep(0.5)
        print(f"Running in eventloop. {i=}")


async def get_from_other_thread(loop):
    print("running in threadpool")
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, wait_in_thread)

    return result


async def go():
    loop = asyncio.get_running_loop()
    task1 = loop.create_task(printer())
    result = await get_from_other_thread(loop)
    print(result)

    await task1


asyncio.run(go())

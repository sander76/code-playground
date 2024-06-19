import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

asyncio.get_event_loop()


async def call_back():
    await asyncio.sleep(1)
    return 10


def in_thread(func):
    result = None

    def _run():
        nonlocal result
        _loop = asyncio.new_event_loop()
        result = _loop.run_until_complete(func)

    th = threading.Thread(target=_run)
    result = th.start()
    th.join()
    return result


async def run():
    print(in_thread(call_back()))


asyncio.run(run())

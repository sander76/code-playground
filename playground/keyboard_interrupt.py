"""Some KeyboardInterrupt code.

Use this code when targetting a windows machine.
Otherwise you should probably be following:

https://www.roguelynn.com/words/asyncio-we-did-it-wrong/

Windows does not allow for adding signal handlers. So we should be using
KeyboardInterrupt instead.
"""

import asyncio
import logging
from asyncio import CancelledError

_LOGGER = logging.getLogger(__name__)


async def long_runner():
    """Just a long running task."""
    try:
        while True:
            await asyncio.sleep(1)
            print("long runner")
    except CancelledError:
        # called when the final shutdown function is run.
        print("run when this task is cancelled.")
    finally:
        await asyncio.sleep(2)
        print("finished.")


async def short_runner():
    """Just a short running task."""
    print("Start short running task.")
    await asyncio.sleep(1)
    print("Finish short running task.")


async def nested():
    """A nested coroutine.

    Illustrating that putting a keyboard interrupt here has no effect.
    """
    try:
        asyncio.create_task(long_runner(), name="long running task.")
        asyncio.create_task(short_runner(), name="short running task.")
    except KeyboardInterrupt:
        # this isn't caught. Keyboard interrupt must be outside the event loop
        print("nested keyboard interrupt.")
        raise


async def shutdown(loop):
    """The shutdown task."""
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    for task in tasks:
        print(f"Cancelling task: {task}")
        task.cancel()

    await asyncio.gather(*tasks)
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(nested())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Handling the exception outside the loop.")
    finally:
        print(f"loop is running: {loop.is_running()}")
        loop.run_until_complete(shutdown(loop))
        print("closing the loop.")
        loop.close()


if __name__ == "__main__":
    main()

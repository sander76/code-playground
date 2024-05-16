"""Some KeyboardInterrupt code.

https://www.roguelynn.com/words/asyncio-we-did-it-wrong/
"""

import asyncio
import logging
import signal
from asyncio import CancelledError
from typing import Collection, Coroutine

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
    raise ValueError("Some error that should stop the program.")


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


def run_tasks(tasks: Collection[Coroutine]):
    loop = asyncio.get_event_loop()

    def handle_exception(loop, context):
        msg = context.get("exc", context["message"])
        print(context)
        print(f"error {msg}")
        asyncio.create_task(shutdown())

    async def shutdown():
        """The shutdown task."""
        print("shutting down.")
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

        for task in tasks:
            print(f"Cancelling task: {task}")
            task.cancel()

        await asyncio.gather(*tasks)
        loop.stop()

    # register signals in the loop.
    for _signal in (signal.SIGHUP, signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(_signal, lambda: asyncio.create_task(shutdown()))
    loop.set_exception_handler(handle_exception)
    try:
        for task in tasks:
            loop.create_task(task)
        loop.run_forever()
    finally:
        loop.close()
        print("shutdown success.")


def main():
    run_tasks([nested()])


if __name__ == "__main__":
    main()

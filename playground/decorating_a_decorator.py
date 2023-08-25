import asyncio
from re import L

enabled = False


def the_decorator(lastname: str):
    def _wrapper(func):
        async def _wrapped(*args, **kwargs):
            print(f"wrapped with {lastname}")
            await func(*args, **kwargs)

        return _wrapped

    return _wrapper


def decorator_wrapper(lastname: str):
    global enabled

    def _wrapper(func):
        async def wrapping_the_decorator(*args, **kwargs):
            if enabled:
                return the_decorator(lastname)(func(*args, **kwargs))
            else:
                return await func(*args, **kwargs)

        return wrapping_the_decorator

    return _wrapper


@decorator_wrapper("teunissen")
async def wrapped(name: str):
    print(name)


asyncio.run(wrapped("sander"))

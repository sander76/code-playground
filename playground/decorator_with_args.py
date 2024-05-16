import asyncio


def async_rec(name: str):
    def _decorator(func):
        async def _wrapper(*args, **kwargs):
            print(name)
            return await func(*args, **kwargs)

        return _wrapper

    return _decorator


@async_rec("somename")
async def do_print(name: str):
    return f"wrapped {name}"


print(asyncio.run(do_print("sander")))

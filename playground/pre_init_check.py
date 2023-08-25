import asyncio
from typing import Any


class Worker:
    async def go(self):
        print("done")

    async def load_config(self):
        print("configured")


class ExtraWorker(Worker):
    def __init__(self) -> None:
        super().__init__()
        self._initialized = False

    def initialize_wrapper(self, func):
        async def _wrapper(*args, **kwargs):
            await self.load_config()
            return await func(*args, **kwargs)

        return _wrapper

    def __getattribute__(self, __name: str) -> Any:
        attribute = super(ExtraWorker, self).__getattribute__(__name)
        if __name in ["_initialized", "initialize_wrapper", "load_config"]:
            return attribute
        # attribute = self.get_attr(__name)
        if self._initialized:
            return attribute
        else:
            self._initialized = True
            return self.initialize_wrapper(attribute)


async def run(worker: ExtraWorker):
    await worker.go()
    await worker.go()


if __name__ == "__main__":
    worker = ExtraWorker()
    asyncio.run(run(worker))

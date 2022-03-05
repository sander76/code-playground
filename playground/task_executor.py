from __future__ import annotations

import asyncio
from typing import Any, Awaitable, Callable
from time import time

charts = {}


def measure(func):
    async def wrapper(*args, **kwargs):
        start = time()
        await func(*args, **kwargs)
        stop = time()
        charts[func.__name__] = {"start": start, "stop": stop}

    return wrapper


class Task:
    def __init__(
        self, func: Callable[..., Awaitable[Any]], waits_for: list["Task"] = []
    ) -> None:
        self._waits_for = waits_for
        self._func = func
        self.event = asyncio.Event()
        self.result: object = []

    async def go(self):
        if self._waits_for:
            await asyncio.gather(*(task.event.wait() for task in self._waits_for))

        results = (task.result for task in self._waits_for)
        self.result = await self._func(*results)
        self.event.set()


class Tasks:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(
        self, func: Callable[..., Awaitable[Any]], depends: list[Task] = []
    ) -> Task:
        self._tasks.append(task := Task(func, depends))
        return task

    async def execute(self):
        await asyncio.gather(*(task.go() for task in self._tasks))


@measure
async def func1():
    await asyncio.sleep(1)
    print("func1")
    return "func1"


@measure
async def func2(data):
    await asyncio.sleep(1)
    new_data = f"{data} + func2"
    print(new_data)
    return new_data


@measure
async def func3(data, data1):
    await asyncio.sleep(1)
    new_data = f"{data} + {data1} + func3"
    print(new_data)
    return new_data


@measure
async def func4(data):
    new_data = "func4"
    print(new_data)


@measure
async def func5():
    await asyncio.sleep(5)
    print(data := "func5")
    return data


@measure
async def func6(data, data_1):
    await asyncio.sleep(3)
    print(result := f"{data} + {data_1} + func6")
    return result


@measure
async def main():
    tasks = Tasks()

    task1 = tasks.add_task(func1)
    task2 = tasks.add_task(func2, [task1])
    tasks.add_task(func3, [task1, task2])
    tasks.add_task(func4, [task2])
    task6 = tasks.add_task(func5)
    tasks.add_task(func6, [task1, task6])
    await tasks.execute()


def print_chart(chart_with=100):
    base_time = charts["main"]["start"]
    total_execution_time = charts["main"]["stop"] - base_time

    print(f"total execution time: {total_execution_time} [s]")

    scaler = chart_with / total_execution_time

    for name, durations in charts.items():
        start_seconds = " " * int(scaler * (durations["start"] - base_time))
        duration = "-" * int(scaler * (durations["stop"] - durations["start"]))
        if len(duration) == 0:
            duration = "-"
        print(f"{name:>15} {start_seconds}{duration}")


asyncio.run(main())
print_chart()

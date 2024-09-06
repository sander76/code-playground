from typing import Generic, Protocol, TypeVar

T = TypeVar("T")


class JobRunner(Protocol[T]):
    def __call__(self, T) -> T: ...


def go(value: int) -> int:
    return value * 2


def process(runner: JobRunner[int]):
    return runner(2)


val = process(go)
print(val)

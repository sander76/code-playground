from contextlib import contextmanager
from typing import Generator


@contextmanager
def as_decorator() -> Generator[None, None, None]:
    print("start")
    yield
    print("end")


@as_decorator()
def multi(val: int) -> int:
    return 10 * 2


if __name__ == "__main__":
    result = multi(10)
    print(result)

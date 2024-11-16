from contextlib import contextmanager
from typing import Generator


@contextmanager
def as_decorator() -> Generator[int, None, None]:
    result = yield
    result = next(result)

    return result * 2


def multi(val: int) -> int:
    with as_decorator():
        return val


if __name__ == "__main__":
    result = multi(2)
    print(result)

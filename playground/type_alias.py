from typing import TypeAlias, NewType
from uuid import UUID, uuid4

# speed = NewType("speed", int)
# duration = NewType("duration", int)


# def return_two_ints() -> tuple[speed, duration]:
#     return (1, 2)


# def make_it_happend() -> tuple[speed, duration]:
#     speed, duration = return_two_ints()
#     return duration, speed


a = set[str | UUID]


def go(values: a) -> None:
    pass


go({uuid4(), "abc"})
go({"abc"})

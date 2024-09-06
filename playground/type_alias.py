from typing import NewType, TypeAlias
from uuid import UUID, uuid4

speed = NewType("speed", int)
duration = NewType("duration", int)


def return_two_ints() -> tuple[speed, duration]:
    return (speed(1), duration(2))


def make_it_happend() -> tuple[speed, duration]:
    speed, duration = return_two_ints()
    return speed, duration

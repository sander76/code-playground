from typing import NewType

speed = NewType("speed", int)
duration = NewType("duration", int)


def return_two_ints() -> tuple[speed, duration]:
    """Some docstring."""
    return (speed(1), duration(2))


def make_it_happen() -> tuple[speed, duration]:
    """Some docstring."""
    speed, duration = return_two_ints()
    return speed, duration
    # return duration, speed  # this fails on type checking. Switched duration and speed.


def something_with_speed(value: int) -> int:
    return 10 * value


something_with_speed(10)
something_with_speed(speed(2))

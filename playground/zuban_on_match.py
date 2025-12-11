from dataclasses import dataclass
from typing import assert_never


@dataclass
class Square:
    circumference: int = 10


@dataclass
class Circle:
    radius: int = 5


def print_output(obj: Square | Circle) -> int:
    match obj:
        case Square():
            return obj.circumference
        case Circle():
            return obj.radius
        case _:
            assert_never(obj)

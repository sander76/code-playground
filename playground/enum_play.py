from enum import Enum, StrEnum


class State(Enum):
    UP = ["UP", "1"]
    DOWN = ["DOWN", "2"]


print("UP" in State.UP.value)

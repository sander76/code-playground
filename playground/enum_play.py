from __future__ import annotations

from enum import Enum, StrEnum
from typing import Self


class State(Enum):
    UP = ["UP", "1"]
    DOWN = ["DOWN", "2"]


print("UP" in State.UP.value)


class MyEnum(Enum):
    VAL1 = 10
    VAL2 = 20

    DEFAULT = VAL1


if __name__ == "__main__":
    print("default value: ", MyEnum.DEFAULT)
    print("")
    print("all", list(MyEnum))
    for val in MyEnum:
        print(val)

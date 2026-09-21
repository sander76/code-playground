from enum import Enum
from typing import Literal


class Empty(Enum):
    token = 0


NO_VALUE = Empty.token


class NOTHING:
    pass


def func(value: int | None | Empty | type[NOTHING]):
    print("************************************")

    print(f"You choose: {value}")
    if value is not NOTHING:
        print("abc")
    if value is NOTHING:
        print(22)
    elif value is NO_VALUE:
        print("0")
    else:
        print(500)


func(10)
func(None)
func(NO_VALUE)
func(NOTHING)

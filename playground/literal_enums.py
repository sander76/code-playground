from enum import Enum, auto
from typing import Literal, assert_never


class MyEnum(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()


def go(value: Literal[MyEnum.ONE, MyEnum.TWO]):
    match value:
        case MyEnum.ONE:
            print("value one")
        case MyEnum.TWO:
            print("value two")
        case _:
            assert_never(value)


go(value=MyEnum.ONE)

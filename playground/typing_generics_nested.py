"""
Using TypeVar and Generic to create a base class which takes an init parameter.
This init parameter is typed according to the overriding class.

Also have a look here: https://stackoverflow.com/questions/64873588/typevbar-in-class-init-type-hinting#64874113
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class BaseClass(Generic[T]):
    def __init__(self, value: T):
        self._value = value

    def go(self) -> T:
        return 1


class SomeForm:
    pass


class Another(BaseClass[int]):
    pass


V = TypeVar("V")


def class_factory(tp: type[V], value: V) -> BaseClass[V]:
    class MyObj(BaseClass[tp], SomeForm):
        pass

    return MyObj


cls = class_factory(int)

v = cls.go()

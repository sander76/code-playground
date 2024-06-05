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


class Class1(BaseClass[str]):
    """A class 1"""


class Class2(BaseClass[int]):
    """Class 2"""


class Class3(BaseClass[T]):
    """Class 3"""


class Inherited(Class3[int]):
    """Inherited"""


class JustClass(Generic[T]):
    def __init__(self, val: T):
        self._val = val

    @property
    def value(self) -> T:
        return self._val


indirect = BaseClass[int](10)
indirect.go()

another = BaseClass[str]("10")
another.go()


a = Class1("A value")
b = Class2(10)
c = Class3(True)
d = Inherited("aa")
e = JustClass("a string")


reveal_type(a._value)
reveal_type(b._value)
reveal_type(c._value)
reveal_type(d._value)
reveal_type(e.value)

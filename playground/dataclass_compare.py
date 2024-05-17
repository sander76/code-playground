from dataclasses import dataclass


@dataclass
class MyClass:
    a: int


a = MyClass(a=10)
b = MyClass(a=10)

assert a == b

c = MyClass(a=11)

assert a == c

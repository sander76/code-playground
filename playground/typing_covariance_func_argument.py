from dataclasses import dataclass
from typing import Callable, TypeVar

# @dataclass
# class MyObj:
#     a: int


# @dataclass
# class Inherit(MyObj):
#     b: int


# class MCls:
#     def __init__(self, sub: MyObj):
#         self.sub = sub


# cls = MCls(sub=Inherit(a=1, b=2))

# Clbl = TypeVar("Clbl", bound=MyObj)


# def go(var: Callable[[Clbl], None]) -> None:
#     obj = Inherit(a=1, b=2)
#     var(obj)


# def clbl(var: Inherit) -> None:
#     print(var)


# go(clbl)


# from typing import Callable, TypeVar


class Resources:
    pass


class MyResources(Resources):
    pass


def simulate_resources(x: Resources) -> float:
    return 2.0


def simulate_my_resources(x: MyResources) -> float:
    return 2.0


ResourcesT = TypeVar("ResourcesT", bound=Resources)


def simulate_once(f: Callable[[ResourcesT], float]) -> None:
    my_resource = MyResources()
    f(my_resource)


simulate_once(simulate_resources)
simulate_once(simulate_my_resources)

from dataclasses import dataclass
from typing import Protocol, TypeVar


class Namespaced(Protocol):
    namespace: str


T = TypeVar("T", bound="Namespaced")


@dataclass
class Foo:
    namespace: str


@dataclass
class Bar:
    namespace: str
    id: int


@dataclass
class NoNs:
    id: int


def frobnicate(namespaced: list[T]) -> list[T]:
    for x in namespaced:
        print(x.namespace)
    return namespaced


result1 = frobnicate([Foo("foo")])
result2 = frobnicate([Bar("bar", 1)])
result3 = frobnicate([NoNs(id=1)])


# from typing import Generic, Protocol, TypeVar


# class Addable(Protocol):
#     def go(self, value: int) -> int: ...


# TAddable = TypeVar("TAddable", Addable, float)


# def go(value: TAddable) -> None:
#     print(value.go(10))


# class MyAddable:
#     def go(self, value: int) -> int:
#         return value * 2


# go(MyAddable())


# class GenericAddable(Generic[TAddable]):
#     def __init__(self) -> None:
#         self.values: list[TAddable] = []

#     def add(self, value: TAddable) -> None:
#         self.values.append(value)

#     def val(self) -> TAddable:
#         return self.values[0]


# class SpecificAddable(GenericAddable[MyAddable]): ...


# cls = SpecificAddable()

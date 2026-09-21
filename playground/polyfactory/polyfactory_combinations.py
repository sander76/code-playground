from polyfactory.factories import DataclassFactory
from dataclasses import dataclass


@dataclass
class Option1:
    val: int


@dataclass
class Option2:
    val: str | None = None


@dataclass
class MyClass:
    val: int
    option: Option1 | Option2


class MyClassFactory(DataclassFactory[MyClass]): ...


if __name__ == "__main__":
    combs = list(MyClassFactory.coverage())
    print(combs)

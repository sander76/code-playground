from dataclasses import dataclass
from enum import Enum

from polyfactory.factories import DataclassFactory


@dataclass
class HomeTown:
    name: str


@dataclass
class Person:
    name: str
    age: float
    height: float
    weight: float
    home_town: HomeTown


class PersonFactory(DataclassFactory[Person]):
    __model__ = Person


def test_random_seed() -> None:
    # the outcome of 'factory.__random__.choice' is deterministic, because Random has been seeded with a set value.
    factory = PersonFactory.build(**{"home_town.name": "roermond"})
    print(factory)


class BaseEnum(Enum): ...


class OtherEnum(BaseEnum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class MyModel:
    values: dict[BaseEnum, int]


class MyModelFactory(DataclassFactory[MyModel]): ...


if __name__ == "__main__":
    my_model = MyModelFactory.build()

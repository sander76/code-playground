from dataclasses import dataclass

from polyfactory.factories import DataclassFactory


@dataclass
class Person:
    name: str
    age: float
    height: float
    weight: float


class PersonFactory(DataclassFactory[Person]):
    __model__ = Person

    name = ["sander", "piet"]


def test_random_seed() -> None:
    # the outcome of 'factory.__random__.choice' is deterministic, because Random has been seeded with a set value.
    first = PersonFactory.build()
    assert PersonFactory.build().name == "John"
    assert PersonFactory.build().name == "George"
    assert PersonFactory.build().name == "John"


if __name__ == "__main__":
    test_random_seed()

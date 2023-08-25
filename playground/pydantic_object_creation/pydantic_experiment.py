from __future__ import annotations
from typing import ClassVar, TypeVar
from pydantic import Field, BaseModel


T = TypeVar("T", bound=BaseModel)


class StrictModel(BaseModel):
    type_registry: ClassVar[dict[str, type[StrictModel]]] = {}
    type: str = Field(..., alias="@type")

    @classmethod
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        cls.type_registry[cls.__name__] = cls

    @classmethod
    def __get_validators__(cls):
        yield cls.instantiate_actual_type

    @classmethod
    def instantiate_actual_type(cls, data: dict) -> StrictModel:
        _type_key = {"type", "@type"} & set(data.keys())
        if not _type_key:
            raise ValueError("Model data is missing a 'type' or '@type' field.")
        _type = data.get(_type_key.pop())
        if _type in cls.type_registry:
            return cls.type_registry[_type](**data)
        return super().parse_obj(data)

    @classmethod
    def parse_obj(cls, data: dict) -> StrictModel:
        return cls.instantiate_actual_type(data)


class Animal(StrictModel):
    type: str = Field("Animal", alias="@type")

    def sound(self) -> None:
        print("Animal!")


class Dog(Animal):
    type: str = Field("Dog", alias="@type")

    def sound(self) -> None:
        print("Woef!")


class Lion(Animal):
    type: str = Field("Lion", alias="@type")

    def sound(self):
        print("Rrraaahhh!")


class Zoo(StrictModel):
    type: str = Field("Zoo", alias="@type")
    animals: list[Animal] = []


def test_types():
    zoo = Zoo.parse_obj(
        {
            "type": "Zoo",
            "animals": [
                {"type": "Dog"},
                {"type": "Lion"},
                {"type": "Dog"},
                {"type": "Dragon"},
            ],
        }
    )
    for animal in zoo.animals:
        animal.sound()
    print(zoo)


if __name__ == "__main__":
    test_types()

from typing import Annotated, Literal

from pydantic import BaseModel, Field


class Dog(BaseModel):
    pet_type: Literal["dog"] = "dog"

    leg_count: int = 4
    age: int = 0


class Cat(BaseModel):
    pet_type: Literal["cat"] = "cat"

    leg_count: int = 4


class Petstore(BaseModel):
    pet: Annotated[Cat | Dog, Field(discriminator="pet_type")]

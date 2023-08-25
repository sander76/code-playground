from pydantic import Field
from pydantic_object_creation.pydantic_experiment import Animal


class Dragon(Animal):
    type: str = Field("Dragon", alias="@type")

    def sound(self) -> None:
        print("hot hot hot")

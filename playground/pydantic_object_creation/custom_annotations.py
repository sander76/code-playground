from typing import Annotated
from pydantic import BaseModel


def add_annotation(model: BaseModel):
    for filed, values in model.model_fields.items():
        print(filed)


class Car(BaseModel):
    name: str
    color: Annotated[int, "help!"]


car = Car(name="honda", color=10)

add_annotation(car)

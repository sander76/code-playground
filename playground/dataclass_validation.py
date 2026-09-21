from pydantic import BaseModel


class SomeObj:
    def __init__(self, value_1: int, value_2):
        self.value_1 = value_1
        self.value_2 = value_2


class MyModel(BaseModel): ...

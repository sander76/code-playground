from dataclasses import dataclass


@dataclass
class MyModel:
    age: int


data = {"age": "10"}

age = MyModel(**data)

print(age)

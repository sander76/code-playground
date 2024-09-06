import dataclasses
from dataclasses import dataclass


@dataclass
class Child:
    value: int
    name: str = "myname"


@dataclass
class Parent:
    value: Child


first = Parent(Child(value=10, name="other name"))

updated = dataclasses.replace(first, value={"value": 8})

print(updated)

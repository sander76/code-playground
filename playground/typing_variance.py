from typing import Sequence
from pydantic import BaseModel


class ItemA:
    ...


class ItemB(ItemA):
    ...


class Items:
    def __init__(self) -> None:
        self.items: list[ItemA] = []

    def add_to_list(self, items: Sequence[ItemA]):
        self.items.extend(items)


cls = Items()

b_items: Sequence[ItemB] = [ItemB()]

cls.add_to_list(b_items)


class A(BaseModel):
    pass


class B(BaseModel):
    pass


class Parent(BaseModel):
    value: list[A | B]


class StrictParent(Parent):
    value: list[A]

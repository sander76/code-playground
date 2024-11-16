#  Literal Types are invariant,
# meaning a Literal of a subtype is not a subtype of the Literal of its supertype.
# For example, though int is a subtype of object, Literal[3] is not a subtype of Literal[object].

from typing import Sequence


class Parent:
    pass


class Child(Parent):
    pass


def go(values: Sequence[Parent]) -> None:
    print(values)


go([Parent()])
go([Child()])

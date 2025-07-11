from typing import Any, NotRequired, TypedDict, Unpack, overload

from pydantic import BaseModel


class MyArgs(TypedDict):
    value_1: int
    value_2: str


def go(**kwargs: Unpack[MyArgs]) -> None:
    pass


def go_with_kwargs(value_1: int, value_2: str) -> None:
    print(value_1)
    print(value_2)


go_with_kwargs(**MyArgs(value_1=1, value_2="abc"))

go_with_kwargs(**{"value_1": 1, "value_2": "abc"})


class MoreArgs(TypedDict):
    value_1: int
    value_2: str
    value_3: NotRequired[bool]


def go_with_not_required(**kwargs: Unpack[MoreArgs]) -> None:
    pass


go_with_not_required()

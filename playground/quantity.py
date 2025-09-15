from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar, overload

ReactrType = TypeVar("ReactrType")


class Reactr(Generic[ReactrType]):
    def __init__(self, default: ReactrType) -> None:
        self._default = default

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = name

    def __get__(self, obj: ReactrType | None, type: type[ReactrType] | None = None) -> ReactrType:
        if obj is None:
            raise ValueError("not possible")
        return obj.__dict__.get(self.name) or self._default

    def __set__(self, obj: object, value: ReactrType) -> None:
        obj.__dict__[self.name] = value

    # def __add__(self, other):
    #     pass

    def __str__(self) -> str:
        return str(self._default)


class MyObj:
    my_q: int = Reactr(10)

    def __init__(self):
        self.my_q = 20


@dataclass
class OtherObj:
    my_q: int = field(default=Reactr(10))


my_obj = MyObj()

val = my_obj.my_q
print(val)

other = OtherObj()
other_val = other.my_q

print(other_val)

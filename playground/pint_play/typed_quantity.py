from dataclasses import dataclass
from typing import Generic, TypeVar

from pint import Quantity

# T = TypeVar("T")


# class QuantityT(Generic[T]):
#     def __init__(self, value: float, unit: T):
#         self._value = value
#         self._unit = unit

#         self._pint = Quantity(value, unit)

#     def __getattr__(self, name: str):
#         return getattr(self._pint, name)


# q1 = Quantity(10.0, "m")
# q2 = Quantity(20.0, "mm")


# print(q1 + q2)


@dataclass
class ExampleAsset:
    capacity: Quantity  # type: ignore


# ex = ExampleAsset(capacity=10)

ex = ExampleAsset(capacity=10)

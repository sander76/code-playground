from __future__ import annotations

from copy import copy
from dataclasses import asdict, dataclass
from typing import Self, TypedDict


@dataclass
class Parameters:
    value_1: int


class DictParams(TypedDict):
    value_1: int
    value_2: int


@dataclass
class Model:
    value_1: int

    @classmethod
    def from_parameters(cls, params: Parameters) -> Model:
        return cls(asdict(params))

    @classmethod
    def from_dataclass(cls, params: DictParams) -> Self:
        new = copy(params)

        return cls(**{key: value for key, value in params.items() if key not in ["value_2"]})

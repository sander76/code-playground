from collections import abc
from typing import Any, NoReturn


class AppendOnly(abc.MutableSequence):
    def __init__(self) -> None:
        self.validations: list[int] = []

    def __len__(self) -> int:
        return len(self.validations)

    def __setitem__(self, value: int) -> None:
        self.validations.append(value)

    def __delitem__(self) -> NoReturn:
        raise ValueError("Not allowed.")

    def __getitem__(self, idx: int) -> int:
        return self.validations[idx]

    def insert(self, index: int, value: Any) -> None:
        self.validations.append(value)


cls_ = AppendOnly()

cls_.append(10)

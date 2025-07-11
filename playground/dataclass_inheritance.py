from abc import ABC, abstractmethod
from dataclasses import dataclass


class MyClass(ABC):
    def __init__(self, value: int):
        self.value = value

    @abstractmethod
    def go(self) -> None: ...


@dataclass
def Inherited(MyClass):
    value_2: int


cls = Inherited()

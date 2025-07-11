from abc import ABC, abstractmethod


class BaseClass(ABC):
    @abstractmethod
    def go(self) -> None: ...


class NewClass(BaseClass):
    def do(self) -> None:
        print("do")

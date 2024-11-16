from abc import ABC, abstractmethod


class BaseReturnType: ...


class BaseInputType: ...


class ChildInputType(BaseInputType): ...


class ChildReturnType(BaseReturnType):
    def __init__(self) -> None:
        self.a: int = 11


class Base(ABC):
    @abstractmethod
    def create(self, inp: BaseInputType) -> BaseReturnType:
        pass


class Child(Base):
    def create(self, inp: ChildInputType) -> ChildReturnType:
        return ChildReturnType()

    # def go(self, val: int) -> None:
    #     print(val)


class Another(Base):
    def create(self, inp: ChildInputType) -> int:
        return 1

    # def go(self, val: int, name: str) -> None:
    #     print(f"{val} {name}")


cls = Child()
val = cls.create(ChildInputType())

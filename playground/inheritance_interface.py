from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def f(self, i: int, *args, **kwargs) -> object:
        pass


class B(A):
    def f(self, i: int | None) -> int:
        return 1


class C(A):
    def f(self, i: int, f: float | None) -> None:
        pass


class D(A):
    def f(self, i: int | None = None) -> None: ...


class E(A):
    def f(self, i: int | None = None) -> str:
        return "abc"


class F(A): ...


class G(A):
    def f(self) -> None:
        pass


b = B()

g = G()
g.f()

f = F()

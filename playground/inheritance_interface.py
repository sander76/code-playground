class A:
    def f(self, i: int) -> None:
        pass


class B(A):
    def f(self, i: int | None) -> None:
        pass


class C(A):
    def f(self, i: int, f: float | None) -> None:
        pass


class D(A):
    def f(self, i: int | None = None) -> None: ...


class E(A):
    def f(self, i: int | None = None) -> None:
        super().f(1)

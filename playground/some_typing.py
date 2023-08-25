class A:
    ...


class B(A):
    ...


class C:
    def __init__(self, items: list[A]) -> None:
        self.items = items


c = C([A(), B()])

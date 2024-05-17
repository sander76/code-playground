class A:
    clsvar: int = 10

    def __init_subclass__(cls, /, clsvar) -> None:
        cls.clsvar = clsvar
        super().__init_subclass__()


class B(A, clsvar=20):
    def __init__(self) -> None:
        print(self.clsvar)


b = B()

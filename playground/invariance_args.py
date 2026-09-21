class Base:
    def go(self, value: int | str) -> int | None:
        return int(value)


class Child(Base):
    def go(self, value: str) -> int | None:
        return 2 * int(value)


class MyObj: ...


class MyChildObj: ...


class WithObj:
    def go(self, value: MyObj) -> int:
        raise NotImplementedError()


class ChildWithObj(WithObj):
    def go(self, value: MyChildObj) -> int:
        raise NotImplementedError()

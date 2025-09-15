class Base:
    some_value: int = 10

    @classmethod
    def go(cls):
        return cls.some_value * 2


class Main(Base):
    some_value: int = 20


print(Main.go())

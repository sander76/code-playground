from dataclasses import dataclass


@dataclass
class MyClass:
    a: int = 1

    def add(self, value: int):
        self.a += value
        return self

    def go(self):
        print(self.a)


_cls = MyClass()
_cls.add(10).go()

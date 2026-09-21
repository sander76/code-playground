from typing import Protocol

class HasSomething(Protocol):
    def go(self)->int:...


class TakesProtocol:
    def __init__(self,haver:HasSomething):
        self._haver=haver

    def go(self)->int:
        return self._haver.go()

class AlsoHasSomething:
    """something"""

    def go(self)->int:
        return 10

class ThisOneToo:
    def go(self)->int:
        return 12


class NarrowedDown(TakesProtocol):
    def __init__(self,haver:AlsoHasSomething|ThisOneToo):
        super().__init__(haver)



cls = NarrowedDown(haver=AlsoHasSomething())

print(cls.go())


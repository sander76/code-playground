from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar, Unpack, cast

T = TypeVar("T")


@dataclass
class Unified(Generic[T]): ...


class Container:
    def __init__(self, my_class: type[MyClass]) -> None:
        class Caster(MyClass):
            def __init__(self, *args: int) -> None:
                cast(str, args)

                super().__init__(*args)

        self._my_class = my_class
        self.caster = Caster


cont = Container(MyClass)

cont.caster.my_val

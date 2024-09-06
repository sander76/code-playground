import pickle
from functools import singledispatch
from typing import Callable


class MyClass:
    def __init__(self, lower: float | None) -> None:
        self.lower = lower
        self._callable = self.set_lower(lower)

    def set_lower(self, lower_boundary: float | None) -> Callable[[float], float]:
        # usage of lambdas as return callables will fail the pickle call.
        if lower_boundary is None:
            return self._just_lower
        return self._lower_from_float

    def _just_lower(self, value) -> float:
        return value

    def _lower_from_float(self, value) -> float:
        return max(self.lower, value)

    def __call__(self, value: float):
        return self._callable(value)


class MyMainObject:
    def __init__(self, value: float, modifiers: list[Callable[[float], float]]) -> None:
        self._value = value
        self._modifiers = modifiers

    def get_value(self) -> float:
        value = self._value
        for modifier in self._modifiers:
            value = modifier(value)
        return value


modifier = MyClass(lower=1)
main_obj = MyMainObject(10, [modifier])

print(main_obj.get_value())

pkl = pickle.dumps(main_obj)
unpkl = pickle.loads(pkl)

print(unpkl.get_value())

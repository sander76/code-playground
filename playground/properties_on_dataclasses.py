from dataclasses import InitVar, dataclass, field


@dataclass(frozen=True)
class Vehicle:
    wheels: InitVar[int | None]
    _wheels: int | None = field(init=False, repr=True)

    def __post_init__(self, wheels: int | None):
        object.__setattr__(self, "_wheels", wheels)

    @property
    def wheels(self) -> int:
        if self._wheels is None:
            raise ValueError("Wheels cannot be none.")
        return self._wheels


veh1 = Vehicle(wheels=10)
print(veh1.wheels)
print(veh1)

veh2 = Vehicle(wheels=None)
# print(veh2.wheels) # this will raise as wheels is None.

# veh2.wheels = 10 # also fails due to being frozen.

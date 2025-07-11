from typing import TYPE_CHECKING, Generic

if TYPE_CHECKING:
    from typing_extensions import TypeVar

SimResultT = TypeVar("SimResultT")
ReturnTypeT = TypeVar("ReturnTypeT", default=str)


class Simulation(Generic[ReturnTypeT]):
    def simulate(self) -> ReturnTypeT: ...


sim = Simulation()
res = sim.simulate()

other_sim = Simulation[int]()
other_res = other_sim.simulate()

from __future__ import annotations

from collections import UserDict, UserList
from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Generic, Iterable, Protocol, TypeAlias, TypeVar, override

# Goal:
# - have typed results from a simulate or simulate_once call.
# - have a straightforward way of defining the simulation.
# - hide as much boilerplate as possible while still having all functionality.


#####
# Option 1: Protocol for inferring type of generic.
#####

T = TypeVar("T", covariant=True)
K = TypeVar("K", covariant=True)


class ResourceWithSimulateCall(Protocol[T, K]):
    """Protocol used to define the type of the Engine return types based on the return type of the
    run call inside this protocol."""

    def sim_result(self, results: Iterable[T]) -> K:
        pass

    def simulate(self) -> T:
        pass


# For simplicity I've not included a model class inside this example as I am assuming we have merged
# the Engine and Model into one class. (and maybe rename it to `Simulation` so we can rename
# the methods `simulate` and `simulate_once` to `run` and `run_once` ?)
class Simulation(Generic[T, K]):
    # A generic engine class containing the `simulate_once` and `simulate` calls.

    # the `root_resource` is a protocol with a run call which has a generic as return type
    # type checkers are able to infer the type of Engine class, and its return types of the simulate and
    # simulate_once calls.)
    def __init__(self, root_resource: ResourceWithSimulateCall[T, K]):
        self._simulate_call = root_resource

    def run_once(self) -> T:
        """Perform a simulation once."""
        return self._simulate_call.simulate()

    def run(self, n_simulations: int) -> K:
        """Perform a simulation multiple times."""
        results = [self._simulate_call.simulate()]
        return self._simulate_call.sim_result(results)


@dataclass
class Resource:
    """Our base resource class."""

    def sim_result(self) -> Any:
        raise NotImplementedError

    def simulate(self) -> Any:
        raise NotImplementedError


# The above will live in coral-sim.
# below the code to run a simulation.


# Define the root resource object implementing the simulation logic tying the different resource inputs and outputs
# together.
@dataclass
class MyResource(Resource):
    # other (child) resources here.
    @dataclass
    class Result:
        prices: str

    @override
    def simulate(self) -> MyResource.Result:
        # the return type of this call determines the return type of the return types of the `simulate` and
        # `simulate_once` calls of the engine object.
        return MyResource.Result(prices="abc")

    @override
    def sim_result(self, results: Iterable[T]) -> list[MyResource.Result]:
        return [MyResource.Result(prices="def")]


my_resource = MyResource()

my_engine = Simulation(my_resource)

single_result = my_engine.run_once()  # --> type is str
multiple_results = my_engine.run(1)  # --> type is list[str]

first = multiple_results[0].prices


## does this also work with a dataclass


@dataclass
class SimulationDC(Generic[T, K]):
    # A generic engine class containing the `simulate_once` and `simulate` calls.

    # the `root_resource` is a protocol with a run call which has a generic as return type
    # type checkers are able to infer the type of Engine class, and its return types of the simulate and
    # simulate_once calls.)
    resource_with_simulate_call: ResourceWithSimulateCall[T, K]

    def run_once(self) -> T:
        """Perform a simulation once."""
        return self.resource_with_simulate_call.simulate()

    @property
    def rn(self) -> T:
        return self.resource_with_simulate_call.simulate()

    def run(self, n_simulations: int) -> K:
        """Perform a simulation multiple times."""
        results = [self.resource_with_simulate_call.simulate()]
        return self.resource_with_simulate_call.sim_result(results)


res = MyResource()
sr = SimulationDC(resource_with_simulate_call=res)

res_sr = sr.run_once()
res_all = sr.run()

rn = sr.rn

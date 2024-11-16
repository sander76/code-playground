from dataclasses import dataclass
from typing import Generic, TypeVar


@dataclass
class InputData:
    val: int


@dataclass
class OutpData:
    val: int


inp = TypeVar("inp")
out = TypeVar("out")


class Producer(Generic(inp, out)):
    def produce(self, inp) -> out:
        pass


class Params:
    def make_producer(self):
        return Producer()

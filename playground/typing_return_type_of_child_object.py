from ast import TypeAlias
from dataclasses import dataclass


@dataclass
class Result:
    x: int


@dataclass
class OtherResult:
    y: int


class Producer:
    def generate(self) -> Result:
        return Result(x=1)


class OtherProducer:
    def generate(self) -> OtherResult:
        return OtherResult(y=10)


class Generator:
    @property
    def producer(self) -> Producer | OtherProducer:
        return Producer()

    def generate(self) -> Result:
        return self.producer.generate()


gen = Generator()

res = gen.generate()

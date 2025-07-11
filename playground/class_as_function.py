from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel, create_model

PowerT = TypeVar("PowerT")
PowerResourceT = TypeVar("PowerResourceT")


@dataclass
class GasResource:
    spark: int

    def generate(self) -> dict:
        return {}


@dataclass
class SinglePowerResource:
    def generate(self) -> dict:
        return {}


@dataclass
class PowerGasSimulation(Generic[PowerResourceT]):
    power_resource: PowerResourceT
    gas_resource: GasResource

    @dataclass
    class PowerGasResult:
        power_price: dict
        gas_price: dict

    def simulate(self):
        return PowerGasSimulation.PowerGasResult(power_price={}, gas_price={})


class PowerGasCfg(BaseModel, Generic[PowerT, PowerResourceT]):
    spark: int
    _power_config: PowerT

    def create_resource(self) -> PowerGasSimulation[PowerResourceT]:
        gas_resource = GasResource(spark=self.spark)

        return PowerGasSimulation(power_resource)


@dataclass
class PowerSimulation(Generic[PowerResourceT]):
    @dataclass
    class PowerResult:
        power: dict

    power_resource: PowerResourceT

    def simulate(self):
        return PowerSimulation.PowerResult(power={})


class SinglePowerCfg(BaseModel):
    region: str

    @property
    def with_gas(self) -> type[PowerGasCfg[SinglePowerCfg]]:
        return create_model("spr", _power_config=(SinglePowerCfg, self), __base__=PowerGasCfg)

    def create(self) -> SinglePowerResource:
        return SinglePowerResource()


class SimulationCfg(BaseModel):
    start: int

    @property
    def with_single_power(self) -> type[SinglePowerCfg]:
        return SinglePowerCfg


cls = SimulationCfg(start=1).with_single_power(region="abc").with_gas(spark=10)
print(cls)
pcfg = cls._power_config
print(pcfg)

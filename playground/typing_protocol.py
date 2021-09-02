import logging
from typing import Protocol, Sequence, Any, Union
from dataclasses import dataclass

_LOGGER = logging.getLogger(__name__)


class Proto(Protocol):
    val: int


@dataclass
class ImplementedProtoDataclass:
    val: int


class ImplementedProto:
    def __init__(self, protonr: int):
        self.val = protonr


@dataclass
class FailedImplement:
    value: int


def proto_runner(_protos: Sequence[Proto]) -> None:
    for proto in _protos:
        print(proto.val)


if __name__ == "__main__":
    protos: list[Proto] = [ImplementedProtoDataclass(4)]
    proto_runner(protos)

    new_protos: list[Proto] = [
        ImplementedProtoDataclass(2),
        FailedImplement(2),
    ]  # this should fail. Last item does not comply with the Protocol.
    proto_runner(new_protos)

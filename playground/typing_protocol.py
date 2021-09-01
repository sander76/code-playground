import logging
from typing import Protocol, Sequence, Any, Union
from dataclasses import dataclass

_LOGGER = logging.getLogger(__name__)


class Proto(Protocol):
    val: Any


@dataclass
class ImplementedProtoDataclass:
    val: int


class ImplementedProto:
    def __init__(self, protonr: int):
        self.val = str(protonr)


def proto_runner(_protos: Sequence[Proto]) -> None:
    for proto in _protos:
        print(proto.val)


if __name__ == "__main__":
    protos = [ImplementedProtoDataclass(4)]

    proto_runner(protos)

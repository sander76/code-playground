from dataclasses import dataclass
from typing import Generic, TypeVar


class HasResource1:
    def go(self) -> str: ...


class HasResource2:
    def go(self) -> int: ...


T = TypeVar("T", HasResource1, HasResource2)


@dataclass
class WithResource(Generic[T]):
    config: T


my_resource = WithResource(config=HasResource1())

my_resource.config

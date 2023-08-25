from typing import List, Sequence, TypeVar
from pydantic import BaseModel, BaseSettings


class UP(BaseModel):
    ...


class MUP(UP):
    ...


class EC(BaseModel):
    up: Sequence[UP]


class MEP(EC):
    up: Sequence[BaseModel]


class Item(BaseSettings):
    value: int


class Collector(BaseSettings):
    __root__: List[Item] = []

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]


collector = Collector()

collector.__root__.append(Item(value=10))

print(collector.json(indent=4))

print("enumeratiing:")
for itm in collector:
    print(itm)

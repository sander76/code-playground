from deepdiff import DeepHash
from pydantic import BaseModel


class Hashable(BaseModel):
    a: int
    b: str
    c: list[str]

    # class Config:

    #     allow_mutation = False
    #     frozen = True


class SomeObj:
    def __init__(self, b: list[dict]) -> None:
        self.x: int = 1
        self.b: list[dict] = b

    def __eq__(self, __o: object) -> bool:
        if not type(self) is type(__o):
            return False
        org = frozenset((obj["a"] for obj in self.b))
        other = frozenset(((obj["a"] for obj in __o.b)))

        return org == other

    def __hash__(self) -> int:
        hash_x = hash(self.x)
        hash_b = hash(frozenset((obj["a"] for obj in self.b)))
        return hash_x ^ hash_b


a = SomeObj(b=[{"a": 10}, {"a": 11}, {"a": 15}])
b = SomeObj(b=[{"a": 11}, {"a": 10}, {"a": 15}])

print(a == b)

dict = {}

# should result in a dict with len==1 as both objects have the same hash.
dict[a] = 10
dict[b] = 11

print(dict)

pydantic_hashable_1 = Hashable(a=10, b="abc", c=["j", "k"])
pydantic_hashable_2 = Hashable(a=10, b="abc", c=["k", "j"])

print(f"identical: {pydantic_hashable_2 == pydantic_hashable_1}")


# dct_1 = pydantic_hashable_1.dict()
# dct_2 = pydantic_hashable_2.dict()

hash_1 = DeepHash(pydantic_hashable_1, apply_hash=False)
hash_2 = DeepHash(pydantic_hashable_1)


print(hash_1 == hash_2)

items = [pydantic_hashable_1, pydantic_hashable_2]

# print(pydantic_hashable_1.copy(deep=True) in items)

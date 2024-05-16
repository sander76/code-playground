from collections import defaultdict
from typing import TypedDict


class MyDCT(TypedDict):
    a: int


MYDCT: MyDCT = defaultdict(int)

MYDCT["a"] = MYDCT["a"] + 1

print(MYDCT["a"])

MYDCT = defaultdict(int)
print(MYDCT["a"])

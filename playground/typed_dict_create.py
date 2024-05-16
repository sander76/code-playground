from collections import defaultdict
from typing import Self, TypedDict, get_args, get_type_hints


class MyDCT(TypedDict):
    a: int

    @classmethod
    def create(cls) -> Self:
        args = get_type_hints(cls)

        _instance = cls(**{_key: 0 for _key in args.keys()})
        return _instance


dct = MyDCT.create()
print(dct)

dct["a"] = dct["a"] + 1

print(dct)

from typing import Literal, overload, reveal_type


@overload
def go(val: int, key_type: type[str]) -> str: ...


@overload
def go(val: int, key_type: type[int]) -> int: ...


def go(val: int, key_type: type[str] | type[int]) -> int | str:
    if key_type is str:
        return str(val * 2)
    else:
        return val * 2


a = go(10, key_type=str)
b = go(10, key_type=int)

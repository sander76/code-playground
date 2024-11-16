from typing import Mapping, TypedDict, TypeVar

RetVal = TypeVar("RetVal", bound=Mapping[str, int])


def go(inp: RetVal) -> RetVal:
    return inp


class MyDict(TypedDict):
    val: int


res = go(MyDict(val=1))

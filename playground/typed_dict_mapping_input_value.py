from typing import Any, Mapping, TypedDict

MyDict = TypedDict("MyDict", {"a": int})


def go(val: Mapping[str, Any]) -> int:
    return val["a"]


val = go(MyDict(a=1))
other = go({"a": 10})

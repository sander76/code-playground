from typing import TypedDict

from pydantic import TypeAdapter


class MyDict(TypedDict):
    a: int


c = {"a": "1"}
b = MyDict(c)
print(b)

m = TypeAdapter(MyDict)
m.validate_python(c, strict=True)

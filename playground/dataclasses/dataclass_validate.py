from dataclasses import dataclass

from beartype import beartype, door
from pydantic import TypeAdapter


@beartype
@dataclass
class MyCls:
    val: int


cls_1 = MyCls(val="abc")
print(cls_1)


ta = TypeAdapter(MyCls)
ta.validate_python(cls_1)

door.die_if_unbearable(cls_1, MyCls)

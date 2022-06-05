from typing import Optional
import pydantic


class Model(pydantic.BaseModel):
    a_value: Optional[int] = None


class Parent(pydantic.BaseModel):
    value: int
    child: Model
    other_child: list[Model] = []


a = Model(a_value=10)

b = Model()
b.a_value = "rubbish"  # <-- this does not raise an error!


# the above is fairly obvious, but the errors can be more subtle.

parent = Parent(value=10, child=b)

parent.other_child.append(a)
parent.other_child.append("nonsens")  # <-- This does not raise an error either.

from functools import cached_property

from pydantic import BaseModel


class MyModel(BaseModel):
    myval: int

    @cached_property
    def mul(self):
        return self.myval * 3


model = MyModel(myval=10)

print(model.mul)
print(model.mul)
model.myval = 3
print(model.mul)
print(model.mul)

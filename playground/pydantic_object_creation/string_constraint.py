from typing import Annotated
from pydantic import BaseModel, StringConstraints


class MyModel(BaseModel):
    values: Annotated[
        str | None, StringConstraints(strip_whitespace=True, min_length=1)
    ] = None


model = MyModel()
print(model)

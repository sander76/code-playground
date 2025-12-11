from typing import Annotated

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(validate_by_alias=True)

    _my_val: Annotated[int, Field(validation_alias="my_val")]


mdl = MyModel(my_val="1")
print(mdl)

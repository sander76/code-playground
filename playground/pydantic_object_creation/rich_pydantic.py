from typing import Annotated

# from rich import print
import annotated_types
from pydantic import BaseModel


class ModelWithPydanticErorr(BaseModel):
    my_value: Annotated[int, annotated_types.Gt(0)]


try:
    model = ModelWithPydanticErorr(my_value=-10)
except Exception as err:
    print(err)

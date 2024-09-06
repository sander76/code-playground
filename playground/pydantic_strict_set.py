from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, Strict


class MyModel(BaseModel):
    model_config = ConfigDict(strict=False)
    a: Annotated[set[str], Strict()]


mdl = MyModel.model_validate_json('{"a":["a","b"]}')
print(mdl)

mdl = MyModel.model_validate({"a": ["a", "b"]})
print(mdl)

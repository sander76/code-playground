from typing import Any

from pydantic import BaseModel, model_validator


class MyModel(BaseModel):
    val1: int
    val2: int

    @model_validator(mode="before")
    @classmethod
    def checkval2(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "val2" not in data:
                data["val2"] = 10
        return data


mdl = MyModel(val1=10)

print(mdl)

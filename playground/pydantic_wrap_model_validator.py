from typing import Any, Self

from pydantic import BaseModel, ConfigDict, ModelWrapValidatorHandler, model_validator


class UserModel(BaseModel):
    username: str

    model_config = ConfigDict(frozen=True)

    @model_validator(mode="wrap")
    @classmethod
    def evaluate_username(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        val = handler(data)
        if val.username == "no_name":
            return handler(val.model_dump() | {"username": "no idea"})
        return val


mdl = UserModel(username="no_name")
print(mdl.username)

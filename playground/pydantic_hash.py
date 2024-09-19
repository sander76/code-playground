import hashlib

from deepdiff import DeepHash
from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    items: list[int] = []

    value: str


mdl = MyModel(items=[1, 2, 3], value="myval")


hash = hash(mdl)

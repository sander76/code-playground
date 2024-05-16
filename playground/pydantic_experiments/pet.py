import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel


class Dog(BaseModel):
    pet_type: Literal["dog"]


json.dump(Dog.model_json_schema(), Path("dog.json").open(mode="w", encoding="utf-8"))

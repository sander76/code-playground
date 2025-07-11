from typing import Literal

from pydantic import BaseModel, Field, create_model


class Bm(BaseModel):
    value: str

    def __call__(self):
        print(f"value={self.value!r}")

    @classmethod
    def with_new_annotation(cls):
        return create_model("copied", value=(Literal["abc", "def"], ...), __base__=Bm)


def make_model():
    return create_model("copied", value=(Literal["abc", "def"], ...), __base__=Bm)


# make_model()(value="defg")()
new_model = Bm.with_new_annotation()
new_model(value="abcd")()

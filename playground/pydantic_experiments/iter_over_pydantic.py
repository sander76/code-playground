from pydantic import BaseModel


class Model(BaseModel):
    a: int = 10


class Model1(BaseModel):
    model: Model = Model()
    c: str = "abc"


model = Model1()

print(model.dict())


def go_over_pydantic(model: BaseModel):
    for key, value in model:
        print(f"{key=}, {value=}")
        if isinstance(value, BaseModel):
            go_over_pydantic(value)


go_over_pydantic(model)

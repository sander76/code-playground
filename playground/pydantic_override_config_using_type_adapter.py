from pydantic import BaseModel, ConfigDict, TypeAdapter


class MyModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    value: int


data = {"value": 10, "val": 20}

# this fail. due to extra='forbid'
# mdl = MyModel.model_validate(data)


class PermissiveModel(MyModel):
    model_config = ConfigDict(frozen=True, extra="ignore")


mdl = MyModel.model_validate(PermissiveModel.model_validate(data).model_dump())
print(mdl)

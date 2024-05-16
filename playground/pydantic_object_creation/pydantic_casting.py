from pydantic import BaseModel


class MyModel(BaseModel):
    debug: bool


model = MyModel.model_validate({"debug": "true"})
print(model)

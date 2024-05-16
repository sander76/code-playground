import pickle
from pathlib import Path

from pydantic import BaseModel

# define a model in pydantic
# pickle and save it to file.
# comment the actual model (class MyModel)
# observe loading of the pickled file fails.


# class MyModel(BaseModel):
#     value: int


class MyModel(BaseModel):
    value: int
    proceed: bool


# model = MyModel(value=10)

pickled_file = Path("pickled")
# pickle.dump(model, Path("pickled").open(mode="wb"))
print(pickled_file.open(mode="rb").read())

result = pickle.load(pickled_file.open("rb"))
print(result)
print(result.model_dump_json())

print(isinstance(result, MyModel))
print(result.proceed)

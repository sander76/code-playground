from pydantic import BaseModel


class MyModel(BaseModel):
    val: int

    @property
    def other_val(self) -> bool:
        return False


class Child(MyModel):
    other_val: bool


mdl = MyModel(val=10)
print(mdl)

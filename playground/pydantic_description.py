from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)

    some_val: int
    """Does this end up in the description?"""  # <== yes


print(MyModel.model_fields["some_val"].description)

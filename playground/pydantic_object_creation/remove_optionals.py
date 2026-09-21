from pydantic import BaseModel

from typing import Annotated

from pydantic import Field, create_model


class MyModel(BaseModel):
    val: int | None = None


def make_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
    new_fields = {}

    for f_name, f_info in model_cls.model_fields.items():
        f_dct = f_info.asdict()

        f_dct["attributes"].pop("default", None)
        f_dct["attributes"].pop("default_factory", None)
        new_fields[f_name] = Annotated[
            f_dct["annotation"],
            *f_dct["metadata"],
            Field(**f_dct["attributes"]),
        ]

    return create_model(
        f"{model_cls.__name__}Optional",
        __base__=model_cls,
        **new_fields,
    )


mdl = MyModel(val=10)
print(mdl)

Mdl = make_fields_optional(MyModel)

print(Mdl())

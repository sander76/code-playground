from typing import Annotated, Any, TypeVar

import pydantic
from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    WrapSerializer,
    WrapValidator,
)
from pydantic.types import HashableItemType


def extended_set(
    item_type: type[HashableItemType],
    raise_on_validate: bool = False,
    dump_to_list: bool = False,
) -> type[set[HashableItemType]]:
    """Return a set type with additional functionality.

    ```python
    from pydantic import BaseModel

    class MyModel(BaseModel):
        my_set: extended_set(str, raise_on_validate=True)
    ```

    Args:
        item_type: _description_
        raise_on_validate: _description_
        dump_to_list: _description_

    Returns:
        _description_
    """

    def check_unique(
        v: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
    ) -> Any:
        if isinstance(v, set):
            return handler(v)

        result = handler(v)
        if len(v) != len(result):
            raise ValueError(f"Provided values for {info.field_name}")

        return result

    def to_list(v: Any, handler: Any, info: Any) -> Any:
        dta = [handler(_v) for _v in v]
        return dta

    args: list[Any] = []
    if raise_on_validate:
        args.append(WrapValidator(check_unique))
    if dump_to_list:
        args.append(WrapSerializer(to_list))

    RaisingSet = Annotated[set[item_type], *args]
    return RaisingSet


class HashThingie(BaseModel):
    model_config = ConfigDict(frozen=True)

    value: int


class Model(BaseModel):
    # myset: extended_set(str, raise_on_validate=True, dump_to_list=True)
    myset: extended_set(HashThingie, raise_on_validate=True, dump_to_list=True)
    another: extended_set(dict, raise_on_validate=True)


# mdl = Model(myset={"a"})
# assert mdl == Model(myset={"a"})

# mdl = Model(myset=["a", "a"])

mdl = Model(myset=[HashThingie(value=10)])
print(mdl)

print(mdl.model_dump())

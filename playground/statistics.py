from dataclasses import dataclass, fields
from typing import Any, Self, TypeVar, cast


@dataclass
class ValueObj:
    val_1: int

    def as_str(self) -> Self:
        return cast(Self, _GetFields(attr_fields=self))


class Statistics:
    def __init__(self):
        pass


@dataclass(frozen=True)
class _GetFields:
    attr_fields: object

    def __getattr__(self, item: str) -> Any:
        field_names = [field.name for field in fields(self.attr_fields)]
        if item in field_names:
            return item
        return getattr(self, item)


TModel = TypeVar("TModel", bound=dataclass)


def as_string(model: TModel) -> TModel:
    return cast(TModel, _GetFields(attr_fields=model))


str_field = as_string(ValueObj).val_1
print(str_field)
# print(fields(ValueObj))

my_ojb = ValueObj(val_1=1)

print(my_ojb.as_str().val_1)

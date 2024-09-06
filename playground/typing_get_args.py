import inspect
from dataclasses import dataclass
from typing import Annotated, Union, get_args, get_type_hints


@dataclass(frozen=True)
class MyClass:
    b: Annotated[Union[str, int], "abc"]
    """Some docstring"""

    c: str | int
    a: Annotated[str | int, "abc"] = 10
    d: tuple[int, ...] = ()


class MyNormalClass:
    b: Annotated[Union[str, int], "abc"]
    c: str | int
    a: Annotated[str | int, "abc"] = 10


def inspect_hints(the_class: type[object]):
    print(f"\n\n### inspecting {the_class}")
    for key, type_hints in get_type_hints(MyClass).items():
        print(f"{key=} {get_args(type_hints)}")

    for key, type_hints in inspect.get_annotations(the_class).items():
        print(f"{key}: {getattr(type_hints,'__metadata__','no_metadata')}")


inspect_hints(MyClass)
inspect_hints(MyNormalClass)

cls = MyClass

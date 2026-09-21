import inspect
from pprint import pprint

from typing_extensions import Final

_DEFAULT_VARS = ("region", "regions")
_DEFAULT_CLASSES = ("MyObj",)


class MyExc(Exception):
    def __init__(self, message: str):
        self._args_from_stack = []
        super().__init__(message)

        self._mesage = message
        stck = inspect.stack()

        for idx, frame_info in enumerate(stck):
            local = frame_info.frame.f_locals
            pprint(local)
            if "self" in local:
                try:
                    obj_name = local["self"].__class__.__name__
                except AttributeError:
                    # just not in there.
                    continue
                else:
                    if obj_name in _DEFAULT_CLASSES:
                        self._args_from_stack.append({"class": obj_name})
            else:
                for var in _DEFAULT_VARS:
                    if var in local:
                        self._args_from_stack.append({var: local[var]})

    def __str__(self) -> str:
        return f"{self._mesage}, vars={self._args_from_stack}"


def call_2():
    raise MyExc("something is wrong")


def call_1(regions: list[str]):
    for region in regions:
        # call_2()
        obj = MyObj()


class MyObj:
    def __init__(self):
        call_2()


class WithTraceObj:
    ADD_TO_STACK_TRACE: Final[bool] = True


if __name__ == "__main__":
    call_1(regions=["NL", "BE"])

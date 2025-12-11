from functools import wraps
from typing import Callable, ParamSpec, Sequence, TypeVar, overload

P = ParamSpec("P")
R = TypeVar("R")


@overload
def rec(wrapped_func: Callable[P, R] = ..., *, ignore: None = ...) -> Callable[P, R]: ...


@overload
def rec(wrapped_func: None = ..., *, ignore: Sequence[str] = ...) -> Callable[[Callable[P, R]], Callable[P, R]]: ...


def rec(
    wrapped_func: Callable[P, R] | None = None, *, ignore: Sequence[str] | None = None
) -> Callable[[Callable[P, R]], Callable[P, R]] | Callable[P, R]:
    keys_to_be_removed = set(ignore) if ignore else set()

    def _rec(func: Callable[P, R]) -> Callable[P, R]:
        """Decorate a function which returns a value which is to be recorded."""

        @wraps(func)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for key in keys_to_be_removed:
                kwargs.pop(key)
            result = func(*args, **kwargs)

            return result

        return _wrapper

    if wrapped_func:
        return _rec(wrapped_func)

    return _rec


@rec(ignore=["val"])
def go(**kwargs: int) -> dict[str, int]:
    return kwargs


# @rec("some name")
# def another_go(val: int, op: str) -> tuple[int, str]:
#     return val * 10, op


val = go(val=10, val_1=20)

print(val)


@rec
def another_go(**kwargs: int) -> dict[str, int]:
    return kwargs


val = another_go(val=10, val_1=20)
print(val)

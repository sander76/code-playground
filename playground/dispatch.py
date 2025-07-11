from functools import singledispatch


@singledispatch
def evaluate(values: tuple[int, int] | int) -> tuple[int, int] | int:
    return values


@evaluate.register
def _(values: int) -> int:
    return values


@evaluate.register
def _(values: tuple[int, int]) -> tuple[int, int]:
    return values


vals = evaluate(1)

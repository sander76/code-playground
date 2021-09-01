"""
Many times I partially type annotate a function.
To prevent this use --disallow-incomplete-defs in mypy.
"""


def go(value1: int, value2: str) -> str:
    # remove one of the above type annotations and you'll see
    # a mypy error popping up.
    return f"{value1} {value2}"


go(1, "a")

from functools import wraps


def org_renderer():
    """The org docstring"""
    return 10


@wraps(org_renderer)
def new_renderer():
    return org_renderer()


print(new_renderer.__doc__)

import typing


class RequiredProps(typing.TypedDict):
    # all of these must be present
    a: int
    b: str


class OptionalProps(typing.TypedDict, total=False):
    # these can be included or they can be omitted
    c: int
    d: int


class ReqAndOptional(RequiredProps, OptionalProps):
    pass


def hi(req_and_optional: ReqAndOptional) -> None:
    print(req_and_optional)


hi(10, 20, c=10)

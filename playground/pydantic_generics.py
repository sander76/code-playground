# from typing_extensions import reveal_type
from pydantic import BaseModel
from pydantic.generics import GenericModel

from typing import Generic, TypeVar, Type


class BaseResponse(BaseModel):
    ...


class BaseParameters(BaseModel):
    ...


ResponseType = TypeVar("ResponseType", bound=BaseResponse)
ParametersType = TypeVar("ParametersType", bound=BaseParameters)


class Base(GenericModel, Generic[ResponseType, ParametersType]):
    response: ResponseType
    parameters: ParametersType


class Response(BaseResponse):
    value: int


class Parameters(BaseParameters):
    values: str


class GidcJob(Base[Response, Parameters]):

    resp: str = ""


a_job = GidcJob(reponse=Response(value=10), parameters=Parameters(values="123"))

a_job.response
a_job.parameters
reveal_type(a_job.response)

T = TypeVar("T", bound=object)


def foo(cls: type[T]) -> T:
    if cls is str:
        return cls("abc")
    raise TypeError()


a = foo(str)

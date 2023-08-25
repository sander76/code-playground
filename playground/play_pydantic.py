from pydantic import AnyUrl

# from pydantic import BaseModel, Field


# class SomeModel(BaseModel):
#     identifiedObject: str = Field("a value", alias="identified_object")


# model = SomeModel()

# print(model)


def go(url: AnyUrl) -> str:
    return url.host


go("http://localhost/v1/api")

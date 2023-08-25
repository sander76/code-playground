from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, SecretStr


class MyModel(BaseSettings):
    base: AnyHttpUrl
    path: str
    data: SecretStr


model = MyModel(base="http://localhost", path="some_path", data="mysecret")

print(model)

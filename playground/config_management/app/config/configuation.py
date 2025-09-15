from functools import cache

from pydantic_settings import BaseSettings


class MySettings(BaseSettings):
    setting1: int
    setting2: str


@cache
def get_settings() -> MySettings:
    return MySettings(setting1=1, setting2="abc")

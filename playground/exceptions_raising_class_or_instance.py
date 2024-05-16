class MyException(Exception):
    def __init__(self, value: int) -> None:
        super().__init__(f"my exception with a message. {value=!r}")


def go() -> None:
    # change this from `MyException` to `MyException(10)` and observe the difference.
    raise MyException


try:
    go()
except MyException as err:
    print(err)

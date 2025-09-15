from typing import Literal

MY_UNITS = Literal["W", "MW", "kW"]


def go(args: MY_UNITS | str) -> None: ...

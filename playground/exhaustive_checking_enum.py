#  https://hakibenita.com/python-mypy-exhaustive-checking
from __future__ import annotations

from typing import NoReturn
import enum


def assert_never(value: NoReturn) -> NoReturn:
    assert False, f"Unhandled value: {value} ({type(value).__name__})"


class OrderStatus(enum.Enum):
    Ready = "ready"
    # Scheduled = "scheduled" # check or uncheck this item to see mypy in action (failing at the assert_never function)
    Shipped = "shipped"


def handle_order(status: OrderStatus) -> str:
    """handle the order based on order status."""

    #  Only two out of three enums are evaluated. Scheduled is missing.
    #  Mypy indicates an error in the `assert_never` function.

    if status is OrderStatus.Ready:
        return "ship order"

    elif status is OrderStatus.Shipped:
        return "shipped"
    # elif status is OrderStatus.Scheduled:
    #     return "ready"
    else:
        assert_never(status)

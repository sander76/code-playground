# enum check all types
from __future__ import annotations

import enum

from typing_extensions import assert_never


class OrderStatus(enum.Enum):
    Ready = "ready"
    Scheduled = "scheduled"  # check or uncheck this item to see mypy in action (failing at the assert_never function)
    Shipped = "shipped"


def handle_order(status: OrderStatus) -> str:
    """handle the order based on order status."""

    #  Only two out of three enums are evaluated. Scheduled is missing.
    #  Mypy indicates an error in the `assert_never` function.

    if status == OrderStatus.Ready:
        return "ship order"

    if status == OrderStatus.Shipped:
        return "shipped"
    assert_never(status)


def handle(status: OrderStatus) -> str:
    match status:
        case OrderStatus.Ready:
            return "ready"
        case OrderStatus.Shipped:
            return "shipped"
        case _:
            assert_never(status)  # this raises mypy issue


handle_order()

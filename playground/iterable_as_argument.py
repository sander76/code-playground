"""Implement a class which implements the iterator dunder method.

Mypy should not complain.
"""

from typing import Iterable, Iterator


class SomeClass:
    def __init__(self, data: list[int]) -> None:
        self.data = data

    def __iter__(self) -> Iterator[int]:
        for itm in self.data:
            yield itm


cls = SomeClass([1, 2, 3])


def do_stuff(source: Iterable[int]) -> None:
    """Do stuff."""
    for itm in source:
        print(itm)


do_stuff(cls)
do_stuff([1, 2, 3])

do_stuff({1, 2, 3})
do_stuff({1: 1}.keys())

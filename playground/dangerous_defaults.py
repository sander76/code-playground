from typing import Any


class A:
    def __init__(self) -> None:
        self.collection: list[Any] = []


def do_stuff_with_a(a=A()):
    a.collection.append(10)
    return a


result = do_stuff_with_a()
print(result.collection)

other_result = do_stuff_with_a()
# print(other_result.collection)

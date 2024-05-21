from timeit import timeit


class WithSlots:
    __slots__ = ["a", "b"]

    def __init__(self) -> None:
        self.a = 10000
        self.b = {"val": 1000}


with_slots = WithSlots()
slotted_dict = with_slots.b

a_dict = {"a": 10000}


print(timeit('a_dict["a"]', globals=globals()))
print(timeit("with_slots.a", globals=globals()))
print(timeit("slotted_dict['val']", globals=globals()))

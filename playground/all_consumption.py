a = [True, False, True]


def truthy(vals: list[bool]):
    for val in vals:
        print(val)
        yield val


truths = all(truthy(a))

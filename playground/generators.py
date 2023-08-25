def inner():
    inner_result = yield 2
    print("inner", inner_result)
    return 3


def outer():
    yield 1
    val = yield from inner()
    print("outer", val)
    yield 4


gen = outer()
print(next(gen))
print(next(gen))
print(next(gen))

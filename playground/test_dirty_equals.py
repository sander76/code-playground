from dirty_equals import IsPartialDict, IsPositiveInt

a = {"a": 10, "b": {"c": 5, "d": 3}}

# def test_something():
#     assert a == IsPartialDict({"a":100})

# def test_other():
#     assert -1 == IsPositiveInt()

def test_nested():
    dct = {'a':10,'b':-12}

    assert dct == dct | {'b':IsPositiveInt()}
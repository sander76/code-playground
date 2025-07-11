dct_1 = {"a": 1}
dct_2 = {"a": 1}

print(dct_1 == dct_2)


class MyObj:
    def __init__(self, value: int):
        self.value = value


dct_1 = {"a": MyObj(value=1)}
dct_2 = {"a": MyObj(value=1)}

print(dct_1 == dct_2)

print(dct_1 == {"a": dct_1["a"]})


class CustomEq:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


# we're now using the custom __eq__ method.
print({"a": CustomEq(value=1)} == {"a": CustomEq(value=1)})


class NoEq:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, value):
        raise NotImplementedError


# this raises because __eq__ raises.
# print({"a": NoEq(value=1)} == {"a": NoEq(value=1)})

# this doesn't
no_eq = NoEq(value=1)
print({"a": no_eq} == {"a": no_eq})

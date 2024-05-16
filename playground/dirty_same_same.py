from dirty_equals import IsPartialDict

a = {"a": 10, "b": {"c": 5, "d": 3}}

print(a == IsPartialDict({"a": 10}))
print(a == IsPartialDict({"b": IsPartialDict({"c": 5})}))
print(a == IsPartialDict({"b": IsPartialDict({"d": 3})}))


def is_sub_set(expected: dict, actual: dict) -> bool:
    for k, v in expected.items():
        if k not in actual:
            return False
        if isinstance(v, dict):
            if not isinstance(actual[k], dict) or not is_sub_set(v, actual[k]):
                return False
        elif actual[k] != v:
            return False
    return True


print(is_sub_set({"b": {"c": 5}}, a))

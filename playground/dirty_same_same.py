from dirty_equals import IsPartialDict

a = {"a": 10, "b": {"c": 5, "d": 3}}

print(a == IsPartialDict({"a": 10}))
print(a == IsPartialDict({"b": IsPartialDict({"c": 5})}))
print(a == IsPartialDict({"b": IsPartialDict({"d": 3})}))

assert a == IsPartialDict({"a":100})
import jmespath
from glom import assign

a = {"a": {"value": 1}, "b": {"value": 2}}


_ = assign(a, "*.value", 4)
print(a)

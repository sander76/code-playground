import hashlib
import pickle
from dataclasses import dataclass, field, fields


@dataclass(frozen=True)
class MyClass:
    name: str
    items: list = field(default_factory=lambda: [""])


inst = MyClass(name="abc")

for field in fields(inst):
    print(field.name)
    print(getattr(inst, field.name))

pickle.dumps(inst)

print(hashlib.sha256(pickle.dumps(inst)).digest())


# inst.items.append("abc")

# print(hash(inst))

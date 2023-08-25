from rich.text import Text
from rich import print
import json
from rich.json import JSON

t1 = Text("Problem", "red")

t1.append(Text("just a message"))

# print(t1)

t2 = Text("More problems", "red")
# print(f"{t2} some more")
# print(t2)

# t3 = Text()
t3 = Text.assemble(t2, "more problems")
print(t3)

a = "long [warning] string [red]\[red text][/red] some more"
print(a)

dct = {"value": 1, "value2": False}

t4 = Text("A value")
t4.append("\n")
js = JSON(json.dumps(dct))

t4.append(js.text)
# t4 = JSON(json.dumps(dct))

print(t4)

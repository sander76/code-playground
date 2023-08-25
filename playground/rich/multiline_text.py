from rich.text import Text
from rich.json import JSON
import json
from rich import print

some_json = {"a": 10}

js = JSON(json.dumps(some_json))

text = Text("some \n\n multiline data")

print(text.cell_len)

print(text)
print(js)

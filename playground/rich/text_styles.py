from pydantic import ColorError
from rich import print
from rich.text import Text
from rich.style import Style
from rich.color import Color, ColorType

txt = Text("some value", style=Style(color="red"))
txt.append(Text("some more", style=Style(color="blue")))

txt.stylize(Style(bgcolor="yellow"))

print(txt)

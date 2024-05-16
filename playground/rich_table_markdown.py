from rich import markdown
from rich.table import Table

table = Table()
table.add_column("test1")
table.add_column("test2")

table.add_row("value1", "value2")

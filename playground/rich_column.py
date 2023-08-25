# import os
# import sys

# from rich import print
# from rich.columns import Columns

# if len(sys.argv) < 2:
#     print("Usage: python columns.py DIRECTORY")
# else:
#     directory = os.listdir(sys.argv[1])
#     columns = Columns(directory, equal=True, expand=True)
#     print(columns)

from rich import print
from rich.table import Table

grid = Table.grid(expand=True)
grid.add_column()
grid.add_column(justify="right")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")

print(grid)

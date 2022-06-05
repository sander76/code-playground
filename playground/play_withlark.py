from lark import Lark


json_parser = Lark(
    r"""
    value: dict
         | list
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """,
    start="value",
)

text = '{"key": ["item0", "item1", 3.14]}'
text1 = "[123,344]"
test = '"abc"'
result = json_parser.parse(test)
print(result.pretty())

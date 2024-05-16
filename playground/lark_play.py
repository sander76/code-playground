from lark import Lark

# for lark cheatsheet go here: https://github.com/lark-parser/lark/blob/master/docs/_static/lark_cheatsheet.pdf

parser = Lark(
    r"""
    start:  _line+ // find the rule 1 or more times.
        
    _line: WARN | ERROR | SPACES | WORDS // the underscore tells lark to inline the rule (no nested tree)
    
    WARN: /[\[]*[\s]*warn[\w]*[\s]*[\]]*/
    ERROR: /[\[]*[\s]*error[\w]*[\s]*[\]]*/

    WORDS.-100: /[\w]+/  // has a priority of -100 (the lowest)
    SPACES.-100: WS+

    %import common.WORD
    %import common.WS

""",
    start="start",
)

line = "some word  [ warning ] warn 234 error "

result = parser.parse(line)

for token in result.children:
    print(token.type)
    print(token.value)
print(result.children)

# json_parser = Lark(
#     r"""
#     value: dict
#          | list
#          | ESCAPED_STRING
#          | SIGNED_NUMBER
#          | "true" | "false" | "null"

#     list : "[" [value ("," value)*] "]"

#     dict : "{" [pair ("," pair)*] "}"
#     pair : ESCAPED_STRING ":" value

#     %import common.ESCAPED_STRING
#     %import common.SIGNED_NUMBER
#     %import common.WS
#     %ignore WS

#     """,
#     start="value",
# )

# text = '{"key": ["item0", "item1", 3.14]}'
# text1 = "[123,344]"
# test = '"abc"'
# result = json_parser.parse(test)
# print(result.pretty())

from lark import Lark, Transformer, Visitor
from lark.tree import Tree
from lark import common

strings = [
    "Switch.mRID",
    "Switch.mRID == 151703",  # bk_e_ms_schakelaar_fp veld 6
    "Switch.mRID == 45115",  # bk_e_ms_schakelaar_fp veld 5
    "Switch.normalOpen == True",
    "rdf:type in ['PowerTransformer']",
]

obj_id_ex_value = r"([^.]*)\.mRID\s?==\s?(.*)"
# obj_prop_ex_value

clause_parser = Lark(
    r"""
    item: identifier exp value
    
    identifier : obj_id
               | obj_prop
               | type

    obj_id     : object ".mRID"
    obj_prop   : object "." WORD
    type       : WORD ":type"

    exp        : "==" -> eq
               | "in" -> in 
    
    value      : mrid
               | "True" -> true
               | "False" -> false
    
    object     : WORD

    mrid       : SIGNED_NUMBER

    %import common.WORD
    %import common.WS
    %import common.SIGNED_NUMBER
    %ignore WS

    """,
    start="item",
)

val = clause_parser.parse(strings[3])

print(val.pretty())

LABEL_MAPPING = {"Switch": "EFP_SCHAKELAAR", "PowerTransformer": "Trafo"}

# class ObjVisitor(Visitor):
#     def __init__(self) -> None:
#         super().__init__()
#         self._obj={}

#     def obj_id()


class ToObjects(Transformer):
    def item(self, items: Tree):

        return dict(items)

    def obj_id(self, item):
        (item,) = item
        item = str(item)
        return {"label": item}

    def mrid(self, item):
        return int(item[0])

    def value(self, value):
        return value[0]

    def object(self, object):
        val = object[0]
        return LABEL_MAPPING[val]

    def true(self, _):
        return True

    def false(self, _):
        return False


obj = ToObjects().transform(val)
print(obj)

# # from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
# from parsimonious.grammar import Grammar


# grammar = Grammar(
#     """
#     expr              = identifier expression value

#     identifier        = object_property / type_desc
#     object_property   = obj "." val
#     obj               = ~r"[A-Z0-9]*"i
#     val               = ~r"[A-Z0-9]*"i
#     type_desc         = ~r"([A-Z0-9]*)\:([A-Z0-9]*)"i

#     expression        = " == " / " in "
#     value             = ~"[A-Z 0-9]*"i

#     """
# )


# # object_list       = lcoll items rcol
# #     lcoll             = "["
# #     rcoll             = "]"


# print(grammar.parse(strings[3]))

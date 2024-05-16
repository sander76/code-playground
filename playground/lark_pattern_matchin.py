from lark import Lark, Transformer, Visitor
from lark.tree import Tree
from lark import common

strings = [
    '{"when": "start", "select": {"or": ["BusbarSection.mRID == 289815669"]}}'
    "Switch.mRID",
    "Switch.mRID == 151703",  # bk_e_ms_schakelaar_fp veld 6
    "Switch.mRID == 45115",  # bk_e_ms_schakelaar_fp veld 5
    "Switch.normalOpen == True",
    "rdf:type in ['PowerTransformer']",
]


clause_parser = Lark(
    r"""
    item : start_stop_objects
          | stop_labels

    start_stop_objects : obj_id "==" value
    stop_labels        : "rdf:type in" obj_list

    ?obj_id    : object ".mRID"
    obj_prop   : object "." WORD

    ?value     : mrid
               | "True" -> true
               | "False" -> false

    obj_list   : "[" [object ("," object)*] "]"
    object     : ["'"]WORD["'"]

    mrid       : SIGNED_NUMBER

    %import common.WORD
    %import common.WS
    %import common.SIGNED_NUMBER
    %ignore WS

    """,
    start="item",
)

val = clause_parser.parse(strings[1])
print(val.pretty())


class ToObjects(Transformer):
    LABEL_MAPPING = {"Switch": "EFP_SCHAKELAAR", "PowerTransformer": "Trafo"}

    def start_stop_objects(self, item):
        return {"label": item[0], "key": "assetId", "value": item[1]}

    def stop_labels(self, item):
        items = item[0]
        return [{"label": obj} for obj in items]

    def obj_list(self, items):
        return list(items)

    def mrid(self, item):
        return int(item[0])

    def object(self, object):
        val = object[0]
        return ToObjects.LABEL_MAPPING[val]

    def true(self, _):
        return True

    def false(self, _):
        return False


obj = ToObjects().transform(val)
print(obj)

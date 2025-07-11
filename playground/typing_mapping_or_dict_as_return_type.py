from collections.abc import Mapping


def ret_mapping() -> Mapping[str, int]:
    return {"myval": 1}


val = ret_mapping()

# val["k"] = 10

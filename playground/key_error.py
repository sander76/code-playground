a = {"a": 10}


def go():
    val = a["b"]


try:
    go()
except KeyError as err:
    pass

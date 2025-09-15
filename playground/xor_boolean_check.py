from operator import xor


def go(val: int | None, val_2: int | None):
    if xor(val is None, val_2 is None):
        print("one of both is None")
        return

    print(val, val_2)


go(10, 10)
go(None, 10)
go(10, None)
go(None, None)

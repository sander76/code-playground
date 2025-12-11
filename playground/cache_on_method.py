from functools import cache


class MyClass:
    def __init__(self, val: int):
        self.val = val

    @cache
    def go(self) -> int:  # <---- self is not part of the cache key
        return self.val * 2


mycls = MyClass(val=2)
print("expecting 4")
print(mycls.go())

mycls.val = 10
print(mycls.go())

class MyModel:
    def __init__(self, val: int) -> None:
        self.val = val


from testfixtures.comparison import compare

val1 = MyModel(val=10)
val2 = MyModel(val=10)

print(val1 == val2)
print(val1.__dict__ == val2.__dict__)
print(compare(val1, val2, strict=True))

val3 = MyModel(val=11)
print(compare(val1, val3, strict=True))

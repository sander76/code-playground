# def multiply(value:int):
#     return value * 2

# def add(value:int):
#     return value+10

# print(multiply(10).add)


class B:
    def __init__(self) -> None:
        self.a = 10


b = B()

print(id(b.__class__))
print(id(b.__class__))
print(id(b.__class__))
print(id(b.__class__))

print(hash(b.__class__))
print(b.__class__)

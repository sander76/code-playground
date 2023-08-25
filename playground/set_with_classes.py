class A:
    def __init__(self, value: int = 10) -> None:
        self.a = value


container = set()

a = A(value=12)

container.add(a)

print(a in container)

a.a = 20


container.add(a)

print(len(container))

for con in container:
    print(con.a)

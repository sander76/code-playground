class B:
    def __init__(self, source: bytes) -> None:
        self._source = source

    def __getitem__(self, item):
        return self._source[item]


a = B(bytes([1, 2, 3]))

print(a[1])
print(a[1:3])

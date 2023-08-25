class A:
    def get_value(self):
        return 10


class B:
    def __init__(self) -> None:
        self.cls_a: A = A()

    def get_value_for_b(self):
        value_a = self.cls_a.get_value()

        return value_a * 2


def test_get_value(monkeypatch):
    b = B()

    result = b.get_value_for_b

    assert result == 20

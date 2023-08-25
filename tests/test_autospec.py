from unittest.mock import create_autospec


class SomeClass:
    def _render(self, value: str,some_more:str) -> str:
        return f"{value} {some_more} rendered"

    def lines(self, value: str) -> str:
        return self._render(value)


def test_with_mock(monkeypatch):
    monkeypatch.setattr(SomeClass, "_render", create_autospec(spec=SomeClass._render,return_value="mocked_value"))

    smclass = SomeClass()

    result = smclass.lines("some_value")
    print(result)

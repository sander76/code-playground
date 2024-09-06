import pytest


def test_something():
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_dict_():
    a = [{"a": "hello", "c": 0.1 + 0.2}]

    assert a == [{"a": "hello", "c": pytest.approx(0.3)}]

import pytest


@pytest.fixture
def my_fix():
    # raise AssertionError("fixture fail.")
    raise ValueError("fixture fail.")


def test_raise(my_fix):
    1 == 1


def test_failed_assert():
    assert False, "wrong assertion"

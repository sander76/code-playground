class A:
    """A test class"""


class B:
    """A B test class"""


def test_without_assert():
    a = B()
    assert isinstance(a, A)


def test_with_assert() -> None:
    a = B()
    assert isinstance(a, A), "A should be A"

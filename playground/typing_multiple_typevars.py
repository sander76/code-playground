from __future__ import annotations

from typing import Generic, Protocol, TypeVar, reveal_type

#
# protocol definitions
#
T = TypeVar("T")
O = TypeVar("O", int, float)


class Addable(Protocol[O]):
    def __add__(self, other) -> Addable: ...


Tadd_self = TypeVar("Tadd", bound=Addable)
Tadd_other = TypeVar("Tadd_other", bound=Addable)

#
# Simpler example of typing issues with Curve type
#


class X(Generic[T]):
    _elt: T

    def __init__(self, elt: T) -> None:
        self._elt = elt

    def __add__(self: X[Tadd_self], rhs: X[Tadd_other]) -> X[T | Tadd_other]:
        return X(self._elt + rhs._elt)


class CantAdd:
    pass


# checking that X can store any type
test_any = X[int](CantAdd())
reveal_type(test_any)

# these work BUT ONLY BECAUSE Tadd is bound to a float and int
# likely not how it is supped to work
float_plus_float = X(1.0) + X(2.0)
reveal_type(float_plus_float)

int_plus_int = X(1) + X(2)
reveal_type(int_plus_int)

# should pass, but does not
int_plus_float = X(1) + X(2.0)
reveal_type(int_plus_float)

# passes in mypy, but should not
# doesn't pass in pylance
# Y_plus_Y = X(CantAdd()) + X(CantAdd())


a = 100
b = 1.0
c = a + b
reveal_type(c)

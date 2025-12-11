from dataclasses import dataclass


@dataclass(kw_only=True)
class Base:
    a: int
    b: int = 1


@dataclass
class Child(Base):
    c: int

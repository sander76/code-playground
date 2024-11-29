from curses.ascii import isupper
from itertools import batched


def to_snake(val: str) -> str:
    """Convert a string to snake case.

    >>> to_snake("a Word")
    'a_word'

    >>> to_snake("a word")
    'a_word'

    >>> to_snake("aWord")
    'a_word'

    >>> to_snake("A Word")
    'a_word'

    >>> to_snake("AWord")
    'a_word'

    >>> to_snake("a worD")
    'a_wor_d'

    >>> to_snake("a word ")
    'a_word'

    >>> to_snake("a wor D")
    'a_wor_d'
    """

    def walk():
        str_iter = iter(val)
        try:
            while True:
                char = next(str_iter)
                if char == " ":
                    next_char = next(str_iter)
                    if next_char.isupper():
                        # concat a combination of two characters consisting of a space and an upper case char
                        # to a single underscore.
                        yield from ("_", next_char.lower())
                    else:
                        yield from ("_", next_char)
                elif char.isupper():
                    yield from ("_", char.lower())
                else:
                    yield char
        except StopIteration:
            return

    return "".join(walk()).lstrip("_")


if __name__ == "__main__":
    pass

class MyException(Exception): ...


def do_stuff():
    try:
        try:
            raise MyException("some message")
        except MyException as err:
            err.add_note("note 1")
            raise
    except MyException as err:
        err.add_note("note_2")
        raise


do_stuff()

class CallError(Exception):
    """A call error exception."""


def function():
    raise KeyError("A key error has occurred.")


def caller():
    try:
        function()
    except KeyError as err:
        raise CallError(
            "a call error"
        ) from None  # <-- If None, only the CallError stack will be used and the KeyError data is silenced.
        # If `from err` both KeyError and CallError are displayed in the error message.


if __name__ == "__main__":
    caller()

import pickle


class Other:
    def __init__(self, *args) -> None:
        self.args = args


class GdssError(Exception):
    """Raise an error when a Gdss request did not succeed."""

    def __init__(self, message: str, structlog_context: dict) -> None:
        super().__init__(message)
        self.structlog_context = structlog_context


exc = GdssError("I am an error", {"foo": "bar"})

pickled = pickle.dumps(exc)
unpickled = pickle.loads(pickled)
unpickled = pickle.loads(pickle.dumps(exc))

print(unpickled.structlog_context)

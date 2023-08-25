import structlog

_logger = structlog.get_logger()


class StructuredException(Exception):
    def __init__(self, message: str, structlog_context: dict) -> None:
        super().__init__(message)
        self.structlog_context = structlog_context


def a_function(value: int = 10):
    _log = _logger.bind(a=value)
    raise StructuredException(
        "something went wrong", structlog_context=structlog.get_context(_log)
    )


try:
    a_function()
except StructuredException as e:
    message = str(e)
    _logger.exception(e, **e.structlog_context)

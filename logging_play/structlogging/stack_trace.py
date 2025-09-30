import structlog

_logger = structlog.get_logger()


def raise_some_more():
    raise ValueError("some error")


try:
    raise_some_more()
except ValueError:
    _logger.exception("something went wrong")

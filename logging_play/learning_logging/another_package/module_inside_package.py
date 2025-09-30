import logging

_LOGGER = logging.getLogger(__name__)


def execute_this_function():
    _LOGGER.info("This caught by an up-level logging entry.")
    _LOGGER.debug("This is a debug message")


def with_exception():
    try:
        1 / 0
    except Exception:
        _LOGGER.exception("something went wrong with an exception")


def warner():
    _logger = logging.getLogger("warner")
    _logger.warning("another warning")
    _logger.info("some info inside warner")
    _logger.error("some error")

# pretty inconvenient. don't use.

import logging

from pythonjsonlogger.jsonlogger import JsonFormatter


def setup():
    logger = logging.getLogger()

    handler = logging.StreamHandler()
    formatter = JsonFormatter()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


setup()

_logger = logging.getLogger(__name__)


_logger.info("some_info", extra={"value": 10})

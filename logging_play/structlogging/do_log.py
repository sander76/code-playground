import logging
from pprint import pprint

import structlog
from structlog import get_logger, processors
from structlog.contextvars import merge_contextvars
from structlog.dev import ConsoleRenderer, set_exc_info
from structlog.stdlib import LoggerFactory, add_logger_name
from structlog.threadlocal import wrap_dict

# logging.basicConfig(level=logging.DEBUG)
# _normal_logger = logging.getLogger()
# _normal_logger.setLevel(logging.DEBUG)

_processors = [
    processors.add_log_level,
    processors.StackInfoRenderer(),
    set_exc_info,
    processors.TimeStamper(),
    ConsoleRenderer(),
]
structlog.configure(processors=_processors)


class MyException(Exception):
    def __init__(self, message: str, value: int) -> None:
        super().__init__(message, value)
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return f"{self.message} {self.value}"


structlog.configure()


_logger = structlog.get_logger(__name__, b=1)
_log = _logger.bind(a=10)
_logger.info("some info")


def with_exception():
    raise MyException("my exception raised", 10)


# context = structlog.get_context(_log)
# pprint(context)

_log.exception(with_exception())

import structlog
from structlog.stdlib import LoggerFactory


class MyException(Exception):
    def __init__(self, message: str, value: int) -> None:
        super().__init__(message, value)
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return f"{self.message} {self.value}"


structlog.configure(logger_factory=LoggerFactory())


_logger = structlog.get_logger(__name__, b=1)
_log = _logger.bind(a=10)
_logger.info("some info")


def with_exception():
    raise MyException("my exception raised", 10)


# context = structlog.get_context(_log)
# pprint(context)

_log.exception(with_exception())

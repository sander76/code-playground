import logging
from collections import defaultdict

from pytest import LogCaptureFixture


class LogCapFilter:
    """Add this filter to a logger to filter messages.

    Examples:
        In a module which contains a logger you want to cap its output:
        >>> _logger = logging.getLogger(__name__)
        >>> _logger.addFilter(LogCapFilter())
        >>> _logger.info("A capped log message", extra={"cap": LogCap("unique_id")})

    """

    def __init__(self) -> None:
        self.occurrences: dict[str, int] = defaultdict(lambda: 0)

    def filter(self, record: logging.LogRecord) -> bool:
        try:
            cap: LogCap = record.cap  # type: ignore
        except AttributeError:
            # cap attribute found, so not doing any capping.
            return True

        self.occurrences[cap.cap_id] += 1
        if self.occurrences[cap.cap_id] > cap.limit:
            return False

        if self.occurrences[cap.cap_id] == cap.limit:
            record.msg = f"{record.msg} [MESSAGE LIMITED TO {cap.limit} OCCURRENCES]"
        return True


class LogCap:
    """Add this to the extra dict of your log message to limit the number of occurrences in the log output."""

    def __init__(self, log_id: str, limit: int = 3) -> None:
        """Init.

        Args:
            log_id: An identifier for the LogCapFilter to count the number of occurrences of a message.
            limit: Max amount of occurrences in the log output. Defaults to 3.
        """
        self.limit = limit
        self.cap_id = log_id


def test_log_cap(caplog: LogCaptureFixture):
    caplog.set_level(logging.INFO)
    _logger = logging.getLogger("my test logger")
    _logger.addFilter(LogCapFilter())

    for _ in range(10):
        _logger.info("this should occur only 4 times", extra={"cap": LogCap("log_id", limit=4)})

    assert caplog.messages == [
        "this should occur only 4 times",
        "this should occur only 4 times",
        "this should occur only 4 times",
        "this should occur only 4 times [MESSAGE LIMITED TO 4 OCCURRENCES]",
    ]


def test_no_logcap(caplog: LogCaptureFixture):
    caplog.set_level(logging.INFO)
    _logger = logging.getLogger("my test logger")
    _logger.addFilter(LogCapFilter())

    _logger.info("no logcap message")

    assert caplog.messages == ["no logcap message"]

import contextlib
import functools
import logging
from typing import Generator, Iterable

logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)


class LogCapFilter:
    def __init__(self):
        self.occurrences: dict[str, int] = {}

    def filter(self, record: logging.LogRecord):
        try:
            cap: LogCap = record.cap
        except AttributeError:
            return True
        occurence = self.occurrences.setdefault(cap.cap_id, 0)
        self.occurrences[cap.cap_id] += 1
        if occurence >= cap.limit:
            return False
        record.msg = f"{record.msg} [MESSAGE LIMITED TO {cap.limit} OCCURRENCES]"
        return True


_logger.addFilter(LogCapFilter())


class LogCap:
    def __init__(self, log_id: str, limit: int = 3) -> None:
        self.limit = limit
        self.cap_id = log_id


# def cap_logging(logger: logging.Logger):
#     logcounter = LogCounter(logger.name)
#     logger.addFilter(logcounter)

#     def decorator(func):
#         functools.wraps(func)

#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             finally:
#                 if logcounter in logger.filters:
#                     logger.filters.remove(logcounter)
#                 fltrs = logger.filters

#                 for message, count in logcounter.occurrences.items():
#                     logger.info(f"{message} occurred {count} times")

#         return wrapper

#     return decorator


# @contextlib.contextmanager
# def cap_logging(logger: logging.Logger) -> Generator[None, None, None]:
#     logcounter = LogCounter()
#     logger.addFilter(logcounter)
#     try:
#         yield
#     finally:
#         logger.removeFilter(logcounter)
#         for message, count in logcounter.occurrences.items():
#             logger.info(f"{message} occurred {count} times")


def log_list_tester() -> list[str]:
    data = []
    for i in range(10):
        _logger.info("some list info", extra={"cap": LogCap(log_id="abc")})
        data.append(f"list item {i}")
    return data


def go():
    for item in log_list_tester():
        print(item)


go()

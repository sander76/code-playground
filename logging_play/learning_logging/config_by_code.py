import logging

import uv_project
from rich.logging import RichHandler

from learning_logging.another_package import module_inside_package
from learning_logging.log_filter import add_id


class LogCollector(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        self._collection: list[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self._collection.append(record)


stream_handler = RichHandler(
    rich_tracebacks=False, tracebacks_show_locals=False, show_path=False
)
stream_handler.setFormatter(logging.Formatter("%(message)s", datefmt="[%X]"))
stream_handler.setLevel(logging.INFO)
stream_handler.addFilter(add_id())

_logger = logging.getLogger("warner")
_logger.setLevel(logging.WARNING)

base_logger = logging.getLogger()
base_logger.setLevel(logging.DEBUG)
base_logger.addFilter(add_id())
base_logger.addHandler(stream_handler)

log_collector = LogCollector()
log_collector.setLevel(logging.WARNING)
base_logger.addHandler(log_collector)

_logger = logging.getLogger(__name__)

_logger.info("this is local info")
_logger.warning("this is a warning")
module_inside_package.execute_this_function()
module_inside_package.warner()
module_inside_package.with_exception()
uv_project.hello()

print(log_collector._collection)

for log in log_collector._collection:
    print(f"{log.levelname} {log.msg}")

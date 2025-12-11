import logging
from logging import StreamHandler


def setup_logging():
    logger = logging.getLogger("anothername")
    logger.setLevel(logging.INFO)

    stream_handler = StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))

    stream_handler.setLevel(logging.INFO)

    logger.addHandler(stream_handler)


setup_logging()
_logger = logging.getLogger("some_name")

_logger.info("hello")

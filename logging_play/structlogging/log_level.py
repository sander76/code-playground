import structlog
import logging

_logger = structlog.get_logger()

logging.basicConfig(level=logging.INFO)

structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.INFO))

_logger.info("this is info")
_logger.debug("this is debug")

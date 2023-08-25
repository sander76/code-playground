import structlog
import logging

logger = structlog.get_logger()

exception = ValueError("A problem")

# logger.exception(exception)

# logger.error(exception,exc_info=True)
logger.info("starting to do stuff")


def go():
    raise ValueError("a problem", 10)


def print_err(exception):
    # logger.error(str(exception), exc_info=exception)

    logger.exception(str(exception))
    logger.exception(exception)


# try:
#     go()
# except ValueError:
#     logger.exception("a problem")

try:
    go()
except ValueError as err:
    print_err(err)

import logging

_LOGGER = logging.getLogger(__name__)


def run_a_function():
    _LOGGER.debug("This is a debug message")
    _LOGGER.info("This is an info message", extra={"fname": __file__})


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run_a_function()

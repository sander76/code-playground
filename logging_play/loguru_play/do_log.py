import sys

from loguru import logger

# def custom_sink(message):
#     rec = message.record
#     print(rec)


# logger.add(custom_sink)
logger.add("app.log", serialize=True)
# logger.add(sys.stdout, format="{time} {level} {message} {extra}")

context_logger = logger.bind(value=10)
context_logger.debug("this is a debug message", name="sander", another=101)
logger.info("some more")

import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


def logall(logger):
    def wrapping_call(func):
        def _wrap(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, str):
                logger.debug(f"result from {func.__name__}: {result=}")

            elif isinstance(result, tuple):
                addr, value = result
                logger.debug(f"result from {func.__name__}: {value.prettyPrint()}")

            return result

        return _wrap

    def _logall(cls):
        def _wrapper(*args, **kwargs):
            class Wrapped(cls):
                def __getattribute__(self, attr):
                    if attr.startswith("read"):
                        logger.debug(f"{attr} on {cls.__name__!r}")
                    return wrapping_call(super().__getattribute__(attr))

            return Wrapped(*args, **kwargs)

        return _wrapper

    return _logall


@logall(_logger)
class MyClass:
    def read(self, name):
        return f"hello {name}"


cls = MyClass()
cls.read("sander")

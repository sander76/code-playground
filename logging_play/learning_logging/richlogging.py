import logging

from rich.logging import RichHandler

from learning_logging import imported_file

log = logging.getLogger()

log.info("just some info")

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=False)],
)


class CustomException(Exception):
    def __init__(self, parameters_period, price_period) -> None:
        super().__init__(
            f"Battery parameters period not compatible with price period."
            + f" {parameters_period=!r}, {price_period=!r}"
        )


def experiment():
    try:
        print(1 / 0)
    except Exception:
        log.exception("problem occurred.")

    try:
        raise CustomException(parameters_period="HOURLY", price_period="DAILY")
    except CustomException as err:
        log.error(err)
    log.info(
        "a dict",
        **{
            "value": 1,
            "value2": False,
            "value3": [1, 2, 3, 4, 5, 6],
            "value4": "some more values",
            "value5": {"sub1": 10, "sub2": ["asdf", "gegre"]},
        },
    )

    log.debug("Should not print", extra={"some_info": 1})

    val = 10
    log.info("value: %s", val)


imported_file.do_some_logging()

if __name__ == "__main__":
    # logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)

    experiment()

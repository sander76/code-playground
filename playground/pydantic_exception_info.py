import logging

from pydantic import BaseModel, ValidationError

logging.basicConfig(level=logging.INFO)


_logger = logging.getLogger(__name__)


class Mdl(BaseModel):
    value: int
    value_2: int


def go():
    try:
        mdl = Mdl(value=10, value_2="abc")
    except ValidationError:
        _logger.exception("something went wrong")


go()

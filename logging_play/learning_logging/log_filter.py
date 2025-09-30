import logging
from logging import LogRecord

_LOGGER = logging.getLogger(__name__)


def add_id():
    def filter(record: LogRecord):
        record.msg = f"an id -- {record.msg}"
        return True

    return filter


def add_id_js():
    def filter(record:LogRecord):
        record.prod_id="a record"
        return True
        # record["prod_id"]= "an id"

    return filter

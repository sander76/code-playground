from tenacity import RetryError, Retrying, retry
from tenacity.stop import stop_after_attempt
from tenacity.retry import retry_if_exception_type
from tenacity import wait
from datetime import datetime
import time

RETRIES = 3

_wait = wait.wait_exponential(max=20)


def collect():
    current = time.time()
    print(f"attempt {current}")
    raise ValueError("A value error")


def do_try():
    retrier = Retrying(
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(ValueError),
        wait=wait.wait_exponential(max=20),
        reraise=True,
    )

    for attempt in retrier:
        with attempt:
            print(f"Attempt nr: {attempt.retry_state.attempt_number}")
            collect()


class Injector:
    def __init__(self, retries=3):
        self._retries = retries
        self._previous_run = 0

    @retry(
        stop=stop_after_attempt(0),
        reraise=True,
        retry=retry_if_exception_type(ValueError),
        wait=_wait,
    )
    def collect(self):
        current = time.time()
        print(f"attempt {current - self._previous_run}")
        self._previous_run = current

        raise ValueError("Value error")

    def go(self):
        try:
            self.collect()
        except ValueError:
            print("too many retries")
        except RetryError:
            print("retry caught")


# injector = Injector()
# injector.go()
do_try()

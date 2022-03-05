from failsafe import Failsafe, RetryPolicy, Backoff
from datetime import timedelta, datetime


def some_code():
    print(datetime.now())
    raise ValueError("This is an error")


backoff = Backoff(delay=timedelta(seconds=2), max_delay=timedelta(seconds=30))

retry_policy = RetryPolicy(allowed_retries=4, backoff=backoff)

Failsafe(retry_policy=retry_policy).run(some_code)

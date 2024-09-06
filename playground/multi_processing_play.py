import concurrent
import concurrent.futures
import time

from pydantic import BaseModel


class MySettings(BaseModel):
    delay: int


settings = MySettings(delay=3)


def a_job(delay: int | None = None):
    if delay is None:
        delay = settings.delay

    print(f"delaying {delay} seconds")
    time.sleep(delay)
    return 5


def a_raising_job():
    raise ValueError("my error")


def run_processes():
    jobs = [a_job, a_job, a_raising_job]
    t0 = time.monotonic()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(job, delay=1) for job in jobs]

    print(f"duration {time.monotonic()-t0}")
    for result in results:
        print(result)


run_processes()

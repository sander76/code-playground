import concurrent
import concurrent.futures
import multiprocessing
import time

from pydantic import BaseModel


class MySettings(BaseModel):
    delay: int


settings = MySettings(delay=3)

JOB_NAME = ""


def a_job(delay: int | None = None):
    if delay is None:
        delay = settings.delay

    print(f"delaying {delay} seconds, {JOB_NAME=}")
    time.sleep(delay)
    return 5


def _pre_init(job_name: str):
    print("called")
    global JOB_NAME
    JOB_NAME = job_name


def run_processes():
    jobs = [a_job, a_job]
    t0 = time.monotonic()
    with concurrent.futures.ProcessPoolExecutor(
        mp_context=multiprocessing.get_context("spawn"),
        max_workers=1,
        initializer=_pre_init,
        initargs=("abc",),
    ) as executor:
        results = [executor.submit(job, delay=1) for job in jobs]

    print(f"duration {time.monotonic()-t0}")
    for result in results:
        print(result)


if __name__ == "__main__":
    run_processes()

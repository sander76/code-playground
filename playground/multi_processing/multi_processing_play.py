import concurrent
import concurrent.futures
import multiprocessing
import time

from pydantic import BaseModel


def a_job(delay: int):
    print(f"delaying {delay} seconds")
    time.sleep(delay)
    print(f"finished on delay {delay}")
    return delay


def a_raising_job():
    raise ValueError("my error")


def run_processes():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(a_job, delay=8), executor.submit(a_job, delay=1)]

    for result in results:
        print(result.result())


# class SomeShit:
#     def go(self):
#         run_processes()


# def do_shit():
#     print("some shit")

if __name__ == "__main__":
    run_processes()

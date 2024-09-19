import time

import ray


@ray.remote()
def go(val: int):
    time.sleep(val)
    if val == 2:
        raise ValueError("this was a two.")
    return val * 2


ray.init()

jobs = [go.remote(i) for i in range(5)]

try:
    res = ray.get(jobs)
except Exception:
    pass

print(res)

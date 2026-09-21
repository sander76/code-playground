import time
from dataclasses import dataclass

from diskcache import Cache


@dataclass
class MyObj:
    greet: str
    name: str


CACHE_DIR = "/tmp/myobj-cache"
cache = Cache(CACHE_DIR)
#
# def store(cache: Cache, key: str, obj: MyObj) -> None:
#     if cache[key]:
#
#     cache[key] = obj
#
#
# def retrieve(cache: Cache, key: str) -> MyObj | None:
#     return cache.get(key)
#
#
# def delete(cache: Cache, key: str) -> bool:
#     return cache.delete(key)
#

# if __name__ == "__main__":
#     with Cache(CACHE_DIR) as cache:
#         obj = MyObj(val=42, val_2="hello")
#         print(f"Storing:   {obj}")
#         store(cache, "my_key", obj)
#
#         fetched = retrieve(cache, "my_key")
#         print(f"Retrieved: {fetched}")
#
#         delete(cache, "my_key")
#         missing = retrieve(cache, "my_key")
#         print(f"After delete: {missing}")


@cache.memoize()
def load(my_obj: MyObj) -> str:
    time.sleep(5)
    return f"{my_obj.greet} {my_obj.name}"


strt = time.monotonic()
print(load(MyObj(greet="hi", name="sander")))
print(f"finished in {time.monotonic() - strt}")

strt = time.monotonic()
print(load(MyObj(greet="hello", name="piet")))

print(f"finished in {time.monotonic() - strt}")

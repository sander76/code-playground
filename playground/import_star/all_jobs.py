import importlib
import inspect
from import_star import jobs


def load_jobs():
    members = inspect.getmembers(jobs,predicate=inspect.ismodule)

    for member in members:
        
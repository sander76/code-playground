from collections.abc import Mapping, Sequence
from typing import Iterable


def walk_dict(obj, *path: str | int | None) -> Iterable[tuple[object, tuple[int | str, ...]]]:
    if path is None:
        path = tuple()
    if isinstance(obj, Mapping):
        for key, value in obj.items():
            yield from walk_dict(value, *path, key)
    elif isinstance(obj, Sequence) and not isinstance(obj, str):
        for idx, item in enumerate(obj):
            yield from walk_dict(item, *path, idx)

    # we skip the yield when the path is empty as this would return the original object, which is of no use.
    if path:
        yield obj, path
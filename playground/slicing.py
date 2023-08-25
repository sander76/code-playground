a = [1, 2, 3, 4, 5]


def get_items(idx) -> tuple[int, list[int]]:
    if idx == 0:
        return a[idx], a[1:]
    return a[idx], a[:idx] + a[idx + 1 :]


for i in range(len(a)):
    print(get_items(i))

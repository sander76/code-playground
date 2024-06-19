a = ["feb", "jan", "dec", "oct"]

month_vals = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def month_sorter(value):
    return month_vals[value]


srt = sorted(a, key=month_sorter)

print(srt)

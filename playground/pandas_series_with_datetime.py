# convert a list of string data to a series with datetime values.

from datetime import datetime

import pandas as pd

dt1 = datetime(2020, month=1, day=1, hour=1)
dt2 = datetime(2020, month=1, day=1, hour=2)

data = [
    {"datetime": dt1.isoformat(), "value": 10.0, "other": 1},
    {"datetime": dt2.isoformat(), "value": 20.0, "other": 2},
]

series = pd.DataFrame(
    (row["value"] for row in data),
    index=pd.to_datetime([row["datetime"] for row in data]),
    columns=["value"],
)

# series["datetime"] = pd.to_datetime(series["datetime"])
# series = series.set_index("datetime")
print("as df")
print(series)

ser = pd.Series(
    (row["value"] for row in data),
    index=pd.to_datetime([row["datetime"] for row in data]),
)
print("as series")
print(ser)

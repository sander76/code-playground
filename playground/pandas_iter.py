import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})

for row in df.itertuples(index=False):
    print(row[0])
    print(row[1])

# for label, row in df.items():
#     print(label)
#     print(row)

# for idx, row in df.iterrows():
#     print(row["a"])
#     print(row["b"])

import numpy as np

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([1, 2, 3])
print(bool(arr_1 == arr_2))  # will raise an ambiguous error

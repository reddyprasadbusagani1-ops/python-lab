#27 NumPy indexing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Basic slicing:", arr[1:4])
print("Integer indexing:", arr[[0, 2, 4]])
print("Boolean indexing:", arr[arr > 25])

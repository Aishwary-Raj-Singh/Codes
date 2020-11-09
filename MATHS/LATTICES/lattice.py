import numpy as np
import math

v1 = [6, 2, -3]
v2 = [5, 1, 4]
v3 = [2, 7, 1]

numpy_array = np.array([v1, v2, v3])
print(numpy_array)
det = np.linalg.det(numpy_array)
print("Determinant is: ", math.ceil(abs(det)))

import numpy as np

a = np.array([[1, 0, -1, 5], [2, 1, 0, 6], [3, 4, -2, 7]])
b = np.array([[4, 8, 9], [-3, 0, -5]])

print(np.matmul(b, a))
import numpy as np

arr1 = np.array([[1,2,3], [4,5,6]])

print((arr1))
"""
[[1 2 3]
 [4 5 6]]
"""
print(arr1.shape)#(2, 3)

arr1_transposta = arr1.transpose()

print(arr1_transposta)
"""
[[1 4]
 [2 5]
 [3 6]]
"""

print(arr1.shape)#(2, 3)
print("NumpyのN次元配列")
import numpy as np
A = np.array([[1, 2], [3,4]])
print(A)
# 2行2列
print(A.shape)
print(A.dtype)
# --> int64
# 64ビットの符号付き整数
B = np.array([[3, 0], [0, 6]])
print(B)
print(A + B)
# 要素同士の掛け算
print(A * B)
print(A * 10)

# 不規則な行列
C = np.array([[1, 2],[3, 4, 5]])
print(C)
# [list([1, 2]) list([3, 4, 5])]
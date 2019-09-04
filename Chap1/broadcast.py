print("形状の異なる配列同士の演算：ブロードキャスト")
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)
B = np.array([10, 20])
print(B)
print(A * B)
print("要素へのアクセス")
import numpy as np
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[1])
print(X[2])
print(X[0][0])
print(X[0][1])
print(X[2][1])

for row in X:
    print(row)
    
# 一次元配列への変換    
X = X.flatten()
print(X)
# [51 55 14 19  0  4]
# 0, 2, 4番目の要素だけを抜き出す(0から始まる)
print(X[np.array([0, 2, 4])])

print(X[np.array([3])])

# 15以上の要素だけを抜き出す
print(X > 15)
# [ True  True False  True False False]
# Trueの要素だけを抜き出す
print(X[X > 15])
# [51 55 19]
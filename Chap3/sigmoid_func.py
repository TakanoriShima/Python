print("シグモイド関数の使用")
import numpy as np
import matplotlib.pyplot as plt

print("def sigmoid_function(x):")
print("    return 1.0 / (1 + np.exp(-1 * x))")
# sigmoid関数
def sigmoid_function(x):
    return 1.0 / (1 + np.exp(-1 * x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid_function(x)
# x = x1で段差があるなら
# y = step_func(x - x1)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.savefig("sigmoid_func.svg", format="svg", dpi=1200)
print("sigmoid_func.svg にグラフが出力されました。previewで確認してください")

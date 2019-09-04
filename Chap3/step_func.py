import numpy as np
import matplotlib.pylab as plt
# x = np.array([-1.0, 1.0, 2.0])
# print(x)

print("step_function の定義")
print("ef step_function(x):")
print("    return np.array(x > 0, dtype = np.int) ")
# step関数
def step_function(x):
    return np.array(x > 0, dtype = np.int) 

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
# x = x1で段差があるなら
# y = step_func(x - x1)
plt.plot(x, y)
plt.savefig("step_func.svg", format="svg", dpi=1200)
print("stp_func.svg にグラフが出力されました。previewで確認してください")


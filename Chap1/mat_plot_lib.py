print("Matplotlibの使用")
import numpy as np
import matplotlib.pyplot as plt

# 0~6 を 0.1 刻みで
x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.savefig("sin.svg", format="svg", dpi=1200)

print("Matplotlibの使用")
import numpy as np
import matplotlib.pyplot as plt

# 0~6 を 0.1 刻みで
x = np.arange(0, 6, 0.1)

# データ作成
y1 = np.sin(x)
y2 = np.cos(x)

# グラフの描画
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
#plt.savefig("sin-cos.png", format="png", dpi=1200)
plt.savefig("sin-cos.png")

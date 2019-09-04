print("画像表示")
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("lena.png")
plt.imshow(img)

plt.savefig("lena.svg", format="svg", dpi=1200)
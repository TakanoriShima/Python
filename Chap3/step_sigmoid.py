import numpy as np
import matplotlib.pylab as plt

print("step_function, sigmoid_function の重ね合わせ")

# step関数
def step_function(x):
    return np.array(x > 0, dtype = np.int) 
    
# sigmoid関数
def sigmoid_function(x):
    return 1.0 / (1 + np.exp(-1 * x))

x = np.arange(-5.0, 5.0, 0.1)

y1 = step_function(x)
y2 = sigmoid_function(x)
plt.plot(x, y1, label="step_function")
plt.plot(x, y2, linestyle="--", label="sigmoid_function")
plt.xlabel("x")
plt.ylabel("y")
plt.title("step_function & sigmoid_function")
plt.legend()
#plt.savefig("step-sigmoid.svg", format="svg", dpi=1200)
plt.savefig("step-sigmoid.png")

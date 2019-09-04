def AND(x1, x2): 
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1 * x1 + w2 * x2
    # AND gate
    
    """
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    """
    
import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w * x)
# [0.  0.5]
print(np.sum(w * x))
# 0.5
print(np.sum(w * x) + b)
# -0.19999999999999996
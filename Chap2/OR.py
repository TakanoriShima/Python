import numpy as np
# AND において、パラメータすべての符号を反転で実現
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
        
print("OR(0, 0) =  "  + str(OR(0, 0)))
print("OR(1, 0) =  "  + str(OR(1, 0)))
print("OR(0, 1) =  "  + str(OR(0, 1)))
print("OR(1, 1) =  "  + str(OR(1, 1)))
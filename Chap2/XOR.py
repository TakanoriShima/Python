import AND as And
import NAND as Nand
import OR as Or
def XOR(x1, x2):
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
    s1 = Nand.NAND(x1, x2)
    print("s1 = NAND(x1, x2) = " + str(s1))
    s2 = Or.OR(x1, x2)
    print("s2 = OR(x1, x2) = " + str(s2))
    y = And.AND(s1, s2)
    return y
    
print("XORは多層パーセプトロン")
print("XOR(0, 0) = AND(s1, s2) = " + str(XOR(0, 0)))
print("XOR(1, 0) = AND(s1, s2) = " + str(XOR(1, 0)))
print("XOR(0, 1) = AND(s1, s2) = " + str(XOR(0, 1)))
print("XOR(1, 1) = AND(s1, s2) = " + str(XOR(1, 1)))
    
    
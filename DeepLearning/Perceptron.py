import numpy as np
"""
 2章 パーセプトロン(Perceptron)
 author y-ok
 メリット   パーセプトロンを用いれば、単純な論理回路を表現できる
 デメリット バイアス、重み等のパラメータは事前に準備する必要がある
"""

"""
 ANDゲート
 論理積
"""
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 重み
    b = -0.7 # バイアス
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("--AND--")
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

"""
 NANDゲート
 論理積の否定
 重みとバイアスがANDと異なる
"""
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # 重み
    b = 0.7 # バイアス
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("--NAND--")
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))

"""
 ORゲート
 論理和
 バイアスがANDと異なる
"""
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 重み
    b = -0.2 # バイアス
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("--OR--")
print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))

"""
 XORゲート
 排他的論理和
 XOR == NAND + OR
 多層パーセプロン(multi-layered perceptron)
"""
def XOR(x1, x2):
    s1 = NAND(x1, x2)  # 1層目
    s2 = OR(x1, x2)    # 1層目
    return AND(s1, s2) # 2層目

print("--XOR--")
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))

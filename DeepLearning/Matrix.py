import numpy as np
import matplotlib.pyplot as plt
"""
 多次元配列の扱い方
 author y-ok
"""

# 1次元配列
A = np.array([1, 2, 3, 4])
print(A)

print(np.ndim(A))
print(A.ndim)

print(A.shape)
print(A.shape[0])

# 多次元配列
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)

print(np.ndim(B))
print(B.ndim)

print(B.shape)

# 行列の内積
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
print(X.shape)
print(Y.shape)
print(np.dot(X, Y))

X = np.array([1, 2])
print(X.shape)
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W.shape)

Y = np.dot(X, W)
print(Y)
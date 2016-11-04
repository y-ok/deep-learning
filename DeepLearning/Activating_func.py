import numpy as np
import matplotlib.pyplot as plt
"""
 3.2章 活性化関数
 author y-ok
"""

# ステップ関数
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)

plt.plot(x, step_function(x), label="ステップ関数")
plt.ylim(-0.1, 1.1) # y軸範囲指定

# シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

plt.plot(x, sigmoid(x), label="シグモイド関数", linestyle="--")

# ReLU関数(Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

plt.plot(x, relu(x), label="ReLU関数", linestyle="-.")
plt.show()
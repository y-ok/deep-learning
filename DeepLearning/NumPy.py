import numpy as np

"""
 How to use Numpy
 ver. python3.5
 author y-ok
"""
A = np.array([[1, 2], [3, 4]])

# 行列の形状
print(A.shape)

B = np.array([10, 20])

# 行列要素のデータ型
print(B.dtype)

# ブロードキャスト機能
print(A * 10)

# 要素へのアクセス
X = np.array([[51, 55], [14, 19], [0, 4]])

# 0行目
print(X[0])

# (0,1)の要素
print(X[0][1])

# for文を利用したアクセス
for row in X:
    print(row)

# Xを一次元配列へ変換
X = X.flatten()
print(X)

# インデックスが0, 2, 4番目の要素取得
print(X[np.array([0, 2, 4])])

# 要素が15より大きい値を指定すると、ブーリアン配列となる
print(X > 15)

print(X[X > 15])

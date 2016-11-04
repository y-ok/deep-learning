import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
"""
 How to use Matplotlib
 ver. python3.5
 author y-ok
"""

# データ準備
x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みでデータ生成
y1 = np.sin(x)
y2 = np.cos(x)

# グラフ描画
plt.subplot(2, 1, 1)
plt.plot(x, y1, label="$\sin$")
plt.plot(x, y2, linestyle = "--", label="$\cos$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("$\sin(x)$ & $\cos(x)$")
# グラフに凡例をつける
plt.legend()

"""
Matplotlib.py実行時、以下のエラーが発生
==================================================================================================================
RuntimeError: Python is not installed as a framework.
The Mac OS X backend will not be able to function correctly if Python is not installed as a framework.
See the Python documentation for more information on installing Python as a framework on Mac OS X.
Please either reinstall Python as a framework, or try one of the other backends.
If you are Working with Matplotlib in a virtual enviroment see 'Working with Matplotlib in Virtual environments'
in the Matplotlib FAQ
==================================================================================================================
対処法は、http://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49に記載通り。
以下のファイルを修正し、対応
~/.pyenv/versions/anaconda3-4.1.1/lib/python3.5/site-packages/matplotlib/mpl-data/matplotlibrc
"""
img = imread('./data/img/Lenna.png')
plt.subplot(2, 1, 2)
plt.imshow(img)
plt.show()


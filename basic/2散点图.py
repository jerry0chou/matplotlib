# -*- coding:utf-8 -*-
# Author : JerryChu
import numpy as np
import matplotlib.pyplot as plt
#散点图
# height=[171,184,158,169,181]
# weight=[50,41,67,89,43]
# plt.scatter(height,weight)
# plt.show()

#散点图(大量)
N = 100
x = np.random.randn(N)
y = -x + np.random.randn(N) * 0.2
plt.scatter(x, y,  # 坐标
            s=100,  # 面积
            c='g',  # 颜色
            alpha=0.3  # 透明度 可以判断 哪些点是集中的
            )
plt.show()

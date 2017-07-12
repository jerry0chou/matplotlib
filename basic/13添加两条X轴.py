# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 20, 1)
y1 = x * x
y2 = np.log(x)  # 对x求对数

# 面向过程
plt.plot(y1, x)
plt.twiny()
plt.plot(y2,x, 'r')

plt.show()

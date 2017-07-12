# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
# 子图就是 在一张图里面生成多张图
# 多图 就是 生成多个 窗口 每个窗口可以容乃一个或多个图
x=np.arange(1,100)

plt.subplot(221) # 2X2 排在第一个
plt.plot(x,x)

plt.subplot(2,2,2) # 2X2 排在第二个
plt.plot(x,-x)

plt.subplot(223)
plt.plot(x,x*x)

plt.subplot(2,2,4)
plt.plot(x,np.log(x))

plt.show()
# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11,1)
plt.plot(x,x*x)

ax=plt.gca() # 获取当前的坐标值 getCurrentAxis
ax.locator_params(nbins=40) # 默认调整XY轴密度
#ax.locator_params('y',nbins=5) # 调整Y轴密度

plt.show()

# 调整日期

# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11,1)
plt.plot(x,x*x)
print plt.axis() # 打印默认值
plt.axis([-5,11,0,50]) # 一起调整 XY轴

# plt.xlim([-10,11])
#plt.xlim(xmin=-111,xmax=100)
# plt.ylim([0,100])

plt.show()
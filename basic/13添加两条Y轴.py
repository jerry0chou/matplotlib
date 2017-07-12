# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(2,20,1)
y1=x*x
y2=np.log(x) # 对x求对数


''' # 面向过程
plt.plot(x,y1)
plt.twinx()
plt.plot(x,y2,'r')
'''

# 面向对象
fig=plt.figure() # 第一条曲线
ax1=fig.add_subplot(1,1,1) # 加入位置
ax1.plot(x,y1) # 画出来
ax1.set_ylabel('Y1')
ax1.set_xlabel('compare Y1 and Y2')

ax2=ax1.twinx() # 两者共用同一条X轴
ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')

plt.show()
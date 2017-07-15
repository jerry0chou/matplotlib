# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np

# 使用默认样式
print plt.style.available
# fivethirtyeight  ggplot bmh
plt.style.use('ggplot')

fig,axes=plt.subplots(ncols=2,nrows=2)
ax1,ax2,ax3,ax4=axes.ravel()

# 随机散点图
x,y=np.random.normal(size=(2,100))
ax1.plot(x,y,'o')


# 彩虹直线图
x=np.arange(0,10)
y=np.arange(0,10)
colors=plt.rcParams['axes.prop_cycle']
ncolor=len(colors) # 获得颜色循环的个数
shift=np.linspace(0,10,ncolor)
for s in shift:
    ax2.plot(x,y+s,'-')

# 柱状图
x=np.arange(5)
y1,y2,y3=np.random.randint(1,25,size=(3,5))
width=0.25
ax3.bar(x,y1,width)
ax3.bar(x+width,y2,width)
ax3.bar(x+2*width,y3,width)

# 球状图
for c in range(ncolor):
    xy=np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy,radius=0.3))
ax4.axis('equal')

# 全部显示
plt.show()
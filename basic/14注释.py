# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
#x=np.arange(-10,11,1)
x=np.linspace(-10,11,50)
y=x*x
plt.plot(x,y)
plt.annotate('this is the bottom',
             xy=(0,1), # 箭头所在坐标
             xytext=(0,20),# 注释的一个字符所在的位置
             arrowprops=dict(facecolor='r',frac=0.2,headwidth=30,width=10)
             # facecolor:箭头颜色 frac:箭头占整个箭的比列 headwidth:箭头宽度 width: 箭尾宽度

             )
plt.show()
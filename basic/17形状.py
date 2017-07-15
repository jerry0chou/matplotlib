# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import matplotlib.patches as matpat
import numpy as np

# 官网链接 http://matplotlib.org/api/patches_api.html

fig,ax=plt.subplots()
xy1=np.array([0.2,0.2]) # 圆心坐标
xy2=np.array([0.2,0.8]) # 长方形左下角 的那个点
xy3=np.array([0.8,0.2]) # 多边形中心点
xy4=np.array([0.8,0.8]) # 椭圆中心

circle=matpat.Circle(xy1,0.05)
rect=matpat.Rectangle(xy2,0.2,0.1,color='r')
polygon=matpat.RegularPolygon(xy3,5,0.1,color='g') # 5条边 半径为0.1
eclipse=matpat.Ellipse(xy4,0.4,0.2,color='y') # 椭圆的长直径，和短直径

ax.add_patch(circle)
ax.add_patch(rect)
ax.add_patch(polygon)
ax.add_patch(eclipse)

plt.grid(color='g',linestyle='--')
plt.axis('equal') # 把比例调对
plt.show()
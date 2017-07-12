# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
# 子图就是 在一张图里面生成多张图
# 多图 就是 生成多个 窗口 每个窗口可以容乃一个或多个图
fig1=plt.figure()

ax1=fig1.add_subplot(111)

ax1.plot([1,2,3],[3,2,1])

fig2=plt.figure()

ax2=fig2.add_subplot(111)

ax2.plot([1,2,3],[1,2,3])

plt.show()


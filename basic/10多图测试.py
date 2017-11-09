# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
# 子图就是 在一张图里面生成多张图
# 多图 就是 生成多个 窗口 每个窗口可以容乃一个或多个图
fig=plt.figure(figsize=[10,10])
ax1=fig.add_subplot(1,2,1)
ax1.plot([1,2,3],[3,2,1])

ax2=fig.add_subplot(1,2,2)
ax2.plot([1,2,3],[1,2,3])


plt.savefig('test.png')
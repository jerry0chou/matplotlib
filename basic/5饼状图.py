# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]

#explode = (0, 0, 0, 0)

# Make square figures and axes

plt.axes(aspect=1) #变成正圆，而不是椭圆


explode = (0, 0.1, 0, 0.2)# 给 ABCD 四个分区 加上 突出效果

#plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

plt.pie(fracs, explode=explode, labels=labels,
        autopct='%.2f%%',# 自动添加比列（格式化字符串）2表示两位小数  %%表示转义%
        shadow=True)



plt.show()
# -*- coding:utf-8 -*-
# Author : JerryChu
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

date, open, high, low, close = np.loadtxt('000001.csv', delimiter=',',
                                          converters={0: mdates.strpdate2num('%m/%d/%Y')}, skiprows=1,
                                           usecols=(0, 1, 2, 3, 4), unpack=True)
plt.plot_date(date, open, 'y-')  # y- 黄色的直线图
plt.plot_date(date, high, 'g-')  # g- 绿色的直线图
plt.plot_date(date, low, 'r--')
plt.plot_date(date, close, 'b-')
plt.show()

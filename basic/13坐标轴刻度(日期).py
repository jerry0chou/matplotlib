# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime

fig=plt.figure()

start=datetime.datetime(2016,1,1) # 设置开始日期
stop=datetime.datetime(2018,1,1) # 设置结束日期
delta=datetime.timedelta(days=5) # 设置间隔

dates=mpl.dates.drange(start,stop,delta) #

print len(dates) # dates:365*2/5=146
print dates

y=np.random.rand(len(dates))

ax=plt.gca()

ax.plot_date(dates,y,linestyle='-',marker='')

date_format=mpl.dates.DateFormatter('%Y-%m-%d')

ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate() # 自动调整日期长度和格式

plt.show()
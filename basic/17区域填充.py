# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,5*np.pi,1000)
y1=np.sin(x)
y2=np.sin(2*x)

''' 面向过程
plt.plot(x,y1)
plt.plot(x,y2)

plt.fill(x,y1,'r',alpha=0.3)
plt.fill(x,y2,'y',alpha=0.4)
'''

# OOP
fig=plt.figure()
ax=plt.gca()
ax.plot(x,y1,color='r',alpha=0.5)
ax.plot(x,y2,color='g',alpha=0.5)

#ax.fill_between(x,y1,y2,facecolor='y',alpha=0.3)
ax.fill_between(x,y1,y2,where=y1>y2,facecolor='y',alpha=0.3,interpolate=True) # interpolate自动将离散的值自动填充
ax.fill_between(x,y1,y2,where=y1<y2,facecolor='b',alpha=0.3,interpolate=True) # interpolate自动将离散的值自动填充

plt.show()
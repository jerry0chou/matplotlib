# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np

#r=np.arange(1,6,1)

r=np.empty(9)
r.fill(5)

theta=[x*np.pi/4 for x in range(9)]

ax=plt.subplot(111,projection='polar')
ax.plot(theta,r,color='r',linewidth=3)

ax.grid(True)
plt.show()
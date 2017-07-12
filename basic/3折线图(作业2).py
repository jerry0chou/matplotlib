# -*- coding:utf-8 -*-
# Author : JerryChu
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()

# x=np.linspace(-np.pi,np.pi,256,endpoint=True)
# C,S=np.cos(x),np.sin(x)
# plt.plot(x,C)
# plt.plot(x,S)
# plt.show()
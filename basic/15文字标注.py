# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np
#x=np.arange(-10,11,1)
x=np.linspace(-10,11,50)
y=x*x
plt.plot(x,y)

plt.text(-1.4,10,'f(x)=x*x1',family='serif',size=20,color='r',style='italic')
plt.text(-1.4,20,'f(x)=x*x2',family='fantasy',size=30,color='g',bbox=dict(facecolor='r',alpha=0.2))
plt.show()
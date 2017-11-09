# -*- coding:utf-8 -*-
# Author : JerryChu
#pyplot
import matplotlib.pyplot as plt
import numpy as np
# x=np.arange(0,10,1)
# y=np.random.randn(len(x))
# plt.plot(x,y)
# plt.title('pyplot')
# plt.show()
#
#
# #pylab
# from pylab import *
# x=arange(0,10,1)
# y=randn(len(x))
# plot(x,y)
# title('random numbers')
# show()


#Object Oriented
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(1,2,1)
plt.plot(x,y)
ax.set_title('object oriented')
fig.set_size_inches(18.5, 10.5)


ax=fig.add_subplot(1,2,2)
plt.plot(x,y*y)
ax.set_title('object oriented2')

plt.show()

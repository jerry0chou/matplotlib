# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(1,11,1)
y=x*x

plt.plot(x,x*2,label='Normal')

plt.plot(x,x*3,label='Fast')

plt.plot(x,x*4,label='Faster')

plt.legend(loc=3,ncol=2) # loc=0 表示自适应  其余 1 2 3 4 表示四个象限 ncol=2 表示有几列

plt.show()


#方式2

plt.plot(x,x*2)
plt.plot(x,x*3)
plt.plot(x,x*4)

plt.legend(['Normal','Fast','Faster']) # 用列表也可以写

plt.show()


#OO
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)

ax.legend(['ax legend'])
line, =ax.plot(x,y,label='Inline label')
line.set_label('label via method')
ax.legend()
plt.show()



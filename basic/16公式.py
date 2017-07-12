# -*- coding:utf-8 -*-
# Author : JerryChu
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=fig.add_subplot(111)
ax.axis([1,5,1,5])

# 官网文档 http://matplotlib.org/users/mathtext.html

ax.text(2,4,r'$\alpha_i > \beta_i$',size=30) # 表示不转义
ax.text(4,4,r'$\sum_{i=0}^\infty x_i$',size=15)
plt.show()
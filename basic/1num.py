# -*- coding:utf-8 -*-
# Author : JerryChu
import numpy as np

# Converting Python array_like Objects to Numpy arrays
a = [1, 2, 3, 4]
x1 = np.array(a)
x2 = np.array([a, a])

print(x1.shape)
print(x2.shape)

# 0
c = np.arange(11)

print c[1:5]

print c[:5]

print c[5:]

print c[::-1]

c = np.random.randint(1, 100, 10)
print '原始数据:',c
c_sort = np.sort(c)
print '排序数据np.sort()',c_sort
print  '排序数据c.sort()',c.sort()

mean = np.mean(c)
highest = np.max(c)
lowest = np.min(c)
median = np.median(c)
variance = np.var(c)
print '平均值:',mean,'最大值:',highest,'最小值:',lowest,'中位数:',median,'方差:',variance

c_slice = c[2:5]

c1 = np.zeros((2, 3))
c2 = np.arange(10)
print c1
print c2
x = np.loadtxt('000001.csv', # 文件名
               delimiter=',', # 分隔符
               skiprows=1, # 跳过行
               usecols=(1, 4, 6), # 使用哪几列
               unpack=False) # 分块
#print(c)

o, c, v = np.loadtxt('000001.csv', delimiter=',', skiprows=1, usecols=(1, 4, 6), unpack=True)
print o,c,v
vwap = np.average(c, weights=v)

print vwap

print "finish"

# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
print plt.style.available

f=open('results.txt')
length=0
trainRMSE=[]
testRMSE=[]
MAE=[]
for each in f:
    eachList = each.split("\t")
    trainRMSE.append(eachList[1])
    testRMSE.append(eachList[2])
    MAE.append(eachList[4].strip('\n'))
    length+=1

x=np.arange(0,length,1) # X轴

train=np.array(trainRMSE) # 三条曲线
test=np.array(testRMSE)
mae=np.array(MAE)

plt.plot(x,train)
plt.plot(test)
plt.plot(mae)
plt.title('alpha: 0.01  lambdau: 0.5 lambdav: 0.5 lambdauv 0.01')
plt.legend(['trainRMSE','testRMSE','mae'])
plt.xlabel('Iterations(n)')

plt.show()
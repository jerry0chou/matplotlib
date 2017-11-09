# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#print plt.style.available

f=open('results2.txt')
count=1
chartData=[]
chartHead=[]
for each in f:
    eachList = each.split("\t")
    if eachList[0].isdigit():
        chartData.append(eachList)
    elif eachList[0][0]=='M' or eachList[0][0]=='a':
         chartHead.append(eachList)

def plotChart(eachChartData,eachChartHead,ax):
    length=0
    trainRMSE=[]
    testRMSE=[]
    MAE=[]
    for each in eachChartData:  # data[0:20]
        if each[1] !='nan' and each[2]!='nan' and each[3]!='nan':
            trainRMSE.append(each[1])
            #print each[1],each[2],each[3].strip('\n')
            testRMSE.append(each[2])
            MAE.append(each[3].strip('\n'))
            length+=1

    x=np.arange(0,length,1) # X轴
    train=np.array(trainRMSE) # 三条曲线
    test=np.array(testRMSE)
    mae=np.array(MAE)

    ax.plot(x,train)
    ax.plot(x,test)
    ax.plot(x,mae)
    head=''
    for each in eachChartHead:
        size=len(each)
        each.insert((size+2)/2,'\n')
        for e in each:
            head=head+' '+e
    ax.set_title(head[0:-1])
    ax.legend(['trainRMSE','testRMSE','mae'])
    ax.set_xlabel('Iterations(n)')

length=len(chartData)/20
j=0
k=0
eachChartData = []
fig=plt.figure(figsize=[18,150]) #
#plt.subplots_adjust(bottom=0.1,top=0.95,wspace=0.5,hspace=1.3)
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                wspace=0.8, hspace=1.3)
#plt.subplots_adjust(hspace=1.3)
for i in range(length):
    ax = fig.add_subplot(22, 3, i+1)
    plotChart(chartData[j:j+20],chartHead[k:k+2],ax)
    j=(i+1)*20
    k=(i+1)*2
plt.savefig('123.png')
#encoding=utf-8
#!/usr/bin/python

from numpy import *
import operator

def kNNTest(intX,dataset,labels,k):
	datasetSize=dataset.shape[0]
	juzhen=tile(intX,(datasetSize,1))
	cha=juzhen-dataset
	squre=cha**2
	su=squre.sum(axis=1)
	dis=su**0.5
	sortdis=dis.argsort()
	dd={}
	for i in range(k):
		votelabels=labels[sortdis[i]]
		dd[votelabels]=dd.get(votelabels,0)+1
	sortedclasscount=sorted(dd.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedclasscount[0][0]
		
def file2matrix(filename):
	f=open(filename)
	#获取行数
	nl=len(f.readlines())
	#生成暂时的矩阵		
	returnMat=zeros((nl,3))
	classLabelVector=[]
	f=open(filename)
	index=0
	for line in f.readlines():
		line=line.strip()
		listfromline=line.split('\t')
		returnMat[index,:]=listfromline[0:3]
		classLabelVector.append((listfromline[-1]))
		index+=1
	return returnMat,classLabelVector

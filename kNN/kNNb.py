#encoding=utf-8
#!/usr/bin/python

from numpy import *
from os import listdir
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

def autoNorm(dataset):
	minVal=dataset.min(0)
	maxVal=dataset.max(0)
	returnMat=zeros(shape(dataset))
	ranges=maxVal-minVal
	m=dataset.shape[0]
	minMat=tile(minVal,(m,1))
	maxMat=tile(maxVal,(m,1))
	returnMat=(dataset-minMat)/(maxMat-minMat)
	return returnMat,ranges,minVal

def datingClassTest():
	dataMat,classLabels=file2matrix('/Users/user/Desktop/machinelearninginaction/Ch02/datingTestSet2.txt')
	print classLabels
	normMat,ranges,minVals=autoNorm(dataMat)
	size=normMat.shape[0]
	flag=0.1
	partSize=int(size*flag)
	errorCount=0.0
	for i in range(partSize):
		classifierResult=kNNTest(normMat[i,:],normMat[partSize:size,:],classLabels,3)
		print 'the classifier came back with: %d, the real answer is: %d'\
			%(int(classifierResult),int(classLabels[i]))
		if classifierResult!=classLabels[i]:errorCount+=1.0
	print "the total error rate is: %f" %(errorCount/float(partSize))

def classifyPerson():
	resultList=['not at all','in small doses','in large doses']
	percentTats=float(raw_input('percentage of time spent playing video games?'))
	ffMiles=float(raw_input('frequent flier miles earned per year?'))
	iceCream=float(raw_input('liters of ice cream consumed per year?'))
	datingDataMat,datingLabels=file2matrix('../traningdata/Ch02/datingTestSet2.txt')
	normMat,ranges,minVal=autoNorm(datingDataMat)
	inArray=array([ffMiles,percentTats,iceCream])
	classifierPerson=kNNTest((inArray-minVal)/ranges,normMat,datingLabels,3)
	print 'you will probably like this person:',resultList[int(classifierPerson)-1]
	
def img2vector(filename):
	returnVect=zeros((1,1024))
	fo=open(filename)
	for j in range(32):
		f=fo.readline()
		for i in range(32):
			returnVect[0,32*j+i]=int(f[i])
	return returnVect

def handwritingClassTest(filepath):
	trianingFile='%s/trainingDigits'%(filepath)
	exampleFiles=listdir(trianingFile)
	m=len(exampleFiles)
	trianData=zeros((m,1024))
	hwlabels=[]
	for i in range(m):
		f=exampleFiles[i]
		fname=f.split('.')[0]
		fname=fname.split('_')[0]
		hwlabels.append(fname)
		trianData[i,]=img2vector('%s/%s'%(trianingFile,f))
	
	errorCount=0.0
	testFile='%s/testDigits'%(filepath)
	testFiles=listdir(testFile)
	mt=len(testFiles)
	testData=zeros((mt,1024))
	for j in range(mt):
		f=testFiles[j]
		fname=f.split('.')[0]
		fname=fname.split('_')[0]
		unitTestData=img2vector('%s/%s'%(testFile,f))
		result=kNNTest(unitTestData,trianData,hwlabels,3)
		print "the classifier came back with: %d, the real answer is: %d"\
			%(int(result),int(fname))
		if result!=fname:
			errorCount+=1.0
	print "\nthe total number of errors is: %d" % errorCount
	print "\nthe total error rate is: %f" % (errorCount/float(mt))
						

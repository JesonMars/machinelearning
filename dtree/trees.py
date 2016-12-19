#!/usr/bin/python
#coding=utf8

from math import log

def calcShannonEnt(dataset):
	tcount=len(dataset)
	labels={}
	for i in dataset:
		t=i[-1]
		if t not in labels.keys():
			labels[t]=0
		labels[t]+=1
	shannonEnt=0.0
	for k in labels:
		prob=float(labels[k])/tcount
		shannonEnt-=prob*log(prob,2)
	return shannonEnt
			
def createDataSet():
	dataset=[[1,1,'yes'],
			[1,1,'yes'],
			[1,0,'no'],
			[0,1,'no'],
			[0,1,'no']]
	labels=['no surfacing','flippers']
	return dataset,labels
	
def splitDataSet(dataset,axis,value):
	returnData={}
	for i in dataset:
		if i[axis]==value:
			returndatatmp=i[:axis]
			returndatatmp.extend(i[axis+1:])
			returnData.append(returndatatmp)
	return returnData
	

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:45:26 2017

@author: leonidas
"""

import numpy as np
import operator
def classify(inputPoint,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat     = np.tile(inputPoint,(dataSetSize,1))-dataSet  
    sqDiffMat   = pow(diffMat,2)
    sqDistances = sqDiffMat.sum(axis=1)         
    distances   = pow(sqDistances,0.5)             
    sortedDistIndicies = distances.argsort()
    classCount  = {}
    for i in range(k):
        voteIlabel = labels[ sortedDistIndicies[i] ]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #sort by the apperance number
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]


def mat_to_vect(filename):
    vect = []
    data = open(filename)
    for i in range(32):
        temp = data.readline()
        for j in range(32):
            try:
                vect.append(int(temp[j]))
            except(ValueError):
                print temp[j],'error',ValueError
    return vect


def load_train_data():
    train_lables    = []
    size            = 100
    train_data      = np.zeros((size*10,1024))
    for i in range(10):
        for j in range(size):
            train_lables.append(i)
            train_data[i*100+j,:]  = mat_to_vect('train/%s/%s.txt' %( i,j ))
    return train_lables,train_data

def classnumCut(fileName):  
	return int(fileName[0])
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:48:57 2017

@author: leonidas
"""
import load as l
import time
from os import listdir
def accuracy_test():
    train_lables,train_data = l.load_train_data()       #load training set
    testFileList = listdir('test')                      #get the test set
    errorCount = 0.0                                    #number of error
    mTest = len(testFileList)                           #test samples
    init = time.clock()
    for i in range(mTest):
        fileNameStr = testFileList[i]
        classNumStr = l.classnumCut(fileNameStr)
        vectorUnderTest = l.mat_to_vect('test/%s' % fileNameStr)
        #call the classifier to test
        classifierResult = l.classify(vectorUnderTest, train_data, train_lables, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nTest set size:\t %d" % mTest               #print the test set size
    print "Error detection:\t %d" % errorCount          #print the number of error detection
    print "Error rate is:\t %f" % (errorCount/float(mTest))  #print the error rate
    end = time.clock()
    print "Run time:\t\t %.4fs."% (end-init)            #code run time
if __name__ == "__main__":
    accuracy_test()
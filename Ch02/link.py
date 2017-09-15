import parser
import normalize
import classify
from numpy import *

testRatio = 0.10
dataSet, label = parser.file2matrix('datingTestSet.txt')
normMat, ranges, minval = normalize.autoNormal(dataSet)
m = normMat.shape[0]
testVectors = int(m * testRatio)
error = 0
for i in range(testVectors):
    res = classify.classify(normMat[i,:], normMat[testVectors:m,:], label[testVectors:m], 3)
    #print("retrun : %d, real : %d" % (res, label[i]))
    if res != label[i]:
        error += 1
print("Error percentage : %f" % (error/float(testVectors)))

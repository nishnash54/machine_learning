from numpy import *
import operator

def classify(inx, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diff = tile(inx, (dataSetSize, 1)) - dataSet
    sqdiff = diff**2
    sqdist = sqdiff.sum(axis = 1)
    distances = sqdist**0.5
    sortedDist = distances.argsort()
    count = {}
    for i in range(k):
        voteLabel = labels[sortedDist[i]]
        count[voteLabel] = count.get(voteLabel, 0) + 1
    sortedCount = sorted(count.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedCount[0][0]

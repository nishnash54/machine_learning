from numpy import *
import parser

def autoNormal(dataSet):
    minval = dataSet.min(0)
    maxval = dataSet.max(0)
    ranges = maxval - minval
    normdataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normdataSet = dataSet - tile(minval, (m, 1))
    normdataSet = normdataSet/tile(ranges, (m, 1))
    return(normdataSet, ranges, minval)

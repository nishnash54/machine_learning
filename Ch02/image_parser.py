import numpy as np

def image2vector(filename):
    returnVect = np.zeros((1, 1024))
    fl = open(filename)
    for i in range(32):
        line = fl.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(line[j])
    return returnVect

import numpy as np

def file2matrix(filename):
    fl = open(filename)
    lines = len(fl.readlines())
    retMat = np.zeros((lines, 3))
    vector = []
    fl = open(filename)
    index = 0
    label = []
    for line in fl.readlines():
        line = line.strip()
        lst = line.split('\t')
        retMat[index,:] = lst[0:3]
        label.append(lst[-1])
        index += 1
    return retMat, label

print(file2matrix('datingTestSet.txt'))

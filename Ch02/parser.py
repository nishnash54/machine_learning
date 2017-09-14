import numpy as np
import operator

def file2matrix(filename):
    dic = {}
    typ = 1
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
        if lst[-1] not in dic:
            dic[lst[-1]] = typ
            typ += 1
        label.append(dic[lst[-1]])
        index += 1
    return retMat, label

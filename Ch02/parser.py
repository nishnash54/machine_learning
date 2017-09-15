import numpy as np
import operator

def file2matrix(filename):
    dic = {'largeDoses': 2, 'smallDoses': 1, 'didntLike': 0}
    typ = 0
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
        label.append(dic[lst[-1]])
        index += 1
    return retMat, label

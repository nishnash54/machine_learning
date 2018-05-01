import numpy as np
import pandas as pd
from os import listdir
import matplotlib.pyplot as plt
from sklearn import neighbors

def img2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

if __name__ == "__main__":

    file_list = listdir('trainingDigits')
    m = len(file_list)
    X_train = np.zeros((m, 1024))
    Y_train = []

    for i in range(m):

        file_name = file_list[i]
        X_train[i] = img2vector('trainingDigits/%s' % file_name)
        Y_train.append(int(file_name.split('_')[0]))

    # print(X_train, Y_train)

    file_list = listdir('testDigits')
    m = len(file_list)
    X_test = np.zeros((m, 1024))
    Y_test = []

    for i in range(m):

        file_name = file_list[i]
        X_test[i] = img2vector('trainingDigits/%s' % file_name)
        Y_test.append(int(file_name.split('_')[0]))

    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, Y_train)
    res = knn.score(X_test, Y_test)

    print("Result: %s" % str(res))

import numpy as np
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":

    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')

    X_train = []
    Y_train = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        X_train.append(lineArr)
        Y_train.append(float(currLine[21]))

    # print(X_train)
    # print(Y_train)

    X_test = []
    Y_test = []
    for line in frTest.readlines():
        numTestVec = 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        X_test.append(lineArr)
        Y_test.append(float(currLine[21]))

    # print(X_test)
    # print(Y_test)

    lr = LogisticRegression()
    lr.fit(X_train, Y_train)
    res = lr.score(X_test, Y_test)

    print("Result: %s" % res)

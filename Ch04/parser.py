import re
from word2vec import *
from train import *
from numpy import *

def textParser(string):
    tokens = re.split(r'\W*', string)
    return [tok.lower() for tok in tokens if len(tok) > 3]

def trainingSet():
    docList = []
    fulltext = []
    classList = []
    for i in range(1, 26):
        wordList = textParser(open('email/spam/%d.txt'%i).read())
        docList.append(wordList)
        fulltext.extend(wordList)
        classList.append(1)
        wordList = textParser(open('email/ham/%d.txt'%i).read())
        docList.append(wordList)
        fulltext.extend(wordList)
        classList.append(0)
    vocabulary = create_vocab(docList)
    training = range(50)
    testset = []
    for i in range(10):
        ind = int(random.uniform(0, len(training)))
        testset.append(training[ind])
        del(training[ind])
    trainingmat = []
    trainingclasses = []
    for doc in training:
        trainingmat.append(word2vector(vocabulary, docList[doc]))
        trainingclasses.append(classList[doc])
    p0, p1, pspam = train(array(trainingmat), array(trainingclasses))
    error = 0.0
    for doc in testset:
        wordVec = word2vector(vocabulary, docList[doc])
        if classify(array(wordVec), p0, p1, pspam) != classList[doc]:
            error += 1
            print 'Classification error in ', docList[doc]
    print 'The error percentage is : ', float(error)/len(testset)

trainingSet()

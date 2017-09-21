from numpy import *
import word2vec

def train(data, inp):
    num_train = len(data)
    num_words = len(data[0])
    pAbusive = sum(inp)/float(num_train)
    p0num = ones(num_words)
    p1num = ones(num_words)
    p0den = 2.0
    p1den = 2.0
    for i in range(num_train):
        if inp[i] == 1:
            p1num += data[i]
            p1den += sum(data[i])
        else:
            p0num += data[i]
            p0den += sum(data[i])
    p0 = log(p0num/p0den)
    p1 = log(p1num/p1den)
    return p0, p1, pAbusive

def classify(vec, p0, p1, pAbusive):
    p = sum(vec * p1) + log(pAbusive)
    np = sum(vec * p0) + log(1.0 - pAbusive)
    if p > np:
        return 1
    return 0


data, vector = word2vec.create_dataset()
vocabulary = word2vec.create_vocab(data)
train_data = []
for each in data:
    train_data.append(word2vec.word2vector(vocabulary, each))
p0, p1, pAbusive = train(train_data, vector)
#test = ['love', 'my', 'dalmation']
test = ['stupid', 'garbage']
testVec = word2vec.word2vector(vocabulary, test)
print test, 'classified as : ', classify(testVec, p0, p1, pAbusive)

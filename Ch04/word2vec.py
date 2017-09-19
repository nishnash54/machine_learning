def create_dataset():
  lst = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
  vec = [0, 1, 0, 1, 0, 1]
  return lst, vec

def create_vocab(dataset):
    vocab = set([])
    for each in dataset:
        vocab = vocab | set(each)
    return list(vocab)

def word2vector(vocablist, inp):
    ret = [0] * len(vocablist)
    for word in inp:
        if word in vocablist:
            ret[vocablist.index(word)] = 1
        else :
            print "The word %s is not in my voacbulary" % word
    return ret

data, vector = create_dataset()
vocabulary = create_vocab(data)
print(word2vector(vocabulary, data[0]))

import tree

def classify(inp, labels, test):
    first = inp.keys()[0]
    sec = inp[first]
    ind = labels.index(first)
    for key in sec.keys():
        if test[ind] == key:
            if type(sec[key]).__name__=='dict':
                ret = classify(sec[key], labels, test)
            else:
                ret = sec[key]
    return ret

inp, labels = tree.return_inp()
print(classify(inp, labels, [1, 0]))

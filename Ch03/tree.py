from entropy import *
from split_data import *
import operator

def majority(lst):
    count = {}
    for each in lst:
        if each in count.keys():
            count[each] += 1
        count[each] = 0
    sort = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sort[0][0]

def tree(dataset, labels):
    lst = [each[-1] for each in dataset]
    if lst.count(lst[0]) == len(lst):
        return lst[0]
    if len(dataset[0]) == 1:
        return majority(lst)
    feature = best_split(dataset)
    label = labels[feature]
    myTree = {label:{}}
    del(labels[feature])
    values = [each[feature] for each in dataset]
    for val in set(values):
        myTree[label][val] = tree(split_data(dataset, feature, val), labels)
    return myTree

def return_inp():
    data, labels = entropy.create_dataset()
    print(data, labels)
    myTree = tree(data, labels)
    data, labels = entropy.create_dataset()
    print(myTree)
    return myTree, labels

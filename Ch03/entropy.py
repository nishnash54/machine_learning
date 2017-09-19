from math import log

def calc_entropy(dataset):
    num = len(dataset)
    label = {}
    for vec in dataset:
        if vec[-1] not in label:
            label[vec[-1]] = 0
        label[vec[-1]] += 1
    entropy = 0.0
    for key in label:
        prob = float(label[key])/num
        entropy += prob * log(prob, 2)
    return -entropy

def create_dataset():
    dataset = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']

    '''f = open('lenses.txt')
    dataset = [each.strip().split('\t') for each in f.readlines()]
    labels = ['age', 'prescript', 'astigmatic', 'tearRate']'''
    return dataset, labels

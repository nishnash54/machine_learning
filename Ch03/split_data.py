import entropy

def split_data(dataset, axis, value):
    ret = []
    for vec in dataset:
        if vec[axis] == value:
            reduced = vec[:axis]
            reduced.extend(vec[axis+1:])
            ret.append(reduced)
    return ret

def best_split(dataset):
    features = len(dataset[0]) - 1
    ent = entropy.calc_entropy(dataset)
    infoGain = 0.0
    feature = -1
    for i in range(features):
        lst = [each[i] for each in dataset]
        new_entropy = 0.0
        for value in set(lst):
            newdataset = split_data(dataset, i, value)
            prob = len(newdataset)/float(len(dataset))
            new_entropy += prob * entropy.calc_entropy(newdataset)
        gain = ent - new_entropy
        if gain > infoGain:
            infoGain = gain
            feature = i
    return(feature)

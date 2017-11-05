import os
import image_parser
import numpy as np
import classify

def handwriting():
    hwlabel = []
    filelist = os.listdir('trainingDigits')
    m = len(filelist)
    trainMat = np.zeros((m, 1024))
    for i in range(m):
        name = filelist[i].split('.')[0]
        num = int(name.split('_')[0])
        hwlabel.append(num)
        trainMat[i,:] = image_parser.image2vector('trainingDigits/'+filelist[i])
    filelist = os.listdir('testDigits')
    m = len(filelist)
    error = 0
    testMat = np.zeros((1, 1024))
    for i in range(m):
        label = int(filelist[i].split('.')[0].split('_')[0])
        testMat = image_parser.image2vector('testDigits/'+filelist[i])
        res = classify.classify(testMat, trainMat, hwlabel, 3)
        #print "Return value : %d Actual value : %d" % (res, label)
        if res != label:
            error += 1
    print "Files : %d" % (m)
    print "Errors : %d " % (error)
    print "Error percentage : %f" % (error*100/float(m))

handwriting()

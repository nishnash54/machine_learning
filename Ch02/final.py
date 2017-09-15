import parser
import normalize
import classify
from numpy import *

resList = ['not at all', 'in small doses', 'in large doses']
videogames = float(input('Percentage of time spent playing video games : '))
miles = float(input('Miles earned per year : '))
icecream = float(input('Litres of icecream comsumed : '))
dataArray = array([miles, videogames, icecream])

dataSet, label = parser.file2matrix('datingTestSet.txt')
normMat, ranges, minval = normalize.autoNormal(dataSet)
res = classify.classify(dataArray, dataSet, label, 3)
print 'You will like this person : ', resList[res]
